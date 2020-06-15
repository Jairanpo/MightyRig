import maya.cmds as cmds
import sys
Path  = cmds.internalVar(usd = True) 
PathRoot = Path + 'Autorig'+ '/Modules'+'/Modules_Root'
sys.path.append(PathRoot)
def Twists_Arms():
    window = cmds.window(title='Creating...')
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=1, width=300)    
    cmds.showWindow( window )
    #TWIST_ARM_L
    import Twist_Arm_L
    reload(Twist_Arm_L)
    Twist_Arm_L.Twist_Arm_L()
    #TWIST_ARM_R
    import Twist_Arm_R
    reload(Twist_Arm_R)
    Twist_Arm_R.Twist_Arm_R()
    cmds.group(n='Twist_Arms',em=True)
    cmds.parent('Twists_Arm_L','Twist_Arms')
    cmds.parent('Twists_Arm_R','Twist_Arms')
    cmds.parent('Twist_Arms','hidden')
    cmds.select(cl=True)
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )