import maya.cmds as cmds
import sys
Path  = cmds.internalVar(usd = True) 
PathRoot = Path + 'Autorig'+ '/Modules'+'/Modules_Root'
sys.path.append(PathRoot)

def Twists_Legs():
    window = cmds.window(title='Creating...')
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=1, width=300)    
    cmds.showWindow( window )
    #TWIST_Leg_L
    import Twist_Leg_L
    reload(Twist_Leg_L)
    Twist_Leg_L.Twist_Leg_L()
    #TWIST_Leg_R
    import Twist_Leg_R
    reload(Twist_Leg_R)
    Twist_Leg_R.Twist_Leg_R()
    cmds.group(n='Twist_Legs',em=True)
    cmds.parent('Twists_Leg_L','Twist_Legs')
    cmds.parent('Twists_Leg_R','Twist_Legs')
    cmds.parent('Twist_Legs','hidden')
    cmds.select(cl=True)
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )