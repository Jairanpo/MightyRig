import maya.cmds as cmds
import maya.mel as mel
import sys
Path  = cmds.internalVar(usd = True)
PathMaster = Path + 'Autorig/Modules/Master_Modules'
PathCtrls_Proxy= Path + 'Autorig/Library_Ctrls/Ctrls_Proxy.ma'
PathCtrls_Bendys_Arm= Path + 'Autorig/Library_Ctrls/Ctrls_Bendy_Arm.ma'
PathCtrls_Bendys_Leg= Path + 'Autorig/Library_Ctrls/Ctrls_Bendy_Leg.ma'
PathGuides= Path + 'Autorig/Guide_RIG.ma'
sys.path.append(PathMaster)
import Proxy
reload(Proxy)
import Bendys_Arm
reload(Bendys_Arm)
import Bendys_Leg
reload(Bendys_Leg)
import Stretch_Arms
reload(Stretch_Arms)
import Stretch_Legs
reload(Stretch_Legs)
import Twist_Arms
reload(Twist_Arms)
import Twist_Legs
reload(Twist_Legs)
import Select_Bind_Joints
reload(Select_Bind_Joints)
# Make a new window
if cmds.window("Autorig",exists=True):
    cmds.deleteUI("Autorig")
window = cmds.window("Autorig",title="Autorig", iconName='Short Name',s=False, widthHeight=(210, 400) )
cmds.columnLayout( adjustableColumn=True )
cmds.separator( height=10, style='double' )
cmds.text ('Created by. Gaastonac')
cmds.separator( height=20, style='double' )
cmds.button( label='Import_Guides', command=('Guides()'),h=30)#BUTTON_GUIDES
cmds.separator( height=20, style='double' )
cmds.button( label='Create Rig Proxy', command=('Create_Proxy()'),h=50)
cmds.separator( height=10, style='double' )
Check_Proxy_Layout=cmds.checkBox(label='Proxy_Layout' )
cmds.separator( height=10, style='double' )
cmds.button( label='Add Modules', command=('Add_Module()'),h=50)
cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[ (1,120),(2,120),(3,120)], columnOffset=[(4,'right',3)])
Check_Bendy_Arms=cmds.checkBox(label='Bendys_Arm' )
Check_Bendy_Legs=cmds.checkBox(label='Bendys_Leg' )
Check_Stretch_Arms=cmds.checkBox(label='Stretch_Arm' )
Check_Stretch_Legs=cmds.checkBox(label='Stretch_Leg' )
Check_twist_arms=cmds.checkBox(label='Twist_Arm' )
Check_twist_legs=cmds.checkBox(label='Twist_Leg' )
cmds.columnLayout( adjustableColumn=True )
cmds.separator( height=10, style='double' )
cmds.button( label='Add Attr_Ani_CTL', command=('Add_Attr_Ctl_Ani()'),h=30)
cmds.button( label='SELECT_JOINTS_BIND', command=('Select_Bind()'),h=30)
cmds.showWindow( window )

def Guides():
    if cmds.objExists('Guide_Ctrl_Master')==False:
        cmds.file(PathGuides,i=True)
    else:
        cmds.warning( "LAS GUIAS YA SE IMPORTARON!!!" )
def Scale(Guide,Set):
    Scale_Guide=cmds.xform(Guide,ws=True, q=True, s=True )[0]
    cmds.select(Set)
    mel.eval('selectCurveCV("all")')
    cmds.scale (Scale_Guide,Scale_Guide,Scale_Guide,r=True,ocp=True)
    cmds.select(d=True)
    cmds.delete(Set)

def Create_Proxy():
    if cmds.objExists('hidden')==False:
        checkbox_Proxy_Layout= cmds.checkBox(Check_Proxy_Layout, q=True, v=True)
        if checkbox_Proxy_Layout==True:
            Scale_Guide=cmds.xform('Guide_Ctrl_Master',ws=True, q=True, s=True )
            cmds.group(n='Guide_Scale_Grp',em=True)
            cmds.select(cl=True)
            cmds.xform('Guide_Scale_Grp',ws=True,s=Scale_Guide)
            cmds.file(PathCtrls_Proxy,i=True)
            Scale('Guide_Ctrl_Master','Set_Ctrls_Proxy')
            Proxy.Base_Rig()
            cmds.parent('Guide_Scale_Grp','hidden')
            cmds.select(cl=True)
        else:
            cmds.warning( "NO SELECCIONASTE EL CHECKBOX DE PROXY!!!" )
    else:
        cmds.warning( "EL RIG_PROXY YA ESTA CREADO!!!" )

