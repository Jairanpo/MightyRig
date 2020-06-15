import maya.cmds as cmds
import maya.mel as mel

def Leg_R():
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    ##Joints Leg_R##
    #J_Leg_R#
    trans_Guide_Leg_R = cmds.xform ('Loc_Guide_Leg_R', ws=True, q=True, t=True)
    translate_Guide_ForeLeg_R = cmds.xform ('Loc_Guide_ForeLeg_R', ws=True, q=True, t=True)
    translate_Guide_Foot_R = cmds.xform ('Loc_Guide_Foot_R', ws=True, q=True, t=True)
    Joint_Leg_Neutral_R=cmds.joint(n='J_Leg_Neutral_R',p=trans_Guide_Leg_R,rad=1*Scale_Guide)
    Joint_ForeLeg_Neutral_R=cmds.joint(n='J_ForeLeg_Neutral_R',p=translate_Guide_ForeLeg_R,rad=1*Scale_Guide)
    Joint_Ankle_Neutral_R=cmds.joint(n='J_Ankle_Neutral_R',p=translate_Guide_Foot_R,rad=1*Scale_Guide)
    OJ_Joint_Leg_Neutral_R=cmds.joint('J_Leg_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    OJ_Joint_ForeLeg_Neutral_R=cmds.joint('J_ForeLeg_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    OJ_Joint_Ankle_Neutral_R=cmds.joint('J_Ankle_Neutral_R', e=True, zso=True, oj='xzy',sao='zup')
    joX_Ankle_R=cmds.setAttr("J_Ankle_Neutral_R.jointOrientX",0)
    joY_Ankle_R=cmds.setAttr("J_Ankle_Neutral_R.jointOrientY",0)
    joZ_Ankle_R=cmds.setAttr("J_Ankle_Neutral_R.jointOrientZ",0)
    cmds.select(d=True)
    #J_Ankle_R#
    trans_Guide_Foot_R = cmds.xform ('Guide_Foot_R', ws=True, q=True, t=True)
    translate_Guide_Toe_R = cmds.xform ('Loc_Guide_Toe_R', ws=True, q=True, t=True)
    translate_Guide_Tip_R = cmds.xform ('Loc_Guide_Tip_R', ws=True, q=True, t=True)
    Joint_Toe_Neutral_R=cmds.joint(n='J_Toe_Neutral_R',p=translate_Guide_Toe_R,rad=1*Scale_Guide)
    Joint_Tip_Neutral_R=cmds.joint(n='J_Tip_Neutral_R',p=translate_Guide_Tip_R,rad=1*Scale_Guide)
    OJ_Joint_Leg_Neutral_R=cmds.joint('J_Toe_Neutral_R', e=True, zso=True, oj='xzy',sao='yup')
    OJ_Joint_ForeLeg_Neutral_R=cmds.joint('J_Tip_Neutral_R', e=True, zso=True, oj='xzy',sao='yup')
    rot_Ankle_R = cmds.xform ('J_Ankle_Neutral_R', ws=True, q=True, ro=True)
    cmds.select( d=True )
    cmds.parent('J_Toe_Neutral_R','J_Ankle_Neutral_R')
    cmds.select(d=True)
    cmds.select(Joint_Leg_Neutral_R)
    cmds.mirrorJoint (myz=True, mb=True)
    cmds.delete('J_Leg_Neutral_R')
    Rename_FK= mel.eval('searchReplaceNames("_R1","_R","all")')
    cmds.select(d=True)
    rot_Guide_Leg_R = cmds.xform ('J_Leg_Neutral_R', ws=True, q=True, ro=True)
    trans_Guide_Leg_R = cmds.xform ('J_Leg_Neutral_R', ws=True, q=True, t=True)
    Z_J_Leg=cmds.group(n='Z_J_Leg_Neutral_R',em=True)
    P_J_Leg=cmds.group(n='P_J_Leg_Neutral_R')
    emparentarTrans = cmds.xform ('P_J_Leg_Neutral_R', ws=True, t=trans_Guide_Leg_R)
    emparentarRot = cmds.xform ('P_J_Leg_Neutral_R', ws=True, ro=rot_Guide_Leg_R)
    P_J_Leg_Neutral_R_Z_J_Leg_Neutral_R=cmds.parent('J_Leg_Neutral_R','Z_J_Leg_Neutral_R')
    Activar_color= cmds.setAttr('P_J_Leg_Neutral_R.overrideEnabled', 1)
    Blanco= cmds.setAttr('P_J_Leg_Neutral_R.overrideColor', 16)
    cmds.select( d=True ) 
    #Duplicate the original chain
    Duplicar_a_FK= cmds.duplicate(P_J_Leg, rc=True)
    Duplicar_a_IK= cmds.duplicate(P_J_Leg, rc=True)
    #rename the chain
    Rename_FK= mel.eval('searchReplaceNames("_Neutral_R1","_FK_R","all")')
    Rename_IK= mel.eval('searchReplaceNames("_Neutral_R2","_IK_R","all")')
    #Change Color Herarchy FK_IK
    Activar_Color= cmds.setAttr(('P_J_Leg_FK_R.overrideEnabled'), 1)
    Azul= cmds.setAttr('P_J_Leg_FK_R.overrideColor', 6)
    Activar_Color= cmds.setAttr('P_J_Leg_IK_R.overrideEnabled', 1)
    Amarillo= cmds.setAttr('P_J_Leg_IK_R.overrideColor', 17)
    def J(Joints,nombre,radio):
        for Elemento in Joints:
            Change_Radius_Tip_FK= cmds.setAttr(Elemento+'_'+nombre+'_R'+'.radius',radio*Scale_Guide)
    J(['J_Leg','J_ForeLeg','J_Ankle','J_Toe','J_Tip'],"FK",.5)    
    J(['J_Leg','J_ForeLeg','J_Ankle','J_Toe','J_Tip'],"IK",.3)
    #########Create_Ctrls_FK_R#############
    #Create_Ctrl_Leg_FK_R
    translate = cmds.xform ('J_Leg_FK_R', ws=True, q=True, t=True)
    rot = cmds.xform ('J_Leg_FK_R', ws=True, q=True, ro=True)
    #Emparentar R_FK_Leg_CTL
    emparentarTrans_R = cmds.xform ('P_R_FK_Leg_CTL', ws=True, t=translate)
    emparentarRot_R = cmds.xform ('P_R_FK_Leg_CTL', ws=True, ro=rot)
    cmds.parentConstraint ('R_FK_Leg_CTL', 'J_Leg_FK_R',mo=True)
    #Create_Ctrl_ForeLeg_FK_R
    translate = cmds.xform ('J_ForeLeg_FK_R', ws=True, q=True, t=True)
    rot = cmds.xform ('J_ForeLeg_FK_R', ws=True, q=True, ro=True)
    #Emparentar R_FK_Leg_CTL
    emparentarTrans_R = cmds.xform ('P_R_FK_ForeLeg_CTL', ws=True, t=translate)
    emparentarRot_R = cmds.xform ('P_R_FK_ForeLeg_CTL', ws=True, ro=rot)
    cmds.parentConstraint ('R_FK_ForeLeg_CTL', 'J_ForeLeg_FK_R',mo=True)
    P_ForeLeg_R_Ctrl_Leg_R= cmds.parent(("P_R_FK_ForeLeg_CTL","R_FK_Leg_CTL"))
    #Create_IKAnklele_Leg_R
    Ik_Ankle_Leg_R=cmds.ikHandle(n='Ik_Ankle_Leg_R', sj='J_Leg_IK_R', ee='J_Ankle_IK_R')
    Hidde_Ik_Ankle_Leg_R=cmds.hide('Ik_Ankle_Leg_R')
    #Create_Ctrl_PV_Leg_R
    pos_Leg_IK_R = cmds.xform ('Guide_Leg_R', ws=True, q=True, t=True)
    pos_ForeLeg_IK_R = cmds.xform ('Guide_ForeLeg_R', ws=True, q=True, t=True)
    pos_Ankle_IK_R = cmds.xform ('Guide_Foot_R', ws=True, q=True, t=True)
    Cv_Polevector_Leg_R=cmds.curve(n='Cv_PV_Guide_Leg_R',d=1,p=[(pos_Leg_IK_R ),(pos_ForeLeg_IK_R),(pos_Ankle_IK_R)],k=(0,1,2))
    Move_Cv_Guide=cmds.moveVertexAlongDirection ('Cv_PV_Guide_Leg_R.cv[1]', n= 4.8*Scale_Guide)
    pos_Cv= cmds.pointPosition ('Cv_PV_Guide_Leg_R.cv[1]')
    emparentarTrans_R_PV_Leg_R = cmds.xform ('P_R_PolevectorLeg_CTL', ws=True, t=pos_Cv)
    delete_Cv_Polevector_Leg_R=cmds.delete(Cv_Polevector_Leg_R)
    Cons_PV_Leg_R= cmds.poleVectorConstraint('R_PolevectorLeg_CTL', 'Ik_Ankle_Leg_R' )
    #R_IK_Leg_CTL
    translate_Ctrl_IK_R = cmds.xform ('J_Ankle_IK_R', ws=True, q=True, t=True)
    emparentarTrans_IK_Leg_R = cmds.xform ('P_R_IK_Leg_CTL', ws=True, t=translate_Ctrl_IK_R)
    #Herarchy_IkH_Ctrl_Leg_IK_R
    IkH_Leg_R_Ctrl_Leg_IK_R=cmds.parent('Ik_Ankle_Leg_R','R_IK_Leg_CTL')
    #Create_Ctrl_Switch_Leg_R
    translate_Switch_Leg_R = cmds.xform ('Guide_Ctrl_Switch_Leg_R', ws=True, q=True, t=True)
    rot_Switch_Leg_R = cmds.xform ('Guide_Ctrl_Switch_Leg_R', ws=True, q=True, ro=True)
    emparentarTrans_R_Switch_Leg_R = cmds.xform ("P_R_SwitchLeg_CTL", ws=True, t=translate_Switch_Leg_R)
    emparentarRot_R_Switch_Leg_R = cmds.xform ("P_R_SwitchLeg_CTL", ws=True, ro=rot_Switch_Leg_R)
    #Add_Attrs_Switch_Leg_R
    Atributo_Switch= cmds.addAttr("R_SwitchLeg_CTL",longName='Switch_FK_IK',attributeType='float', defaultValue=10, minValue=0, maxValue=10 )
    agregarAttr= cmds.setAttr ("R_SwitchLeg_CTL.Switch_FK_IK", k=True)
    Atributo_Stretch= cmds.addAttr("R_SwitchLeg_CTL",longName='Stretch',attributeType='float', defaultValue=1, minValue=0, maxValue=1)
    AgregarAttrStretch= cmds.setAttr ("R_SwitchLeg_CTL.Stretch", k=True)
    #Switch_FK_IK_Leg_R
    Select_Leg=cmds.select('J_Leg_Neutral_R','J_ForeLeg_Neutral_R','J_Ankle_Neutral_R')
    sel = cmds.ls (sl=True)
    def Clear_Select():
        cmds.select (cl=True)
    Clear_Select()
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Leg_Switch_FK_IK_R")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('R_SwitchLeg_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
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
    j_Leg_neutral=('J_Leg_Neutral_R')
    j_foreLeg_neutral=('J_ForeLeg_Neutral_R')
    jnt_Ankle_neutral_R=('J_Ankle_Neutral_R')
    JN1 = j_Leg_neutral.split("_Neutral_R")[0]
    JN2 = j_foreLeg_neutral.split("_Neutral_R")[0]
    JN3 = jnt_Ankle_neutral_R.split("_Neutral_R")[0]
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
        cmds.connectAttr (Milista[3]+ "."+Var, "BC_Leg_"+Var+"_R.color2")
        cmds.connectAttr (Milista[6]+ "."+Var, "BC_Leg_"+Var+"_R.color1")
        cmds.connectAttr (Milista[4]+ "."+Var, "BC_ForeLeg_"+Var+"_R.color2")
        cmds.connectAttr (Milista[7]+ "."+Var, "BC_ForeLeg_"+Var+"_R.color1")
        cmds.connectAttr (Milista[5]+ "."+Var, "BC_Ankle_"+Var+"_R.color2")
        cmds.connectAttr (Milista[8]+ "."+Var, "BC_Ankle_"+Var+"_R.color1")
    fun('rotate')
    fun('translate')
    #Cons_Orient_Ik_Ankle_J_Ankle_R
    Parent_Cons_FK_Ctrl_J_Ik_Leg=cmds.parentConstraint('R_FK_Leg_CTL','J_Leg_IK_R',mo=True)
    Herarchy_Switch_Leg_R_J_Ankle_Neutral_R=cmds.parent('P_R_SwitchLeg_CTL','J_Ankle_Neutral_R')
    translate_J_ForeLeg_Ik_R = cmds.xform ('J_ForeLeg_IK_R', ws=True, q=True, t=True)
    translate_Ctrl_Polevector_Leg_R = cmds.xform ('R_PolevectorLeg_CTL', ws=True, q=True, t=True)
    #CVPv_IK_R#
    Cv_Polevector_Leg_R=cmds.curve(n='Cv_Polevector_Leg_R',d=1,p=[(translate_J_ForeLeg_Ik_R),(translate_Ctrl_Polevector_Leg_R)],k=(0,1))
    Z_Cvv_Polevector_Leg_R= cmds.group (n=("Z_Cv_Polevector_Leg_R"),em=True)
    Herarchy_CV_Grp=cmds.parent('Cv_Polevector_Leg_R',"Z_Cv_Polevector_Leg_R")
    lineWidth_Cv_Polevector_Leg_R=cmds.setAttr (Cv_Polevector_Leg_R+".lineWidth",2)
    OvE_Cv_Polevector_Leg_R=cmds.setAttr(Cv_Polevector_Leg_R+".overrideEnabled",1)
    OvDT_Cv_Polevector_Leg_R=cmds.setAttr(Cv_Polevector_Leg_R+".overrideDisplayType",2)
    cmds.select(d=True)
    J_CV_0_Leg_R=cmds.joint(p=translate_J_ForeLeg_Ik_R,n="J_Cv_0_Leg_R")
    Grp_J_CV_0_Leg_R=cmds.group(n='Z_J_Cv_0_Leg_R')
    cmds.select(d=True)
    J_CV_1_Leg_R=cmds.joint(p=translate_Ctrl_Polevector_Leg_R,n="J_Cv_1_Leg_R")
    Grp_J_CV_1_Leg_R=cmds.group(n='Z_J_Cv_1_Leg_R')
    cmds.select(d=True)
    Skin_J_Cvs=cmds.skinCluster('J_Cv_0_Leg_R','J_Cv_1_Leg_R','Cv_Polevector_Leg_R',dr=4)
    Parent_J_CV_Leg_R_J_ForeLeg_IK_R=cmds.parent(Grp_J_CV_0_Leg_R,'J_ForeLeg_IK_R')
    Parent_J_CV_Leg_R_J_ForeLeg_IK_R=cmds.parent(Grp_J_CV_1_Leg_R,'R_PolevectorLeg_CTL')
    cmds.select(d=True)
    #Create Node_Vis_Leg_R#
    Node_Reverse_Vis_Leg_R=cmds.shadingNode('reverse',au=True, n='R_Vis_Leg_R')
    Node_MD_Vis_Leg_R=cmds.shadingNode('multiplyDivide',au=True, n='MD_Vis_Leg_R')
    Operation_MD_Vis_Leg_R= cmds.setAttr (Node_MD_Vis_Leg_R+'.operation',2, k=True)
    Set_2X_Node_MD_Vis_Leg_R= cmds.setAttr (Node_MD_Vis_Leg_R+'.input2X',10, k=True)
    #Conect Vis_Leg_R#
    Switch_MD_Leg_R=cmds.connectAttr('R_SwitchLeg_CTL.Switch_FK_IK',Node_MD_Vis_Leg_R+'.input1X')
    MD_R_Leg_R=cmds.connectAttr(Node_MD_Vis_Leg_R+'.outputX',Node_Reverse_Vis_Leg_R+'.inputX')
    R_Ctrl_FK_Leg_R=cmds.connectAttr(Node_Reverse_Vis_Leg_R+'.outputX','P_R_FK_ForeLeg_CTL.visibility')
    R_J_FK_Leg_R=cmds.connectAttr(Node_Reverse_Vis_Leg_R+'.outputX','P_J_Leg_FK_R.visibility')
    MD_Ctrl_IK_Leg_R=cmds.connectAttr(Node_MD_Vis_Leg_R+'.outputX','P_R_IK_Leg_CTL.visibility')
    MD_PV_IK_Leg_R=cmds.connectAttr(Node_MD_Vis_Leg_R+'.outputX','R_PolevectorLeg_CTL.visibility')
    MD_CV_PV_IK_Leg_R=cmds.connectAttr(Node_MD_Vis_Leg_R+'.outputX','Z_Cv_Polevector_Leg_R.visibility')
    MD_J_IK_Leg_R=cmds.connectAttr(Node_MD_Vis_Leg_R+'.outputX','P_J_Leg_IK_R.visibility')