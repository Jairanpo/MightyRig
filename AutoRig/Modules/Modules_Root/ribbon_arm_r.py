import maya.cmds as cmds
import maya.mel as mel
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
def Point_Cons(Ctrl,Z_Ctrl):
    cmds.pointConstraint(Ctrl,Z_Ctrl,mo=True)
def Ribbon_Arm_R():
    Scale_Guide=cmds.xform('Guide_Scale_Grp',ws=True, q=True, s=True )[0]
    Create_Nurb_Rib_Arm_R= cmds.nurbsPlane(n="Rib_Arm_R",p=[0,0,0],ax=[0,-1,0],w=6,lr=0.167,d=3,u=6,v=1,ch=1)#CREAR PLANO_ARM
    Get_Trans_Rot('J_Arm_Neutral_R')
    Set_Trans_Rot(Create_Nurb_Rib_Arm_R)
    cmds.parent("Rib_Arm_R","J_Arm_Neutral_R")
    cmds.rename('makeNurbPlane1', 'makeRib_Arm_R')
    Extract_TransX_ForeArm_R = cmds.getAttr ("J_ForeArm_Neutral_R.translateX")
    Divide_TransX_ForeArm_R= ((Extract_TransX_ForeArm_R)/2)
    Move_TransX_RibArm_R = cmds.setAttr ("Rib_Arm_R.translateX",Divide_TransX_ForeArm_R)
    Scale_Nurb_Rib_Arm_R= cmds.setAttr ("makeRib_Arm_R.width", Extract_TransX_ForeArm_R)      
    Create_Nurb_Rib_ForeArm_R= cmds.nurbsPlane(n="Rib_ForeArm_R",p=[0,0,0],ax=[0,-1,0],w=6,lr=0.167,d=3,u=6,v=1,ch=1)#CREAR PLANO_FOREARM
    Get_Trans_Rot('J_ForeArm_Neutral_R')
    Set_Trans_Rot(Create_Nurb_Rib_ForeArm_R)
    Parent_J_ForeArm_Neutral_R=cmds.parent("Rib_ForeArm_R","J_ForeArm_Neutral_R")
    Rename_MakeNurb=cmds.rename('makeNurbPlane1', 'makeRib_ForeArm_R')
    Extract_TransX_Hand_R = cmds.getAttr ("J_Hand_Neutral_R.translateX")
    Divide_TransX_Hand_R= ((Extract_TransX_Hand_R)/2)
    Move_TransX_RibForeArm_R = cmds.setAttr ("Rib_ForeArm_R.translateX",Divide_TransX_Hand_R)
    Scale_Nurb_Rib_ForeArm_R= cmds.setAttr ("makeRib_ForeArm_R.width", Extract_TransX_Hand_R)
    cmds.parent("Rib_Arm_R",w=True)
    cmds.parent("Rib_ForeArm_R",w=True) 
    cmds.select(cl=True)
    List_Pos_J_Arms=['J_Arm_Neutral_R','J_ForeArm_Neutral_R']
    Joints=('J_ForeArm_Neutral_R')
    for J_1 in List_Pos_J_Arms:#FOR PARA POSICIONAR Y ORIENTAR LOS CTRLS BENDY
        N = J_1.split("_Neutral_R")[0]
        New_Name=N.split("J_")[1]
        print New_Name
        cmds.joint(n='J_Bendy_1_'+New_Name+'_R',r=True,rad=1*Scale_Guide)#1
        cmds.group(n='Z_J_Bendy_1_'+New_Name+'_R')
        cmds.hide('Z_J_Bendy_1_'+New_Name+'_R')
        cmds.select(cl=True)        
        cmds.parent('Z_J_Bendy_1_'+New_Name+'_R','R_Bendy'+New_Name+'_01_CTL')
        cmds.select(cl=True)
        Get_Trans_Rot(J_1)
        Set_Trans_Rot('P_R_Bendy'+New_Name+'_01_CTL')
        cmds.joint(n='J_Bendy_2_'+New_Name+'_R',r=True,rad=1*Scale_Guide)#2
        cmds.group(n='Z_J_Bendy_2_'+New_Name+'_R')
        cmds.hide('Z_J_Bendy_2_'+New_Name+'_R')
        cmds.parent('Z_J_Bendy_2_'+New_Name+'_R','R_Bendy'+New_Name+'_02_CTL')
        cmds.select(cl=True)
        Get_Trans_Rot(J_1)
        Set_Trans_Rot('P_R_Bendy'+New_Name+'_02_CTL')
        cmds.parent('P_R_Bendy'+New_Name+'_02_CTL',J_1)
        cmds.setAttr ('P_R_Bendy'+New_Name+'_02_CTL.translateX',Divide_TransX_ForeArm_R)
        cmds.parent('P_R_Bendy'+New_Name+'_02_CTL',w=True) 
        cmds.select(cl=True)   
        cmds.joint(n='J_Bendy_3_'+New_Name+'_R',r=True,rad=1*Scale_Guide)#3
        cmds.group(n='Z_J_Bendy_3_'+New_Name+'_R')     
        cmds.parent('Z_J_Bendy_3_'+New_Name+'_R','R_Bendy'+New_Name+'_03_CTL')
        cmds.select(cl=True)
        Get_Trans_Rot(Joints)
        Set_Trans_Rot('P_R_Bendy'+New_Name+'_03_CTL')
        Joints=('J_Hand_Neutral_R')
        Divide_TransX_ForeArm_R=Divide_TransX_Hand_R
    Get_Trans_Rot('J_ForeArm_Neutral_R')
    Set_Trans_Rot('P_R_BendyMasterArm_CTL')
    Skn_Arm_Rib_R=cmds.skinCluster('J_Bendy_1_Arm_R', 'J_Bendy_2_Arm_R','J_Bendy_3_Arm_R', 'Rib_Arm_R',dr=4,tsb=True,mi=4)[0]
    Skn_For_ForeArm_R=cmds.skinCluster('J_Bendy_1_ForeArm_R','J_Bendy_2_ForeArm_R','J_Bendy_3_ForeArm_R', 'Rib_ForeArm_R',dr=4,tsb=True,mi=4)[0]
    List_J_Bendys_Arm=[Skn_Arm_Rib_R,Skn_For_ForeArm_R]#LISTA DE LOS NOMBRES DE LOS SKINS DE LOS PLANOS
    Name_Nurb='Rib_Arm_R'
    Joint_Skin='Arm_'
    for Skn in List_J_Bendys_Arm:#FOR PARA LIMPIAR LOS PESOS DEL SKIN DE LOS PLANOS
        cmds.skinPercent(Skn,Name_Nurb+'.cv[0][0:3]',tv=['J_Bendy_1_'+Joint_Skin+'R',1])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[1][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.2])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[1][0:3]',tv=['J_Bendy_3_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[2][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.6])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[2][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.6])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[2][0:3]',tv=['J_Bendy_3_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[3][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.9])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[3][0:3]',tv=['J_Bendy_3_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[4][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',1])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[5][0:3]',tv=['J_Bendy_1_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[5][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.9])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[6][0:3]',tv=['J_Bendy_1_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[6][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.6]) 
        cmds.skinPercent(Skn,Name_Nurb+'.cv[7][0:3]',tv=['J_Bendy_1_'+Joint_Skin+'R',0])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[7][0:3]',tv=['J_Bendy_2_'+Joint_Skin+'R',0.2])
        cmds.skinPercent(Skn,Name_Nurb+'.cv[8][0:3]',tv=['J_Bendy_3_'+Joint_Skin+'R',1])
        Name_Nurb='Rib_ForeArm_R'
        Joint_Skin='ForeArm_'
    Point_Cons('R_BendyMasterArm_CTL','Z_R_BendyArm_03_CTL')
    Point_Cons('R_BendyMasterArm_CTL','Z_R_BendyForeArm_01_CTL')
    Point_Cons('R_BendyMasterArm_CTL','Z_R_BendyForeArm_02_CTL')
    Point_Cons('R_BendyMasterArm_CTL','Z_R_BendyArm_02_CTL')
    Point_Cons('R_BendyForeArm_03_CTL','Z_R_BendyForeArm_02_CTL')
    Point_Cons('R_BendyArm_01_CTL','Z_R_BendyArm_02_CTL')
    XYZ=['X','Y','Z']
    Ctrls_Bendy=['R_BendyForeArm_01_CTL','R_BendyArm_03_CTL']
    for Ctrl in Ctrls_Bendy: #FOR PARA CONECTAR LAS ROTATICIONES DEL CTR_BENDY_MASTER A LOS CONTROLES 1_FOREARM Y 3_ARM
        for xyz in XYZ:
            cmds.connectAttr('R_BendyMasterArm_CTL.rotate'+xyz,Ctrl+'.rotate'+xyz, f=True)
    cmds.hide('R_BendyArm_03_CTL','R_BendyArm_01_CTL','R_BendyForeArm_01_CTL','R_BendyForeArm_03_CTL','R_BendyForeArm_01_CTL')
    #FOR PARA CONTRAINTS AIMS
    Joints=['Arm','ForeArm']
    Valor_Pos=1
    Valor_Neg=-1
    Num_Ctrl_Father='1'
    Num_Ctrl_Children_1='3'
    Num_Ctrl_Children_2='1'
    Num_Ctrl_Children_3='2'
    for Ctrl in Joints:  
        cmds.aimConstraint('R_Bendy'+Ctrl+'_0'+Num_Ctrl_Father+'_CTL','Z_R_Bendy'+Ctrl+'_0'+Num_Ctrl_Children_1+'_CTL',mo=True,aim=[Valor_Pos,0,0],u=[1,0,0],wu=[0,1,0],wut="objectrotation",worldUpObject='R_Bendy'+Ctrl+'_0'+Num_Ctrl_Father+'_CTL')
        cmds.aimConstraint('R_BendyMasterArm_CTL','Z_R_Bendy'+Ctrl+'_0'+Num_Ctrl_Children_2+'_CTL',mo=True,aim=[Valor_Neg,0,0],u=[1,0,0],wu=[0,1,0],wut="objectrotation",worldUpObject='R_BendyMasterArm_CTL')
        cmds.aimConstraint('R_BendyMasterArm_CTL','Z_R_Bendy'+Ctrl+'_0'+Num_Ctrl_Children_3+'_CTL',mo=True,aim=[Valor_Neg,0,0],u=[1,0,0],wu=[0,1,0],wut="objectrotation",worldUpObject='R_BendyMasterArm_CTL') 
        Valor_Pos=-1
        Valor_Neg=1
        Num_Ctrl_Father='3'
        Num_Ctrl_Children_1='1'
        Num_Ctrl_Children_2='2'
        Num_Ctrl_Children_3='3'
   #FOR PARA CONTRAINTS AIMS
    cmds.group(n='Z_Ribs_Nurb_Arm_R',em=True)
    cmds.parent('Rib_ForeArm_R','Z_Ribs_Nurb_Arm_R')
    cmds.parent('Rib_Arm_R','Z_Ribs_Nurb_Arm_R')
    cmds.select(cl=True) 
    cmds.select('Rib_Arm_R','Rib_ForeArm_R')
    sel= cmds.ls (selection=True)
    lsel= len(sel)
    for nurb in range(lsel):#FOR PARA LOS RIVETS DE LOS RIBBON
        cmds.group(n=('Locs_'+(sel[nurb])),em=True)
        Gett_Spans_Nurb=cmds.getAttr(sel[nurb]+'.spansU')
        print Gett_Spans_Nurb
        if Gett_Spans_Nurb>1:
            U='U'
            V='V'
            maxValue=cmds.getAttr(sel[nurb]+'.minMaxRangeU.maxValue'+U)
        else:
            U='V'
            V='U'
            maxValue=cmds.getAttr(sel[nurb]+'.minMaxRangeV.maxValue'+U)
            Gett_Spans_Nurb=cmds.getAttr(sel[nurb]+'.spansV')          
        Distancia=1/float(Gett_Spans_Nurb)*maxValue
        Repeticiones=Distancia/2
        num=0
        XYZ=['X','Y','Z']
        XYZ_min=['x','y','z']
        for Loc in range(Gett_Spans_Nurb):
            Change_Name=sel[nurb].split('Rib_')[1]
            Locator_Create=cmds.spaceLocator(n='Loc_Rivet_'+(sel[nurb])+'_0'+str(num),a=True)[0]
            cmds.joint(Locator_Create,n='J_Bind_'+str(num)+'_'+Change_Name,rad=.4*Scale_Guide)
            cmds.parent(Locator_Create,('Locs_'+(sel[nurb])))
            Node_POS=cmds.shadingNode('pointOnSurfaceInfo',n='POS',au=True)
            SetPU=cmds.setAttr((Node_POS)+'.parameter'+(U),Repeticiones)
            SetPV=cmds.setAttr((Node_POS)+'.parameter'+(V),.5)
            Node_FBFM=cmds.shadingNode('fourByFourMatrix',n='FBFM',au=True)
            Node_DCM=cmds.shadingNode('decomposeMatrix',n='DCM',au=True)
            Num30=30
            Num0=0
            for xyz in XYZ:
                cmds.connectAttr((Node_POS)+'.position'+xyz,(Node_FBFM)+'.in'+str(Num30),f=True)
                cmds.connectAttr((Node_POS)+'.normal'+xyz,(Node_FBFM)+'.in0'+str(Num0),f=True)
                Num30=Num30+1
                Num0=Num0+1
            Num10=10
            Num20=20
            for xyz2 in XYZ_min:
                cmds.connectAttr((Node_POS)+'.tangentU'+xyz2,(Node_FBFM)+'.in'+str(Num10),f=True)
                cmds.connectAttr((Node_POS)+'.tangentV'+xyz2,(Node_FBFM)+'.in'+str(Num20),f=True)
                Num10=Num10+1
                Num20=Num20+1
            cmds.connectAttr((Node_FBFM)+'.output',(Node_DCM)+'.inputMatrix',f=True)
            cmds.connectAttr((sel[nurb])+'.worldSpace',(Node_POS)+'.inputSurface',f=True)
            cmds.connectAttr((Node_DCM)+'.outputRotate',(Locator_Create)+'.rotate',f=True)
            cmds.connectAttr((Node_DCM)+'.outputTranslate',(Locator_Create)+'.translate',f=True)
            Repeticiones=Repeticiones+Distancia
            num=num+1
            print Repeticiones   
    
    cmds.select(d=True)
    cmds.connectAttr('J_Arm_Neutral_R.scale','J_Bendy_2_Arm_R.scale')
    cmds.connectAttr('J_ForeArm_Neutral_R.scale','J_Bendy_2_ForeArm_R.scale')
    cmds.parentConstraint('J_ForeArm_Neutral_R','P_R_BendyMasterArm_CTL',mo=True)
    cmds.parentConstraint('J_ForeArm_Neutral_R','P_R_BendyForeArm_01_CTL',mo=True)
    cmds.parentConstraint('J_Hand_Neutral_R','P_R_BendyForeArm_03_CTL',mo=True)
    cmds.parentConstraint('J_Arm_Neutral_R','P_R_BendyArm_01_CTL',mo=True)
    List=['Arm','ForeArm']
    for J in List:
        cmds.orientConstraint('J_'+J+'_Neutral_R','P_R_Bendy'+J+'_02_CTL',mo=True)
        if J=='ForeArm':
            print 'no'
        else:
            cmds.orientConstraint('J_'+J+'_Neutral_R','P_R_Bendy'+J+'_03_CTL',mo=True)
    cmds.select(d=True)