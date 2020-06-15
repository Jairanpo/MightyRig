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
def Foot_L():
    global translate,rot
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    Values_Trans_Guides_Arm=[]#LISTA VACIA QUE RECIBIRA LAS POSICIONES DE LAS GUIAS ARM
    List_Get_Trans=['Guide_Toe_L','Guide_Tip_L']
    num=0
    for Guide in List_Get_Trans:#FOR PARA OBTENER POSICION DE LAS GUIAS DEL ARM Y AGREGARLAS A LA LISTA VALUES_TRANS_GUIDES_ARM
        Get_Trans_Rot(Guide)
        list.append(Values_Trans_Guides_Arm,translate)
        num=num+1
    num=0
    for Joints_Create in Values_Trans_Guides_Arm:#CREACION DE LOS JOINTS EN BASE A LAS POSICIONES DE LAS GUIAS
        Name=['Toe','Tip']
        Joint_Neutral_L=cmds.joint(n='J_'+Name[num]+'_Neutral_L',p=Joints_Create,rad=1*Scale_Guide)
        num=num+1
    List_Joints=['J_Toe_Neutral_L','J_Tip_Neutral_L']#LISTA DE LOS JOINTS DEL ARM NEUTRALES
    for OJ in List_Joints:#FOR PARA ORIENTAR LA CADENA DE JOINTS ARM
        cmds.joint(OJ, e=True, zso=True, oj='xzy',sao='yup')
    XYZ=('X','Y','Z')
    for xyz in XYZ:#FOR PARA ASIGNAR JOINT ORIENT EN 0
        cmds.setAttr("J_Tip_Neutral_L.jointOrient"+xyz,0)
    cmds.select(cl=True)
    Get_Trans_Rot('J_Toe_Neutral_L') 
    Z_J_Toe=cmds.group(n='Z_J_Toe_Neutral_L',em=True)#CREACION GRUPO Z_OFFSET TOE_NEUTRAL_L
    Set_Trans_Rot('Z_J_Toe_Neutral_L')
    cmds.parent('J_Toe_Neutral_L','Z_J_Toe_Neutral_L')
    cmds.select(cl=True )
    cmds.setAttr('Z_J_Toe_Neutral_L.overrideEnabled', 1)
    cmds.setAttr('Z_J_Toe_Neutral_L.overrideColor', 16)
    cmds.duplicate(Z_J_Toe, rc=True)#DUPLICAR CADENA P_J_TOE
    cmds.duplicate(Z_J_Toe, rc=True)#DUPLICAR CADENA P_J_TOE
    Rename_FK= mel.eval('searchReplaceNames("_Neutral_L1","_FK_L","all")')#RENOMBRAR CADENA NEUTRAL A FK
    Rename_IK= mel.eval('searchReplaceNames("_Neutral_L2","_IK_L","all")')#RENOMBRAR CADENA NEUTRAL A IK
    cmds.setAttr(('Z_J_Toe_FK_L.overrideEnabled'), 1)
    cmds.setAttr('Z_J_Toe_FK_L.overrideColor', 6)
    cmds.setAttr('Z_J_Toe_IK_L.overrideEnabled', 1)
    cmds.setAttr('Z_J_Toe_IK_L.overrideColor', 17)
    def J(Joints,nombre,radio):#FUNCION PARA CAMBIAR RADIO DE CADENAS FK,IK Y NEUTRAL
        for Elemento in Joints:
            Change_Radius_Tip_FK= cmds.setAttr(Elemento+'_'+nombre+'_L'+'.radius',radio*Scale_Guide)
    J(['J_Toe','J_Tip',],"FK",.5)    
    J(['J_Toe','J_Tip',],"IK",.3)
    def Jnts_Ctrls(J,P_Ctrl,Ctrl):#FUNCION PARA EMPARENTAR Y HACER CONSTRAINT A LOS JOINTS FK DEL TOE
            Get_Trans_Rot(J)
            Set_Trans_Rot(P_Ctrl)
            cmds.parentConstraint(Ctrl,J,mo=True)
    Jnts_Ctrls('J_Ankle_FK_L','P_L_FK_Ankle_CTL','L_FK_Ankle_CTL')
    Jnts_Ctrls('J_Toe_FK_L','P_L_FK_Toe_CTL','L_FK_Toe_CTL')
    cmds.parent('P_L_FK_Toe_CTL','L_FK_Ankle_CTL')
    cmds.select(cl=True)
    Sistemas=['FK','IK','Neutral']
    for Sistema in Sistemas:#FOR PARA JERARQUIZAR LOS SISTEMAS FK,IK,NEUTRAL A ANKLE
        cmds.parent('Z_J_Toe_'+Sistema+'_L','J_Ankle_'+Sistema+'_L')
    cmds.select(cl=True)
    Attrs_ReverseFoot=['FootRoll','Banking','Tip','Heel_Swivel','Ball_Swivel']
    for Name_Attr in Attrs_ReverseFoot:
        cmds.addAttr('L_IK_Leg_CTL',longName=Name_Attr,attributeType='float', defaultValue=0, minValue=-10, maxValue=10 )
        cmds.setAttr ('L_IK_Leg_CTL' + '.'+Name_Attr, k=True)
    List_Guides_Grps=['Guide_BallPivot_L','Guide_Heel_L','Guide_BankOut_L','Guide_BankIn_L','Guide_Tip_Reverse_Foot_L','Guide_Toe_L','Guide_Foot_L']#LISTA DE GUIAS DE FOOTROLL
    num=0
    Name=['BallPivot','Heel','BankOut','BankIn','Tip','FootRoll','Ankle']#LISTA DE NOMBRES PARA LOS ATTRS
    for Grps_Create in List_Guides_Grps:#CREACION DE LOS GRPS EN BASE A LAS POSICIONES DE LAS GUIAS
        cmds.group(p=Grps_Create,n='Z_'+Name[num]+'_L',em=True)
        Z_Group= cmds.group(n='P_'+Name[num]+'_L')
        cmds.parent(Z_Group,w=True)
        num=num+1
    cmds.select(cl=True)
    Father=0
    Children=1
    List_6=['','','','','','']
    for grps in List_6:#FOR PARA JERARQUIZAR LOS GRUPOS DEL REVERSE FOOT
        cmds.parent('P_'+Name[Children]+'_L','Z_'+Name[Father]+'_L')
        Father=Father+1
        Children=Children+1
    cmds.select(cl=True)
    cmds.ikHandle( sj='J_Ankle_IK_L', ee='J_Toe_IK_L',sol='ikSCsolver', p=1, w=1,n='IkHandle_Toe_L')
    cmds.ikHandle( sj='J_Toe_IK_L', ee='J_Tip_IK_L',sol='ikSCsolver', p=1, w=1,n='IkHandle_Tip_L')
    cmds.select(cl=True)
    cmds.parent('IkHandle_Toe_L','Z_FootRoll_L')
    cmds.parent('IkHandle_Tip_L','Z_Tip_L')
    cmds.hide('IkHandle_Tip_L')
    cmds.hide('IkHandle_Toe_L')
    cmds.parent('P_BallPivot_L','L_IK_Leg_CTL')
    cmds.parent('Ik_Ankle_Leg_L','Z_Ankle_L')
    cmds.select(cl=True)
    def SDK(Attr,Grp_Rotate,Value_Rot,Value_Attr):#FUNCION PARA CREAR LOS SDK DE LOS ATTRS
        cmds.setAttr('L_IK_Leg_CTL' + Attr,0)
        cmds.setAttr(Grp_Rotate,0)
        cmds.setDrivenKeyframe (Grp_Rotate, cd=('L_IK_Leg_CTL' + Attr))
        cmds.setAttr('L_IK_Leg_CTL'+Attr,Value_Attr)
        cmds.setAttr(Grp_Rotate,Value_Rot)
        cmds.setDrivenKeyframe (Grp_Rotate, cd=('L_IK_Leg_CTL'+Attr))
        cmds.setAttr('L_IK_Leg_CTL'+Attr,0)
    SDK('.FootRoll','Z_FootRoll_L.rotateX',90,10)
    SDK('.FootRoll','Z_Heel_L.rotateX',-50,-10)
    SDK('.Banking','Z_BankOut_L.rotateZ',-50,10)
    SDK('.Banking','Z_BankIn_L.rotateZ',50,-10)
    SDK('.Tip','Z_Tip_L.rotateX',90,10)
    SDK('.Tip','Z_Tip_L.rotateX',-40,-10)
    SDK('.Heel_Swivel','Z_Heel_L.rotateY',50,10)
    SDK('.Heel_Swivel','Z_Heel_L.rotateY',-50,-10)
    SDK('.Ball_Swivel','Z_BallPivot_L.rotateY',50,10)
    SDK('.Ball_Swivel','Z_BallPivot_L.rotateY',-50,-10)
    Select_Ankle=cmds.select('J_Toe_Neutral_L','J_Tip_Neutral_L')
    sel = cmds.ls (sl=True)
    def Clear_Select():#FUNCION PARA LIMPIAR SELECCION
        cmds.select (cl=True)
    Clear_Select()
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Ankle_Switch_FK_IK_L")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('L_SwitchLeg_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
    for J in sel:#FOR PARA EL SWITCH
        N = J.split("_Neutral_L")[0]
        print N
        New_N=N.split("J_")[1]
        BC_rotate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_rotate_L")
        BC_translate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_translate_L")
        cmds.connectAttr (BC_rotate + ".output", J + ".rotate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_rotate + ".blender")
        cmds.connectAttr (BC_translate + ".output", J + ".translate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_translate + ".blender")
    j_Ankle_neutral=('J_Ankle_Neutral_L')
    j_Toe_neutral=('J_Toe_Neutral_L')
    jnt_Tip_neutral_l=('J_Tip_Neutral_L')
    JN1 = j_Ankle_neutral.split("_Neutral_L")[0]
    JN2 = j_Toe_neutral.split("_Neutral_L")[0]
    JN3 = jnt_Tip_neutral_l.split("_Neutral_L")[0]
    Milista=[]
    list.append(Milista,JN1)
    list.append(Milista,JN2)
    list.append(Milista,JN3)
    def fun1(Var1):    
        list.append (Milista, Milista[0] + Var1)
        list.append (Milista, Milista[1] + Var1)
        list.append (Milista, Milista[2] + Var1)
    fun1('_FK_L')
    fun1('_IK_L')
    def fun(Var):
        cmds.connectAttr (Milista[4]+ "."+Var, "BC_Toe_"+Var+"_L.color2")
        cmds.connectAttr (Milista[7]+ "."+Var, "BC_Toe_"+Var+"_L.color1")
        cmds.connectAttr (Milista[5]+ "."+Var, "BC_Tip_"+Var+"_L.color2")
        cmds.connectAttr (Milista[8]+ "."+Var, "BC_Tip_"+Var+"_L.color1")
    fun('rotate')
    fun('translate')