import maya.cmds as cmds
import maya.mel as mel

def Arm_R():
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    #J_Clavicle_R#
    translate_Guide_Clavicle_R = cmds.xform ('Loc_Guide_Clavicle_R', ws=True, q=True, t=True)
    rot_Guide_Clavicle_R = cmds.xform ('Loc_Guide_Clavicle_R', ws=True, q=True, ro=True)
    J_Clavicle_R=cmds.joint(n=('J_Clavicle_R'),p=translate_Guide_Clavicle_R,rad=.7*Scale_Guide)
    cmds.mirrorJoint (myz=True, mb=True)
    cmds.delete('J_Clavicle_R')
    Rename_FK= mel.eval('searchReplaceNames("_R1","_R","all")')
    cmds.select(d=True)
    Z_J_Clavicle_R= cmds.group (n=("Z_J_Clavicle_R"),em=True)
    translate_J_Clavicle_R = cmds.xform ('J_Clavicle_R', ws=True, q=True, t=True)
    rot_J_Clavicle_R = cmds.xform ('J_Clavicle_R', ws=True, q=True, ro=True)
    emparentarTrans_J_Clavicle_R = cmds.xform (Z_J_Clavicle_R, ws=True, t=translate_J_Clavicle_R)
    emparentarRot_J_Clavicle_R = cmds.xform (Z_J_Clavicle_R, ws=True, ro=rot_J_Clavicle_R)
    cmds.parent(J_Clavicle_R,Z_J_Clavicle_R)
    cmds.select(d=True)
    #R_Clavicle_CTL#
    translate_Clavicle_R = cmds.xform ('J_Clavicle_R', ws=True, q=True, t=True)
    rot_Clavicle_R = cmds.xform ('J_Clavicle_R', ws=True, q=True, ro=True)
    emparentarTrans_Clavicle_R = cmds.xform ('P_R_Clavicle_CTL', ws=True, t=translate_Clavicle_R)
    emparentarRot_Clavicle_R = cmds.xform ('P_R_Clavicle_CTL', ws=True, ro=rot_Clavicle_R)
    cmds.parentConstraint ('R_Clavicle_CTL', 'J_Clavicle_R',mo=True)
    cmds.select(d=True)
    ##Joints Arm_R##
    #J_ARM_R#
    trans_Guide_Arm_R = cmds.xform ('Loc_Guide_Arm_R', ws=True, q=True, t=True)
    translate_Guide_ForeArm_R = cmds.xform ('Loc_Guide_ForeArm_R', ws=True, q=True, t=True)
    translate_Guide_Hand_R = cmds.xform ('Loc_Guide_Hand_R', ws=True, q=True, t=True)
    Joint_Arm_Neutral_R=cmds.joint(n='J_Arm_Neutral_R',p=trans_Guide_Arm_R,rad=1*Scale_Guide)
    Joint_ForeArm_Neutral_R=cmds.joint(n='J_ForeArm_Neutral_R',p=translate_Guide_ForeArm_R,rad=1*Scale_Guide)
    Joint_Hand_Neutral_R=cmds.joint(n='J_Hand_Neutral_R',p=translate_Guide_Hand_R,rad=1*Scale_Guide)
    OJ_Joint_Arm_Neutral_R=cmds.joint('J_Arm_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    OJ_Joint_ForeArm_Neutral_R=cmds.joint('J_ForeArm_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    OJ_Joint_Hand_Neutral_R=cmds.joint('J_Hand_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    joX_Hand_R=cmds.setAttr("J_Hand_Neutral_R.jointOrientX",0)
    joY_Hand_R=cmds.setAttr("J_Hand_Neutral_R.jointOrientY",0)
    joZ_Hand_R=cmds.setAttr("J_Hand_Neutral_R.jointOrientZ",0)
    cmds.select(Joint_Arm_Neutral_R)
    cmds.mirrorJoint (myz=True, mb=True)
    cmds.delete('J_Arm_Neutral_R')
    Rename_FK= mel.eval('searchReplaceNames("_R1","_R","all")')
    cmds.select(d=True)
    rot_J_Arm_Neutral_R = cmds.xform ('J_Arm_Neutral_R', ws=True, q=True, ro=True)
    trans_J_Arm_Neutral_R = cmds.xform ('J_Arm_Neutral_R', ws=True, q=True, t=True)
    Z_J_Arm=cmds.group(n='Z_J_Arm_Neutral_R',em=True)
    P_J_Arm=cmds.group(n='P_J_Arm_Neutral_R')
    emparentarTrans = cmds.xform ('P_J_Arm_Neutral_R', ws=True, t=trans_J_Arm_Neutral_R)
    emparentarRot = cmds.xform ('P_J_Arm_Neutral_R', ws=True, ro=rot_J_Arm_Neutral_R)
    P_J_Arm_Neutral_R_Z_J_Arm_Neutral_R=cmds.parent('J_Arm_Neutral_R','Z_J_Arm_Neutral_R')
    cmds.select(d=True )
    Activar_color= cmds.setAttr('P_J_Arm_Neutral_R.overrideEnabled', 1)
    Blanco= cmds.setAttr('P_J_Arm_Neutral_R.overrideColor', 16)
    #duplicate the originaR chain
    Duplicar_a_FK= cmds.duplicate(P_J_Arm, rc=True)
    Duplicar_a_IK= cmds.duplicate(P_J_Arm, rc=True)
    #rename the chain
    Rename_FK= mel.eval('searchReplaceNames("_Neutral_R1","_FK_R","all")')
    Rename_IK= mel.eval('searchReplaceNames("_Neutral_R2","_IK_R","all")')
    #Change color Herarchy FK_IK
    Activar_color= cmds.setAttr(('P_J_Arm_FK_R.overrideEnabled'), 1)
    Azul= cmds.setAttr('P_J_Arm_FK_R.overrideColor', 6)
    Activar_color= cmds.setAttr('P_J_Arm_IK_R.overrideEnabled', 1)
    Amarillo= cmds.setAttr('P_J_Arm_IK_R.overrideColor', 17)
    def J(Joints,nombre,radio):
        for Elemento in Joints:
            Change_Radius_Tip_FK= cmds.setAttr(Elemento+'_'+nombre+'_R'+'.radius',radio*Scale_Guide)
    J(['J_Arm','J_ForeArm','J_Hand'],"FK",.5)    
    J(['J_Arm','J_ForeArm','J_Hand'],"IK",.3)
    #########Create_Ctrls_FK_R#############
    #Create_Ctrl_Arm_FK_R
    translate = cmds.xform ('J_Arm_FK_R', ws=True, q=True, t=True)
    rot = cmds.xform ('J_Arm_FK_R', ws=True, q=True, ro=True)
    #Emparentar R_FK_Arm_CTL
    emparentarTrans_R = cmds.xform ('P_R_FK_Arm_CTL', ws=True, t=translate)
    emparentarRot_R = cmds.xform ('P_R_FK_Arm_CTL', ws=True, ro=rot)
    cmds.parentConstraint ('R_FK_Arm_CTL', 'J_Arm_FK_R',mo=True)
    #Create_Ctrl_ForeArm_FK_R
    translate = cmds.xform ('J_ForeArm_FK_R', ws=True, q=True, t=True)
    rot = cmds.xform ('J_ForeArm_FK_R', ws=True, q=True, ro=True)
    #Emparentar R_FK_Arm_CTL
    emparentarTrans_R = cmds.xform ('P_R_FK_ForeArm_CTL', ws=True, t=translate)
    emparentarRot_R = cmds.xform ('P_R_FK_ForeArm_CTL', ws=True, ro=rot)
    cmds.parentConstraint ('R_FK_ForeArm_CTL', 'J_ForeArm_FK_R',mo=True)
    #Create_Ctrl_Hand_FK_R
    translate = cmds.xform ('J_Hand_FK_R', ws=True, q=True, t=True)
    rot = cmds.xform ('J_Hand_FK_R', ws=True, q=True, ro=True)
    #Emparentar R_FK_Arm_CTL
    emparentarTrans_R = cmds.xform ('P_R_FK_Wrist_CTL', ws=True, t=translate)
    emparentarRot_R = cmds.xform ('P_R_FK_Wrist_CTL', ws=True, ro=rot)
    cmds.parentConstraint ('R_FK_Wrist_CTL', 'J_Hand_FK_R',mo=True)
    #Herarchy FK_Ctrls
    P_Hand_R_Ctrl_ForeArm_R= cmds.parent(("P_R_FK_Wrist_CTL","R_FK_ForeArm_CTL"))
    P_ForeArm_R_Ctrl_Arm_R= cmds.parent(("P_R_FK_ForeArm_CTL","R_FK_Arm_CTL"))
    #Create_IKHandle_Arm_R
    IK_Handle_Arm_R=cmds.ikHandle(n='Ik_Handle_arm_R', sj='J_Arm_IK_R', ee='J_Hand_IK_R')
    Hidde_IK_Handle_Arm_R=cmds.hide('Ik_Handle_arm_R')
    #Create_Ctrl_PV_ARM_R
    pos_Arm_IK_R = cmds.xform ('J_Arm_IK_R', ws=True, q=True, t=True)
    pos_ForeArm_IK_R = cmds.xform ('J_ForeArm_IK_R', ws=True, q=True, t=True)
    pos_Hand_IK_R = cmds.xform ('J_Hand_IK_R', ws=True, q=True, t=True)
    Cv_Polevector_Arm_R=cmds.curve(n='Cv_PV_Guide_Arm_R',d=1,p=[(pos_Arm_IK_R ),(pos_ForeArm_IK_R),(pos_Hand_IK_R)],k=(0,1,2))
    Move_Cv_Guide=cmds.moveVertexAlongDirection ('Cv_PV_Guide_Arm_R.cv[1]', n= 4.8*Scale_Guide)
    pos_Cv= cmds.pointPosition ('Cv_PV_Guide_Arm_R.cv[1]')
    emparentarTrans_R_PV_Arm_R = cmds.xform ('P_R_PolevectorArm_CTL', ws=True, t=pos_Cv)
    delete_Cv_Polevector_Arm_R=cmds.delete(Cv_Polevector_Arm_R)
    Cons_PV_Arm_R= cmds.poleVectorConstraint('R_PolevectorArm_CTL', 'Ik_Handle_arm_R' )
    #R_IK_Arm_CTL
    translate_Ctrl_IK_R = cmds.xform ('J_Hand_IK_R', ws=True, q=True, t=True)
    rot_Ctrl_IK_R = cmds.xform ('J_Hand_IK_R', ws=True, q=True, ro=True)   
    emparentarTrans_IK_Arm_R = cmds.xform ('P_R_IK_Arm_CTL', ws=True, t=translate_Ctrl_IK_R)
    emparentarRot_IK_Arm_R = cmds.xform ('P_R_IK_Arm_CTL', ws=True, ro=rot_Ctrl_IK_R)
    cmds.setAttr('P_R_IK_Arm_CTL.rotateX',0)
    #Herarchy_IkH_Ctrl_Arm_IK_R
    IkH_Arm_R_Ctrl_Arm_IK_R=cmds.parent('Ik_Handle_arm_R','R_IK_Arm_CTL')
    ##Herarchy_J_R
    Parent_J_Arm_Neutral_R_J_Clavicle_R= cmds.parent("P_J_Arm_Neutral_R","J_Clavicle_R")
    Parent_J_Arm_FK_R_J_Clavicle_R= cmds.parent("P_J_Arm_FK_R","J_Clavicle_R")
    Parent_J_Arm_IK_R_J_Clavicle_R= cmds.parent("P_J_Arm_IK_R","J_Clavicle_R")
    ##Herarchy_Ctrl_FK_Clavicle_R
    Parent_Ctrl_Arm_Neutral_R_Ctrl_Clavicle_R= cmds.parent("P_R_FK_Arm_CTL","R_Clavicle_CTL")
    #Create_Ctrl_Switch_ARM_R
    translate_Switch_ARM_R = cmds.xform ('Guide_Ctrl_Switch_Arm_R', ws=True, q=True, t=True)
    rot_Switch_ARM_R = cmds.xform ('Guide_Ctrl_Switch_Arm_R', ws=True, q=True, ro=True)
    emparentarTrans_R_Switch_ARM_R = cmds.xform ("P_R_SwitchArm_CTL", ws=True, t=translate_Switch_ARM_R)
    emparentarRot_R_Switch_ARM_R = cmds.xform ("P_R_SwitchArm_CTL", ws=True, ro=rot_Switch_ARM_R)
    #Add_Attrs_Switch_Arm_R
    Atributo_Switch= cmds.addAttr("R_SwitchArm_CTL",longName='Switch_FK_IK',attributeType='float', defaultValue=0, minValue=0, maxValue=10 )
    agregarAttr= cmds.setAttr ("R_SwitchArm_CTL.Switch_FK_IK", k=True)
    Atributo_Stretch= cmds.addAttr("R_SwitchArm_CTL",longName='Stretch',attributeType='float', defaultValue=1, minValue=0, maxValue=1)
    AgregarAttrStretch= cmds.setAttr ("R_SwitchArm_CTL.Stretch", k=True)
    #Switch_FK_IK_Arm_R
    Select_Arm=cmds.select('J_Arm_Neutral_R','J_ForeArm_Neutral_R','J_Hand_Neutral_R')
    sel = cmds.ls (sl=True)
    def Clear_Select():
        cmds.select (cl=True)
    Clear_Select()
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Arm_Switch_FK_IK_R")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('R_SwitchArm_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
    for J in sel:
        N = J.split("_Neutral_R")[0]
        print N
        New_N=N.split("J_")[1]
        BC_rotate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_rotate_R")
        BC_translate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_translate_R")
        cmds.connectAttr (BC_rotate + ".output", J + ".rotate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_rotate + ".blender")
        cmds.connectAttr (BC_translate + ".output", J + ".translate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_translate + ".blender")
    j_arm_neutral=('J_Arm_Neutral_R')
    j_forearm_neutral=('J_ForeArm_Neutral_R')
    jnt_hand_neutral_R=('J_Hand_Neutral_R')
    JN1 = j_arm_neutral.split("_Neutral_R")[0]
    JN2 = j_forearm_neutral.split("_Neutral_R")[0]
    JN3 = jnt_hand_neutral_R.split("_Neutral_R")[0]
    Milista=[]
    list.append(Milista,JN1)
    list.append(Milista,JN2)
    list.append(Milista,JN3)
    def fun1(Var1):    
        list.append (Milista, Milista[0] + Var1)
        list.append (Milista, Milista[1] + Var1)
        list.append (Milista, Milista[2] + Var1)
    fun1('_FK_R')
    fun1('_IK_R')
    def fun(Var):    
        cmds.connectAttr (Milista[3]+ "."+Var, "BC_Arm_"+Var+"_R.color2")
        cmds.connectAttr (Milista[6]+ "."+Var, "BC_Arm_"+Var+"_R.color1")
        cmds.connectAttr (Milista[4]+ "."+Var, "BC_ForeArm_"+Var+"_R.color2")
        cmds.connectAttr (Milista[7]+ "."+Var, "BC_ForeArm_"+Var+"_R.color1")
        cmds.connectAttr (Milista[5]+ "."+Var, "BC_Hand_"+Var+"_R.color2")
        cmds.connectAttr (Milista[8]+ "."+Var, "BC_Hand_"+Var+"_R.color1")
    fun('rotate')
    fun('translate')
    #Cons_Orient_Ik_Hand_J_Hand_R
    cmds.duplicate('J_Hand_IK_R',n='Eff_J_Hand_IK_R')
    cmds.move(Scale_Guide*(-2),0,0,'Eff_J_Hand_IK_R',r=True,os=True,wd=True)
    cmds.parent('Eff_J_Hand_IK_R','J_Hand_IK_R')
    cmds.ikHandle(n='IkHandle_Wrist_R',sj='J_Hand_IK_R',ee='Eff_J_Hand_IK_R',sol='ikSCsolver')
    cmds.parent('IkHandle_Wrist_R','R_IK_Arm_CTL')
    cmds.hide('IkHandle_Wrist_R')
    cmds.select(cl=True)
    Parent_Cons_FK_Ctrl_J_Ik_Arm=cmds.parentConstraint('R_FK_Arm_CTL','J_Arm_IK_R',mo=True)
    Herarchy_Switch_Arm_R_J_Hand_Neutral_R=cmds.parent('P_R_SwitchArm_CTL','J_Hand_Neutral_R')
    translate_J_ForeArm_Ik_R = cmds.xform ('J_ForeArm_IK_R', ws=True, q=True, t=True)
    translate_Ctrl_Polevector_Arm_R = cmds.xform ('R_PolevectorArm_CTL', ws=True, q=True, t=True)
    #CVPv_IK_R#
    Cv_Polevector_Arm_R=cmds.curve(n='Cv_Polevector_Arm_R',d=1,p=[(translate_J_ForeArm_Ik_R),(translate_Ctrl_Polevector_Arm_R)],k=(0,1))
    Z_Cvv_Polevector_Arm_R= cmds.group (n=("Z_Cv_Polevector_Arm_R"),em=True)
    Herarchy_CV_Grp=cmds.parent('Cv_Polevector_Arm_R',"Z_Cv_Polevector_Arm_R")
    lineWidth_Cv_Polevector_Arm_R=cmds.setAttr (Cv_Polevector_Arm_R+".lineWidth",2)
    OvE_Cv_Polevector_Arm_R=cmds.setAttr(Cv_Polevector_Arm_R+".overrideEnabled",1)
    OvDT_Cv_Polevector_Arm_R=cmds.setAttr(Cv_Polevector_Arm_R+".overrideDisplayType",2)
    cmds.select(d=True)
    J_CV_0_ARM_R=cmds.joint(p=translate_J_ForeArm_Ik_R,n="J_Cv_0_Arm_R")
    Grp_J_CV_0_ARM_R=cmds.group(n='Z_J_Cv_0_Arm_R')
    cmds.select(d=True)
    J_CV_1_ARM_R=cmds.joint(p=translate_Ctrl_Polevector_Arm_R,n="J_Cv_1_Arm_R")
    Grp_J_CV_1_ARM_R=cmds.group(n='Z_J_Cv_1_Arm_R')
    cmds.select(d=True)
    Skin_J_Cvs=cmds.skinCluster('J_Cv_0_Arm_R','J_Cv_1_Arm_R','Cv_Polevector_Arm_R',dr=4)
    Parent_J_CV_Arm_R_J_ForeArm_IK_R=cmds.parent(Grp_J_CV_0_ARM_R,'J_ForeArm_IK_R')
    Parent_J_CV_Arm_R_J_ForeArm_IK_R=cmds.parent(Grp_J_CV_1_ARM_R,'R_PolevectorArm_CTL')
    cmds.select(d=True)
    #Create Node_Vis_Arm_R#
    Node_Reverse_Vis_Arm_R=cmds.shadingNode('reverse',au=True, n='R_Vis_Arm_R')
    Node_MD_Vis_Arm_R=cmds.shadingNode('multiplyDivide',au=True, n='MD_Vis_Arm_R')
    Operation_MD_Vis_Arm_R= cmds.setAttr (Node_MD_Vis_Arm_R+'.operation',2, k=True)
    Set_2X_Node_MD_Vis_Arm_R= cmds.setAttr (Node_MD_Vis_Arm_R+'.input2X',10, k=True)
    #Conect Vis_Arm_R#
    Switch_MD_Arm_R=cmds.connectAttr('R_SwitchArm_CTL.Switch_FK_IK',Node_MD_Vis_Arm_R+'.input1X')
    MD_R_Arm_R=cmds.connectAttr(Node_MD_Vis_Arm_R+'.outputX',Node_Reverse_Vis_Arm_R+'.inputX')
    R_Ctrl_FK_Arm_R=cmds.connectAttr(Node_Reverse_Vis_Arm_R+'.outputX','P_R_FK_ForeArm_CTL.visibility')
    R_J_FK_Arm_R=cmds.connectAttr(Node_Reverse_Vis_Arm_R+'.outputX','P_J_Arm_FK_R.visibility')
    MD_Ctrl_IK_Arm_R=cmds.connectAttr(Node_MD_Vis_Arm_R+'.outputX','P_R_IK_Arm_CTL.visibility')
    MD_PV_IK_Arm_R=cmds.connectAttr(Node_MD_Vis_Arm_R+'.outputX','R_PolevectorArm_CTL.visibility')
    MD_CV_PV_IK_Arm_R=cmds.connectAttr(Node_MD_Vis_Arm_R+'.outputX','Z_Cv_Polevector_Arm_R.visibility')
    MD_J_IK_Arm_R=cmds.connectAttr(Node_MD_Vis_Arm_R+'.outputX','P_J_Arm_IK_R.visibility')