import maya.cmds as cmds
import maya.mel as mel
def Get_Trans_Rot(Name):#OBTENER TRASLACION Y ROTACION DE UN OBJETO
    global translate,rot
    translate = cmds.xform (Name, ws=True, q=True, t=True)
    rot = cmds.xform (Name, ws=True, q=True, ro=True)
def Set_Trans_Rot(Name):#INSERTAR TRASLACION Y ROTACION A UN OBJETO
    global Parent_Trans,Parent_Rot
    Parent_Trans = cmds.xform (Name, ws=True, t=translate)
    Parent_Rot = cmds.xform (Name, ws=True, ro=rot)
def stretch_Leg_r():
    Gett_TranslateX_ForeLeg_R=cmds.getAttr("J_ForeLeg_Neutral_R.translateX")
    Gett_TranslateX_Ankle_Neutral_R=cmds.getAttr("J_Ankle_Neutral_R.translateX")
    Sum_ForeLeg_Ankle_Trans=Gett_TranslateX_ForeLeg_R+Gett_TranslateX_Ankle_Neutral_R
    DD_Leg_R=cmds.distanceDimension(sp=(0, 0, 0), ep=(1, 0, 0) )    #Create DD_Leg_R#
    cmds.rename('locator1','Ini_Stretch_Leg_R')
    cmds.rename('locator2','End_Stretch_Leg_R')
    Rename_DD_Leg_R=cmds.rename('distanceDimension1','distanceDimension_Stretch_Master_Leg_R')
    cmds.select(cl=True)
    cmds.select('Ini_Stretch_Leg_R')
    Z_Ini_Stretch_Leg_R=cmds.group(n='Z_Ini_Stretch_Leg_R')
    cmds.select(cl=True)
    Get_Trans_Rot('End_Stretch_Leg_R')
    Z_End_Stretch_Leg_R=cmds.group(n='Z_End_Stretch_Leg_R',em=True)
    Set_Trans_Rot(Z_End_Stretch_Leg_R)
    cmds.parent('End_Stretch_Leg_R',Z_End_Stretch_Leg_R)
    cmds.select(cl=True)
    Get_Trans_Rot('J_Leg_Neutral_R')
    Set_Trans_Rot(Z_Ini_Stretch_Leg_R)
    Get_Trans_Rot('J_Ankle_Neutral_R')
    Set_Trans_Rot(Z_End_Stretch_Leg_R)
    cmds.parent(Z_End_Stretch_Leg_R,'R_IK_Leg_CTL')
    cmds.parent(Z_Ini_Stretch_Leg_R,'R_FK_Leg_CTL')
    cmds.select(cl=True)
    Gett_Distance_Stretch_Leg_R=cmds.getAttr('distanceDimension_Stretch_Master_Leg_R.distance')
    Names_Nodes=['MD_Stretch_Leg_R','BC_Stretch_Leg_R','C_Stretch_Leg_R']
    Nodes=['multiplyDivide','blendColors','condition']
    num=0
    for Node in Names_Nodes:
        Create_Note=cmds.shadingNode(Nodes[num],au=True,n=Node)
        cmds.select(cl=True)
        num=num+1
    cmds.setAttr ('MD_Stretch_Leg_R.operation',2, k=True)
    cmds.setAttr ('MD_Stretch_Leg_R.input2X',-Sum_ForeLeg_Ankle_Trans, k=True)
    cmds.setAttr ('BC_Stretch_Leg_R.color2R',1)
    cmds.setAttr ('C_Stretch_Leg_R.operation',2, k=True)
    cmds.setAttr ('C_Stretch_Leg_R.secondTerm',-Sum_ForeLeg_Ankle_Trans, k=True)    
    def Connect(Name,Name2,Attr1,Attr2):
        cmds.connectAttr(Name+Attr1,Name2+Attr2) 
    Connect('distanceDimension_Stretch_Master_Leg_R','MD_Stretch_Leg_R','.distance','.input1X')
    Connect('R_SwitchLeg_CTL','BC_Stretch_Leg_R','.Stretch','.blender')
    Connect('MD_Stretch_Leg_R','BC_Stretch_Leg_R','.outputX','.color1R')
    Connect('BC_Stretch_Leg_R','C_Stretch_Leg_R','.outputR','.colorIfTrueR')
    Connect('distanceDimension_Stretch_Master_Leg_R','C_Stretch_Leg_R','.distance','.firstTerm')
    Connect('C_Stretch_Leg_R','J_Leg_IK_R','.outColorR','.scaleX')   
    Connect('C_Stretch_Leg_R','J_ForeLeg_IK_R','.outColorR','.scaleX') 
    Select_Leg=cmds.select('J_Leg_Neutral_R','J_ForeLeg_Neutral_R')#Switch_FK_IK_Leg_R
    sel = cmds.ls (sl=True)
    cmds.select (cl=True)
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Leg_Stretch_FK_IK_R")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('R_SwitchLeg_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
    Milista=[]#LISTA VACIA QUE RECIBIRA LOS NOMBRES _NEUTRAR_R
    for J in sel:#FOR PARA EN BASE A LA SELECCION(JOINTS) SE CREAN BLENDCOLORS Y SE CONECTE EL MULTIPLYDIVIDE A LOS BLENDS
        N = J.split("_Neutral_R")[0]
        New_N=N.split("J_")[1]
        BC_rotate = cmds.shadingNode ("blendColors", asUtility=True, n="BS_" + New_N+"_stretch_R")
        cmds.select (cl=True)
        cmds.connectAttr (BC_rotate + ".output", J + ".scale")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_rotate + ".blender")
        list.append(Milista,N)#AGREGA EL NOMBRE DEL JOINT SIN NOMBRE DEL SISTEMA A LA LISTA Milista
    def fun1(Var1):#FUNCION PARA AGREGAR STRING A LOS NOMBRES QUE EXISTEN EN Milista
        list.append (Milista, Milista[0] + Var1)
        list.append (Milista, Milista[1] + Var1)
    fun1('_FK_R')
    fun1('_IK_R')
    def fun(Var,Var2):#FUNCION PARA CONECTAR LOS JOINTS FK,IK A LOS BLEND COLORS 
        cmds.connectAttr (Milista[2]+ "."+Var, "BS_Leg_"+Var2+"_R.color2")
        cmds.connectAttr (Milista[4]+ "."+Var, "BS_Leg_"+Var2+"_R.color1")
        cmds.connectAttr (Milista[3]+ "."+Var, "BS_ForeLeg_"+Var2+"_R.color2")
        cmds.connectAttr (Milista[5]+ "."+Var, "BS_ForeLeg_"+Var2+"_R.color1")
    fun('scale','stretch')
    cmds.parent('distanceDimension_Stretch_Master_Leg_R','hidden')
    cmds.hide('distanceDimension_Stretch_Master_Leg_R')
    cmds.hide('Ini_Stretch_Leg_R')
    cmds.hide('End_Stretch_Leg_R')
    cmds.select(cl=True)