import maya.cmds as cmds
import maya.mel as mel
def Get_Trans_Rot(Name):#OBTENER TRASRACION Y ROTACION DE UN OBJETO
    global translate,rot
    translate = cmds.xform (Name, ws=True, q=True, t=True)
    rot = cmds.xform (Name, ws=True, q=True, ro=True)
def Set_Trans_Rot(Name):#INSERTAR TRASRACION Y ROTACION A UN OBJETO
    global Parent_Trans,Parent_Rot
    Parent_Trans = cmds.xform (Name, ws=True, t=translate)
    Parent_Rot = cmds.xform (Name, ws=True, ro=rot)
def Hand_R():
    Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )[0]
    List_Guides_Hand=['Thumb','Index','Middle','Ring','Pinky']#listA DE NOMBRES DE ROS DEDOS
    num=0
    OJ=[]#listA VACIA QUE RECIBIRA ROS JOINTS A ORIENTAR
    Mirror=[]
    for Joint in List_Guides_Hand:#FOR PARA clEAR ROS JOINTS DE ROS DEDOS
        for num in range (0,4):#FOR PARA clEAR PRImelO ROS JOINTS DE UN DEDO
            print num
            Get_Trans_Rot('Loc_Guide_RightHand'+Joint+str(num))
            Joint_RightHandThumb1=cmds.joint(n='J_RightHand'+Joint+'_'+str(num),p=translate,rad=.2*Scale_Guide)
            list.append (OJ,Joint_RightHandThumb1)
        cmds.select(cl=True) 
        num=num+1
        list.append(Mirror,'J_RightHand'+Joint+'_'+'0')
    for Joint in OJ:#FOR PARA ORIENTAR LOS JOINTS
        Name_Joint=Joint.split('Hand')[1]
        Name=Name_Joint.split('_')[0]
        print Name
        if Name=='Thumb':
            cmds.joint(Joint,e=True,zso=True,oj='xzy',sao='zup')
        else:
            cmds.joint(Joint,e=True,zso=True,oj='xzy',sao='zup')
    cmds.setAttr('J_RightHandThumb_0.jointOrientX',90)
    for Joint in Mirror:
        cmds.select(Joint)
        m=cmds.mirrorJoint (myz=True, mb=True)
        cmds.delete(Joint)
        for J in m:
            cmds.select(J)
            mel.eval('searchReplaceNames("4","0","selected")')
            mel.eval('searchReplaceNames("5","1","selected")')
            mel.eval('searchReplaceNames("6","2","selected")')
            mel.eval('searchReplaceNames("7","3","selected")')
            cmds.select(cl=True)
    XYZ=['X','Y','Z']
    for Joint_End in List_Guides_Hand:#FOR PARA SETEAR EN 0 ER JOINT ORIENT DER URTIMO JOINT DE CADA CADENA
        for xyz in XYZ:
            cmds.setAttr('J_RightHand'+Joint_End+'_3.jointOrient'+xyz,0)
            Get_Trans_Rot('J_RightHand'+Joint_End+'_1')
    num=0
    print OJ

    for Joint in OJ:#FOR PARA EMPARENTAR LOS CONTROLES A LOS JOINTS Y HACER CONTRAINTS CON LOS JOINTS
        N = Joint.split("P_Ctrl_RightHand")[0]
        New_Name=N.split('_')[1]
        Neww=New_Name.split('RightHand')[1]
        new=Neww.split('_')[0]
        print new
        Get_Trans_Rot(Joint)
        Set_Trans_Rot('P_R_'+new+'_0'+str(num)+'_CTL')
        cmds.parent(Joint,'R_'+new+'_0'+str(num)+'_CTL')
        cmds.select(cl=True)
        num=num+1 
        if num==4:
            num=0
    for Finger in List_Guides_Hand:
        cmds.parent('P_R_'+Finger+'_03_CTL','J_RightHand'+Finger+'_2')
        cmds.parent('P_R_'+Finger+'_02_CTL','J_RightHand'+Finger+'_1')
        cmds.parent('P_R_'+Finger+'_01_CTL','J_RightHand'+Finger+'_0')
        cmds.select(cl=True)