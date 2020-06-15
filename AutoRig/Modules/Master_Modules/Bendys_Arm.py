import maya.cmds as cmds
import sys
Path  = cmds.internalVar(usd = True) 
PathRoot = Path + 'Autorig'+ '/Modules'+'/Modules_Root'
sys.path.append(PathRoot)
def Bendys():
    window = cmds.window(title='Creating...')
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=1, width=300)    
    cmds.showWindow( window )
    #RIBBON_ARM_L
    import ribbon_arm_l
    reload(ribbon_arm_l)
    ribbon_arm_l.Ribbon_Arm_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #RIBBON_ARM_R
    import ribbon_arm_r
    reload(ribbon_arm_r)
    ribbon_arm_r.Ribbon_Arm_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #Herarchy_Bendys#
    import herarchy_Bendy_Arm
    reload(herarchy_Bendy_Arm)
    herarchy_Bendy_Arm.Herarchy()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )