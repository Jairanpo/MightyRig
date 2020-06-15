import maya.cmds as cmds
translate=None
rot=None
def Get_Trans_Rot(Name):#OBTENER TRASLACION Y ROTACION DE UN OBJETO
    global translate,rot
    translate = cmds.xform (Name, ws=True, q=True, t=True)
    rot = cmds.xform (Name, ws=True, q=True, ro=True)
def Set_Trans_Rot(Name):#INSERTAR TRASLACION Y ROTACION A UN OBJETO
    global Parent_Trans,Parent_Rot
    Parent_Trans = cmds.xform (Name, ws=True, t=translate)
    Parent_Rot = cmds.xform (Name, ws=True, ro=rot)
def Groups_Twist(Grp,Z_Grp):
    cmds.group(n=Grp,em=True)
    cmds.group(n=Z_Grp)
def Locator(Locator,Offset):
    cmds.spaceLocator(n=Locator,p=(0,0,0))
    cmds.group(n=Offset)
def CreateNode(Node,name_node):
    cmds.shadingNode(Node,n=name_node,au=True)
def Twist_Leg_L():
    Scale_Guide=cmds.xform('Guide_Scale_Grp',ws=True, q=True, s=True )[0]
    num=1
    List=['J_Leg_Neutral_L','J_ForeLeg_Neutral_L','J_Ankle_Neutral_L']
    for J in List:
        N=J.split('_Neutral_L')[0]
        New_Name=N.split('J_')[1]
        Groups_Twist(New_Name+'_Twist_L','Z_'+New_Name+'_Twist_L')
        Get_Trans_Rot('J_'+New_Name+'_Neutral_L')
        Set_Trans_Rot('Z_'+New_Name+'_Twist_L')
        cmds.select(cl=True)
        #Locator
        Locator('Loc_Extract_'+New_Name+'_L','Z_Loc_Extract_'+New_Name+'_L')
        Set_Trans_Rot('Z_Loc_Extract_'+New_Name+'_L')
        cmds.select(cl=True)
        #EFFECTOR
        Groups_Twist(New_Name+'_Eff_Twist_L','Z_'+New_Name+'_Eff_Twist_L')
        Get_Trans_Rot(List[num])
        Set_Trans_Rot('Z_'+New_Name+'_Eff_Twist_L')
        cmds.select(cl=True)
        cmds.group(n='Twist_'+New_Name+'_L',em=True)
        cmds.parent('Z_'+New_Name+'_Eff_Twist_L','Twist_'+New_Name+'_L')
        cmds.parent('Z_'+New_Name+'_Twist_L','Twist_'+New_Name+'_L')
        cmds.parent('Z_Loc_Extract_'+New_Name+'_L','Twist_'+New_Name+'_L')
        cmds.select(cl=True)
        if num<2:
            num=num+1
        #CREATE_NODES#
        cmds.shadingNode('multMatrix',n='MMX_'+New_Name+'_L',au=True)
        cmds.shadingNode('decomposeMatrix',n='DCM_'+New_Name+'_L',au=True)
        cmds.shadingNode('quatToEuler',n='QTE_'+New_Name+'_L',au=True)
        #CONNECT ATTRIBUTES#
        cmds.connectAttr(New_Name+'_Twist_L.worldMatrix[0]','MMX_'+New_Name+'_L.matrixIn[0]')
        cmds.connectAttr(New_Name+'_Eff_Twist_L.worldInverseMatrix','MMX_'+New_Name+'_L.matrixIn[1]')
        cmds.connectAttr('MMX_'+New_Name+'_L'+'.matrixSum','DCM_'+New_Name+'_L'+'.inputMatrix')
        cmds.connectAttr('DCM_'+New_Name+'_L'+'.outputQuatX','QTE_'+New_Name+'_L'+'.inputQuatX')
        cmds.connectAttr('DCM_'+New_Name+'_L'+'.outputQuatW','QTE_'+New_Name+'_L'+'.inputQuatW')
        cmds.connectAttr('QTE_'+New_Name+'_L'+'.outputRotate','Loc_Extract_'+New_Name+'_L'+'.rotate')
    cmds.move(2*Scale_Guide,0,0,'Z_Ankle_Eff_Twist_L',r=True,os=True,wd=True)
    Joints=['Leg','ForeLeg']
    for Joint in Joints:
        if Joint=='ForeLeg':
            CreateNode('multDoubleLinear','MDL_'+Joint+'_00_Twist_L')
            cmds.connectAttr('Loc_Extract_'+Joint+'_L.rotate','J_Bendy_3_Leg_L.rotate')
            cmds.connectAttr('Loc_Extract_'+Joint+'_L.rotateX','MDL_'+Joint+'_00_Twist_L.input1')
            cmds.connectAttr('MDL_'+Joint+'_00_Twist_L.output','J_Bendy_1_'+Joint+'_L.rotateX')
            cmds.connectAttr('J_'+Joint+'_Neutral_L.rotate',Joint+'_Twist_L.rotate')    
            CreateNode('multDoubleLinear','MDL_'+Joint+'_01_Twist_L')
            cmds.setAttr('MDL_'+Joint+'_01_Twist_L.input2',.5)
            cmds.connectAttr('Loc_Extract_'+Joint+'_L.rotateX','MDL_'+Joint+'_01_Twist_L.input1')
            cmds.connectAttr('MDL_'+Joint+'_01_Twist_L.output','J_Bendy_2_Leg_L.rotateX')
        else:
            CreateNode('multDoubleLinear','MDL_'+Joint+'_00_Twist_L')
            cmds.setAttr('MDL_'+Joint+'_00_Twist_L.input2',-1)
            cmds.connectAttr('Loc_Extract_'+Joint+'_L.rotateX','MDL_'+Joint+'_00_Twist_L.input1')
            cmds.connectAttr('MDL_'+Joint+'_00_Twist_L.output','J_Bendy_1_'+Joint+'_L.rotateX')
            cmds.connectAttr('J_'+Joint+'_Neutral_L.rotate',Joint+'_Twist_L.rotate')    
            CreateNode('multDoubleLinear','MDL_'+Joint+'_01_Twist_L')
            cmds.setAttr('MDL_'+Joint+'_01_Twist_L.input2',-.5)
            cmds.connectAttr('Loc_Extract_'+Joint+'_L.rotateX','MDL_'+Joint+'_01_Twist_L.input1')
            cmds.connectAttr('MDL_'+Joint+'_01_Twist_L.output','Z_J_Bendy_2_'+Joint+'_L.rotateX')           
    CreateNode('multDoubleLinear','MDL_Ankle_00_Twist_L')
    cmds.connectAttr('Loc_Extract_Ankle_L.rotateX','MDL_Ankle_00_Twist_L.input1')
    cmds.connectAttr('J_Ankle_Neutral_L.rotate','Ankle_Twist_L.rotate')    
    cmds.setAttr('MDL_Ankle_00_Twist_L.input2',.5)
    cmds.connectAttr('MDL_Ankle_00_Twist_L.output','Z_J_Bendy_2_ForeLeg_L.rotateX')
    cmds.group(n='Twists_Leg_L',em=True)
    cmds.select(cl=True)
    cmds.parent('Twists_Leg_L','hidden')
    cmds.select(cl=True)
    Twist_Leg=['Leg','ForeLeg','Ankle']
    for twist in Twist_Leg:
        cmds.parent('Twist_'+twist+'_L','Twists_Leg_L')
        cmds.select(cl=True)
    cmds.hide('Twists_Leg_L')