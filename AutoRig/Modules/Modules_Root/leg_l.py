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
def Leg_L():
    global translate,rot
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    Values_Trans_Guides_Leg=[]#LISTA VACIA QUE RECIBIRA LAS POSICIONES DE LAS GUIAS Leg
    List_Get_Trans=['Guide_Leg_L','Guide_ForeLeg_L','Guide_Foot_L']
    num=0
    for Guide in List_Get_Trans:#FOR PARA OBTENER POSICION DE LAS GUIAS DEL Leg Y AGREGARLAS A LA LISTA VALUES_TRANS_GUIDES_Leg
        Get_Trans_Rot(Guide)
        list.append(Values_Trans_Guides_Leg,translate)
        num=num+1
    num=0
    for Joints_Create in Values_Trans_Guides_Leg:#CREACION DE LOS JOINTS EN BASE A LAS POSICIONES DE LAS GUIAS
        Name=['Leg','ForeLeg','Ankle']
        Joint_Neutral_L=cmds.joint(n='J_'+Name[num]+'_Neutral_L',p=Joints_Create,rad=1*Scale_Guide)
        num=num+1
    List_Joints=['J_Leg_Neutral_L','J_ForeLeg_Neutral_L','J_Ankle_Neutral_L']#LISTA DE LOS JOINTS DEL Leg NEUTRALES
    for OJ in List_Joints:#FOR PARA ORIENTAR LA CADENA DE JOINTS Leg
        cmds.joint(OJ, e=True, zso=True, oj='xzy',sao='zup')
    XYZ=('X','Y','Z')
    for xyz in XYZ:#FOR PARA ASIGNAR JOINT ORIENT EN 0
        cmds.setAttr("J_Ankle_Neutral_L.jointOrient"+xyz,0)
    cmds.select(cl=True )
    Get_Trans_Rot('J_Leg_Neutral_L')
    cmds.group(n='Z_J_Leg_Neutral_L',em=True)#CREACION GRUPO Z_OFFSET Leg_NEUTRAL_L
    P_J_Leg=cmds.group(n='P_J_Leg_Neutral_L')#CREACION GRUPO P_OFFSET Leg_NEUTRAL_L
    Set_Trans_Rot('P_J_Leg_Neutral_L')
    cmds.parent('J_Leg_Neutral_L','Z_J_Leg_Neutral_L')
    cmds.select(cl=True )
    cmds.setAttr('P_J_Leg_Neutral_L.overrideEnabled', 1)
    cmds.setAttr('P_J_Leg_Neutral_L.overrideColor', 16)
    cmds.duplicate(P_J_Leg, rc=True)#DUPLICAR CADENA P_J_Leg
    cmds.duplicate(P_J_Leg, rc=True)#DUPLICAR CADENA P_J_Leg
    Rename_FK= mel.eval('searchReplaceNames("_Neutral_L1","_FK_L","all")')#RENOMBRAR CADENA NEUTRAL A FK
    Rename_IK= mel.eval('searchReplaceNames("_Neutral_L2","_IK_L","all")')#RENOMBRAR CADENA NEUTRAL A IK
    cmds.setAttr(('P_J_Leg_FK_L.overrideEnabled'), 1)
    cmds.setAttr('P_J_Leg_FK_L.overrideColor', 6)
    cmds.setAttr('P_J_Leg_IK_L.overrideEnabled', 1)
    cmds.setAttr('P_J_Leg_IK_L.overrideColor', 17)
    def J(Joints,nombre,radio):#FUNCION PARA CAMBIAR RADIO DE CADENAS FK,IK Y NEUTRAL
        for Elemento in Joints:
            Change_Radius_Tip_FK= cmds.setAttr(Elemento+'_'+nombre+'_L'+'.radius',radio*Scale_Guide)
    J(['J_Leg','J_ForeLeg','J_Ankle'],"FK",.5)    
    J(['J_Leg','J_ForeLeg','J_Ankle'],"IK",.3)
    def Jnts_Ctrls(J,P_Ctrl,Ctrl):#FUNCION PARA EMPARENTAR Y HACER CONSTRAINT A LOS JOINTS FK DEL Leg
            Get_Trans_Rot(J)
            Set_Trans_Rot(P_Ctrl)
            cmds.parentConstraint(Ctrl,J,mo=True)
    Jnts_Ctrls('J_Leg_FK_L','P_L_FK_Leg_CTL','L_FK_Leg_CTL')
    Jnts_Ctrls('J_ForeLeg_FK_L','P_L_FK_ForeLeg_CTL','L_FK_ForeLeg_CTL')
    Jnts_Ctrls('J_Ankle_FK_L','P_L_FK_Ankle_CTL','L_FK_Ankle_CTL')
    cmds.parent(("P_L_FK_Ankle_CTL","L_FK_ForeLeg_CTL"))
    cmds.parent(("P_L_FK_ForeLeg_CTL","L_FK_Leg_CTL"))
    cmds.ikHandle(n='Ik_Ankle_Leg_L', sj='J_Leg_IK_L', ee='J_Ankle_IK_L')#CREAR IK AnkleLE Leg_L
    cmds.hide('Ik_Ankle_Leg_L')
    Get_Trans_Rot('J_Ankle_IK_L')
    cmds.xform ('P_L_IK_Leg_CTL', ws=True, t=translate)
    cmds.parent('Ik_Ankle_Leg_L','L_IK_Leg_CTL')
    #CREAR CURVA PARA POSICION DEL POLEVECTOR
    Cv_Polevector_Leg_L=cmds.curve(n='Cv_PV_Guide_Leg_L',d=1,p=[(Values_Trans_Guides_Leg[0]),(Values_Trans_Guides_Leg[1]),(Values_Trans_Guides_Leg[2])],k=(0,1,2))
    cmds.moveVertexAlongDirection ('Cv_PV_Guide_Leg_L.cv[1]', n= 4.8*Scale_Guide)
    pos_Cv= cmds.pointPosition ('Cv_PV_Guide_Leg_L.cv[1]')
    cmds.xform ('P_L_PolevectorLeg_CTL', ws=True, t=pos_Cv)
    cmds.delete(Cv_Polevector_Leg_L)
    Cons_PV_Leg_L= cmds.poleVectorConstraint( 'L_PolevectorLeg_CTL', 'Ik_Ankle_Leg_L' )
    cmds.select(cl=True)
    Get_Trans_Rot('Guide_Ctrl_Switch_Leg_L')
    Set_Trans_Rot('P_L_SwitchLeg_CTL')
    Attributes=['Switch_FK_IK','Stretch']#LISTA DE ATTRS PARA EL SWITCH
    for Attr in Attributes:#FOR PARA AGREGAR ATRIBUTOS AL SWITCH
        if Attr is 'Stretch':
            Atributo_Switch= cmds.addAttr("L_SwitchLeg_CTL",longName=Attr,attributeType='float', defaultValue=1, minValue=0, maxValue=1 )
            agregarAttr= cmds.setAttr ("L_SwitchLeg_CTL."+Attr, k=True)
        else:
            Atributo_Switch= cmds.addAttr("L_SwitchLeg_CTL",longName=Attr,attributeType='float', defaultValue=10, minValue=0, maxValue=10 )
            agregarAttr= cmds.setAttr ("L_SwitchLeg_CTL."+Attr, k=True)
    #Switch_FK_IK_Leg_L
    Select_Leg=cmds.select('J_Leg_Neutral_L','J_ForeLeg_Neutral_L','J_Ankle_Neutral_L')
    sel = cmds.ls (sl=True)
    cmds.select (cl=True)
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Leg_Switch_FK_IK_L")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('L_SwitchLeg_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
    Milista=[]#LISTA VACIA QUE RECIBIRA LOS NOMBRES _NEUTRAL_L
    for J in sel:#FOR PARA EN BASE A LA SELECCION(JOINTS) SE CREAN BLENDCOLORS Y SE CONECTE EL MULTIPLYDIVIDE A LOS BLENDS
        N = J.split("_Neutral_L")[0]
        New_N=N.split("J_")[1]
        BC_rotate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_rotate_L")
        BC_translate = cmds.shadingNode ("blendColors", asUtility=True, n="BC_" + New_N+"_translate_L")
        cmds.connectAttr (BC_rotate + ".output", J + ".rotate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_rotate + ".blender")
        cmds.connectAttr (BC_translate + ".output", J + ".translate")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_translate + ".blender")
        list.append(Milista,N)#AGREGA EL NOMBRE DEL JOINT SIN NOMBRE DEL SISTEMA A LA LISTA Milista
    def fun1(Var1):#FUNCION PARA AGREGAR STRING A LOS NOMBRES QUE EXISTEN EN Milista
        list.append (Milista, Milista[0] + Var1)
        list.append (Milista, Milista[1] + Var1)
        list.append (Milista, Milista[2] + Var1)
    fun1('_FK_L')
    fun1('_IK_L')
    def fun(Var):#FUNCION PARA CONECTAR LOS JOINTS FK,IK A LOS BLEND COLORS 
        cmds.connectAttr (Milista[3]+ "."+Var, "BC_Leg_"+Var+"_L.color2")
        cmds.connectAttr (Milista[6]+ "."+Var, "BC_Leg_"+Var+"_L.color1")
        cmds.connectAttr (Milista[4]+ "."+Var, "BC_ForeLeg_"+Var+"_L.color2")
        cmds.connectAttr (Milista[7]+ "."+Var, "BC_ForeLeg_"+Var+"_L.color1")
        cmds.connectAttr (Milista[5]+ "."+Var, "BC_Ankle_"+Var+"_L.color2")
        cmds.connectAttr (Milista[8]+ "."+Var, "BC_Ankle_"+Var+"_L.color1")
    fun('rotate')
    fun('translate')
    cmds.parentConstraint('L_FK_Leg_CTL','J_Leg_IK_L',mo=True)
    cmds.parent('P_L_SwitchLeg_CTL','J_Ankle_Neutral_L')
    Get_Trans_Rot('J_ForeLeg_IK_L')
    translate_J_ForeLeg_Ik_L=translate
    Get_Trans_Rot('L_PolevectorLeg_CTL')
    translate_Ctrl_PoleVector_Leg_L=translate
    #CREAR CV PARA POLEVECTOR
    Cv_Polevector_Leg_L=cmds.curve(n='Cv_Polevector_Leg_L',d=1,p=[(translate_J_ForeLeg_Ik_L),(translate_Ctrl_PoleVector_Leg_L)],k=(0,1))
    cmds.group (n=("Z_Cv_Polevector_Leg_L"),em=True)
    cmds.parent('Cv_Polevector_Leg_L',"Z_Cv_Polevector_Leg_L")
    cmds.setAttr (Cv_Polevector_Leg_L+".lineWidth",2)
    cmds.setAttr(Cv_Polevector_Leg_L+".overrideEnabled",1)
    cmds.setAttr(Cv_Polevector_Leg_L+".overrideDisplayType",2)
    cmds.select(cl=True)
    J_CV_0_Leg_L=cmds.joint(p=translate_J_ForeLeg_Ik_L,n="J_Cv_0_Leg_L")
    cmds.select(cl=True)
    J_CV_1_Leg_L=cmds.joint(p=translate_Ctrl_PoleVector_Leg_L,n="J_Cv_1_Leg_L")
    Grp_J_CV_1_Leg_L=cmds.group(n='Z_J_Cv_1_Leg_L')
    cmds.select(cl=True)
    cmds.skinCluster('J_Cv_0_Leg_L','J_Cv_1_Leg_L','Cv_Polevector_Leg_L',dr=4)
    cmds.parent(J_CV_0_Leg_L,'J_ForeLeg_IK_L')
    cmds.parent(Grp_J_CV_1_Leg_L,'L_PolevectorLeg_CTL')
    cmds.select(cl=True)
    #Create and Connect Nodes_Vis_Leg_L#
    Node_Reverse_Vis_Leg_L=cmds.shadingNode('reverse',au=True, n='R_Vis_Leg_L')
    Node_MD_Vis_Leg_L=cmds.shadingNode('multiplyDivide',au=True, n='MD_Vis_Leg_L')
    cmds.setAttr (Node_MD_Vis_Leg_L+'.operation',2, k=True)
    cmds.setAttr (Node_MD_Vis_Leg_L+'.input2X',10, k=True)
    Nodes_Vis=['R_Vis_Leg_L','MD_Vis_Leg_L']
    cmds.connectAttr('L_SwitchLeg_CTL.Switch_FK_IK',Node_MD_Vis_Leg_L+'.input1X')
    cmds.connectAttr(Nodes_Vis[1]+'.outputX',Nodes_Vis[0]+'.inputX')
    #CONECTAR REVERSE_VISIBILITY A LA VISIBILIDAD FK
    cmds.connectAttr(Nodes_Vis[0]+'.outputX','P_L_FK_ForeLeg_CTL.visibility')
    cmds.connectAttr(Nodes_Vis[0]+'.outputX','P_J_Leg_FK_L.visibility')
    Names=['P_L_IK_Leg_CTL','P_L_PolevectorLeg_CTL','Z_Cv_Polevector_Leg_L','P_J_Leg_IK_L']#LISTA DE STRINGS IKS
    for Object in Names:#FOR PARA CONECTAR EL MULTIPLYDIVIDE A LA VISIBILIDAD IK
        cmds.connectAttr(Nodes_Vis[1]+'.outputX',Object+'.visibility')
    cmds.select(cl=True)