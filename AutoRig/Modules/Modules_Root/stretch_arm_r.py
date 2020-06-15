import maya.cmds as cmds
import maya.mel as mel
def Get_Trans_Rot(Name):#OBTENER TRAslACION Y ROTACION DE UN OBJETO
    global translate,rot
    translate = cmds.xform (Name, ws=True, q=True, t=True)
    rot = cmds.xform (Name, ws=True, q=True, ro=True)
def Set_Trans_Rot(Name):#INselTAR TRAslACION Y ROTACION A UN OBJETO
    global Parent_Trans,Parent_Rot
    Parent_Trans = cmds.xform (Name, ws=True, t=translate)
    Parent_Rot = cmds.xform (Name, ws=True, ro=rot)
def Stretch_Arm_R():
    Gett_translateX_ForeArm_R=cmds.getAttr("J_ForeArm_Neutral_R.translateX")
    Gett_translateX_Hand_Neutral_R=cmds.getAttr("J_Hand_Neutral_R.translateX")
    Sum_ForeArm_Hand_Trans=Gett_translateX_ForeArm_R+Gett_translateX_Hand_Neutral_R
    DD_Arm_R=cmds.distanceDimension(sp=(0, 0, 0), ep=(1, 0, 0) )    #cleate DD_Arm_R#
    cmds.rename('locator1','Ini_Stretch_Arm_R')
    cmds.rename('locator2','End_Stretch_Arm_R')
    Rename_DD_Arm_R=cmds.rename('distanceDimension1','distanceDimension_Stretch_Master_Arm_R')
    cmds.select(cl=True)
    cmds.select('Ini_Stretch_Arm_R')
    Z_Ini_Stretch_Arm_R=cmds.group(n='Z_Ini_Stretch_Arm_R')
    cmds.select(cl=True)
    Get_Trans_Rot('End_Stretch_Arm_R')
    Z_End_Stretch_Arm_R=cmds.group(n='Z_End_Stretch_Arm_R',em=True)
    Set_Trans_Rot(Z_End_Stretch_Arm_R)
    cmds.parent('End_Stretch_Arm_R',Z_End_Stretch_Arm_R)
    cmds.select(cl=True)
    Get_Trans_Rot('J_Arm_Neutral_R')
    Set_Trans_Rot(Z_Ini_Stretch_Arm_R)
    Get_Trans_Rot('J_Hand_Neutral_R')
    Set_Trans_Rot(Z_End_Stretch_Arm_R)
    cmds.parent(Z_End_Stretch_Arm_R,'R_IK_Arm_CTL')
    cmds.parent(Z_Ini_Stretch_Arm_R,'R_FK_Arm_CTL')
    cmds.select(cl=True)
    Gett_Distance_Stretch_Arm_R=cmds.getAttr('distanceDimension_Stretch_Master_Arm_R.distance')
    Names_Nodes=['MD_Stretch_Arm_R','BC_Stretch_Arm_R','C_Stretch_Arm_R']
    Nodes=['multiplyDivide','blendColors','condition']
    num=0
    for Node in Names_Nodes:
        Create_Note=cmds.shadingNode(Nodes[num],au=True,n=Node)
        cmds.select(cl=True)
        num=num+1
    cmds.setAttr ('MD_Stretch_Arm_R.operation',2, k=True)
    cmds.setAttr ('MD_Stretch_Arm_R.input2X',-Sum_ForeArm_Hand_Trans, k=True)
    cmds.setAttr ('BC_Stretch_Arm_R.color2R',1)
    cmds.setAttr ('C_Stretch_Arm_R.operation',2, k=True)
    cmds.setAttr ('C_Stretch_Arm_R.secondTerm',-Sum_ForeArm_Hand_Trans, k=True)
    def Connect(Name,Name2,Attr1,Attr2):
        cmds.connectAttr(Name+Attr1,Name2+Attr2) 
    Connect('distanceDimension_Stretch_Master_Arm_R','MD_Stretch_Arm_R','.distance','.input1X')
    Connect('R_SwitchArm_CTL','BC_Stretch_Arm_R','.Stretch','.blender')
    Connect('MD_Stretch_Arm_R','BC_Stretch_Arm_R','.outputX','.color1R')
    Connect('BC_Stretch_Arm_R','C_Stretch_Arm_R','.outputR','.colorIfTrueR')
    Connect('distanceDimension_Stretch_Master_Arm_R','C_Stretch_Arm_R','.distance','.firstTerm')
    Connect('C_Stretch_Arm_R','J_Arm_IK_R','.outColorR','.scaleX')   
    Connect('C_Stretch_Arm_R','J_ForeArm_IK_R','.outColorR','.scaleX') 
    select_Arm=cmds.select('J_Arm_Neutral_R','J_ForeArm_Neutral_R')#Switch_FK_IK_Arm_R
    sel = cmds.ls (sl=True)
    cmds.select (cl=True)
    MD_switch_fk_ik = cmds.shadingNode ("multiplyDivide", asUtility=True, n="MD_Arm_Stretch_FK_IK_R")
    cmds.setAttr(MD_switch_fk_ik+'.operation',2)
    cmds.setAttr(MD_switch_fk_ik+'.input2X',10)
    cmds.connectAttr ('R_SwitchArm_CTL.Switch_FK_IK', MD_switch_fk_ik + ".input1X")
    Milista=[]#listA VACIA QUE RECIBIRA ROS NOMBRES _Neutral_R
    for J in sel:#FOR PARA EN BASE A RA selECCION(JOINTS) SE clEAN blendColors Y SE CONECTE ER multiplyDivide A ROS BRENDS
        N = J.split("_Neutral_R")[0]
        New_N=N.split("J_")[1]
        BC_rotate = cmds.shadingNode ("blendColors", asUtility=True, n="BS_" + New_N+"_stretch_R")
        cmds.select (cl=True)
        cmds.connectAttr (BC_rotate + ".output", J + ".scale")
        cmds.connectAttr (MD_switch_fk_ik + ".outputX", BC_rotate + ".blender")
        list.append(Milista,N)#AGREGA ER NOMBRE DER JOINT SIN NOMBRE DER SISTEMA A RA listA Milista
    def fun1(Var1):#FUNCION PARA AGREGAR STRING A ROS NOMBRES QUE EXISTEN EN Milista
        list.append (Milista, Milista[0] + Var1)
        list.append (Milista, Milista[1] + Var1)
    fun1('_FK_R')
    fun1('_IK_R')
    def fun(Var,Var2):#FUNCION PARA CONECTAR ROS JOINTS FK,IK A ROS BREND colols 
        cmds.connectAttr (Milista[2]+ "."+Var, "BS_Arm_"+Var2+"_R.color2")
        cmds.connectAttr (Milista[4]+ "."+Var, "BS_Arm_"+Var2+"_R.color1")
        cmds.connectAttr (Milista[3]+ "."+Var, "BS_ForeArm_"+Var2+"_R.color2")
        cmds.connectAttr (Milista[5]+ "."+Var, "BS_ForeArm_"+Var2+"_R.color1")
    fun('scale','stretch')
    cmds.parent('distanceDimension_Stretch_Master_Arm_R','hidden')
    cmds.hide('distanceDimension_Stretch_Master_Arm_R')
    cmds.hide('Ini_Stretch_Arm_R')
    cmds.hide('End_Stretch_Arm_R')
    cmds.select(cl=True)