def Add_Attr_Ctl_Ani():#Funcion para agregar atributo a controles animables
    sel=cmds.ls(selection=True)
    for Ctrl in sel:
        if cmds.objExists(Ctrl+'.fbControl')==False:
            cmds.addAttr(Ctrl,ln='fbControl',attributeType='bool')
            cmds.setAttr(Ctrl+'.fbControl',k=True)
            cmds.setAttr(Ctrl+'.fbControl',1)
            cmds.setAttr(Ctrl+'.fbControl',lock=True)

def Add_Module():
    if cmds.objExists('hidden'):
        #######BENDY_ARM#######
        checkbox_bendys_arm= cmds.checkBox(Check_Bendy_Arms, q=True, v=True)
        if checkbox_bendys_arm==True:
            if cmds.objExists('Hidden_Bendy_Arm')==False:
                cmds.file(PathCtrls_Bendys_Arm,i=True)
                Scale('Guide_Scale_Grp','Set_Ctrls_Bendy_Arm')
                Bendys_Arm.Bendys()
            else:
                cmds.warning( "YA EXISTE MODULE BENDY_ARM" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE BENDY ARM!!" )
        
        #######BENDY_LEG#######
        checkbox_bendys_Leg= cmds.checkBox(Check_Bendy_Legs, q=True, v=True)
        if checkbox_bendys_Leg==True:
            if cmds.objExists('Hidden_Bendy_Leg')==False:
                    cmds.file(PathCtrls_Bendys_Leg,i=True)
                    Scale('Guide_Scale_Grp','Set_Ctrls_Bendy_Leg')
                    Bendys_Leg.Bendys()
            else:
                cmds.warning( "YA EXISTE MODULE BENDY_LEG" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE BENDY LEG!!" )
    
    #######STRETCH_ARMS#######
        checkbox_stretch_arm= cmds.checkBox(Check_Stretch_Arms, q=True, v=True)
        if checkbox_stretch_arm==True:
            if cmds.objExists('distanceDimension_Stretch_Master_Arm_L')==False:
                    Stretch_Arms.stretch_arm_l()
            else:
                cmds.warning( "YA EXISTE MODULE STRETCH ARMS" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE STRETCH ARMS!! " )
    
    #######STRETCH_LEGS#######
        checkbox_stretch_leg= cmds.checkBox(Check_Stretch_Legs, q=True, v=True)
        if checkbox_stretch_leg==True:
            if cmds.objExists('distanceDimension_Stretch_Master_Leg_L')==False:
                    Stretch_Legs.Stretch_leg_l()
            else:
                cmds.warning( "YA EXISTE MODULE STRETCH LEGS" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE STRETCH LEGS!! " )

    #######TWIST_ARMS#######
        checkbox_Twist_Arms= cmds.checkBox(Check_twist_arms, q=True, v=True)
        if checkbox_Twist_Arms==True:
            if cmds.objExists('Twist_Arms')==True:
                cmds.warning( "YA EXISTE MODULE TWIST ARMS!" )
            else: 
                if cmds.objExists('Hidden_Bendy_Arm')==True:
                        Twist_Arms.Twists_Arms()
                     
                else:
                    cmds.warning( "NO EXISTEN BENDYS ARMS!!" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE TWIST ARMS!! " )
        #######TWIST_LEGS#######
        checkbox_Twist_Legs= cmds.checkBox(Check_twist_legs, q=True, v=True)
        if checkbox_Twist_Legs==True:
            if cmds.objExists('Twist_Legs')==True:
                cmds.warning( "YA EXISTE MODULE TWIST LEGS!" )
            else:
                if cmds.objExists('Hidden_Bendy_Leg')==True:
                        Twist_Legs.Twists_Legs()
                else:
                    cmds.warning( "NO EXISTEN BENDYS LEGS!!" )
        else:
            cmds.warning( "NO SELECCIONASTE MODULE TWIST LEGS!! " )
    else:
        cmds.warning("NO HAS CREADO EL RIG PROXY")
def Select_Bind():
    Select_Bind_Joints.Selection()