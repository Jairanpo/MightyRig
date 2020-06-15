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
def Hand_L():
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    List_Guides_Hand=['Thumb','Index','Middle','Ring','Pinky']#LISTA DE NOMBRES DE LOS DEDOS
    num=0
    OJ=[]#LISTA VACIA QUE RECIBIRA LOS JOINTS A ORIENTAR
    for Joint in List_Guides_Hand:#FOR PARA CREAR LOS JOINTS DE LOS DEDOS
        for num in range (0,4):#FOR PARA CREAR PRIMERO LOS JOINTS DE UN DEDO
            Get_Trans_Rot('Guide_LeftHand'+Joint+str(num))
            Joint_LeftHandThumb1=cmds.joint(n='J_LeftHand'+Joint+'_'+str(num),p=translate,rad=.2*Scale_Guide)
            list.append (OJ,Joint_LeftHandThumb1)
            num=num+1
        cmds.select(cl=True)
    for Joint in OJ:#FOR PARA ORIENTAR LOS JOINTS
        Name_Joint=Joint.split('Hand')[1]
        Name=Name_Joint.split('_')[0]
        print Name
        if Name=='Thumb':
            cmds.joint(Joint,e=True,zso=True,oj='xzy',sao='zup')
        else:
            cmds.joint(Joint,e=True,zso=True,oj='xzy',sao='zup')
    cmds.setAttr('J_LeftHandThumb_0.jointOrientX',90)
    XYZ=['X','Y','Z']
    for Joint_End in List_Guides_Hand:#FOR PARA SETEAR EN 0 EL JOINT ORIENT DEL ULTIMO JOINT DE CADA CADENA
        for xyz in XYZ:
            cmds.setAttr('J_LeftHand'+Joint_End+'_3.jointOrient'+xyz,0)
            Get_Trans_Rot('J_LeftHand'+Joint_End+'_1')
    num=0
    for Joint in OJ:#FOR PARA EMPARENTAR LOS CONTROLES A LOS JOINTS Y HACER CONTRAINTS CON LOS JOINTS
        N = Joint.split("P_Ctrl_LeftHand")[0]
        New_Name=N.split('_')[1]
        Neww=New_Name.split('LeftHand')[1]
        new=Neww.split('_')[0]
        print new
        Get_Trans_Rot(Joint)
        Set_Trans_Rot('P_L_'+new+'_0'+str(num)+'_CTL')
        cmds.parent(Joint,'L_'+new+'_0'+str(num)+'_CTL')
        cmds.select(cl=True)
        num=num+1 
        if num==4:
            num=0
    for Finger in List_Guides_Hand:
        cmds.parent('P_L_'+Finger+'_03_CTL','J_LeftHand'+Finger+'_2')
        cmds.parent('P_L_'+Finger+'_02_CTL','J_LeftHand'+Finger+'_1')
        cmds.parent('P_L_'+Finger+'_01_CTL','J_LeftHand'+Finger+'_0')
        cmds.select(cl=True)