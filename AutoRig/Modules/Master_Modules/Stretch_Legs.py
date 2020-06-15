import maya.cmds as cmds
import sys
Path  = cmds.internalVar(usd = True) 
PathRoot = Path + 'Autorig'+ '/Modules'+'/Modules_Root'
sys.path.append(PathRoot)
def Mult(Name):
    global Node
    Node=cmds.shadingNode('multiplyDivide',n=Name,au=True)
def Connect(Input, Output):
    cmds.connectAttr(Input,Output,f=True)
def Stretch_leg_l():
    window = cmds.window(title='Creating...')
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=1, width=300)    
    cmds.showWindow( window )
    #Stretch_leg_L
    import stretch_leg_l
    reload(stretch_leg_l)
    stretch_leg_l.stretch_Leg_l()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #Stretch_leg_R
    import stretch_leg_r
    reload(stretch_leg_r)
    stretch_leg_r.stretch_Leg_r()
    MDS=['MD_Scale_MS_Leg_L','MD_Scale_MS_Leg_R']
    #SCALE LEGS#
    for MD in MDS:
        Name=MD.split('MS_')[1]
        Mult(MD)
        Distancia=cmds.getAttr('distanceDimension_Stretch_Master_'+Name+'.distance')
        cmds.setAttr(Node+'.input2X',Distancia)
        Connect('C_mainA_ctl_0.scaleX',Node+'.input1X')
        Connect(Node+'.outputX','MD_Stretch_'+Name+'.input2X')
        Connect(Node+'.outputX','C_Stretch_'+Name+'.secondTerm')
    cmds.select(cl=True)
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )