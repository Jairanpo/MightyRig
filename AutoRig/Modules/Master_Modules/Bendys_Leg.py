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
    #RIBBON_LEG_L
    import ribbon_leg_l
    reload(ribbon_leg_l)
    ribbon_leg_l.Ribbon_Leg_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #RIBBON_LEG_R
    import ribbon_leg_r
    reload(ribbon_leg_r)
    ribbon_leg_r.Ribbon_Leg_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #Herarchy_Bendys#
    import herarchy_Bendy_Leg
    reload(herarchy_Bendy_Leg)
    herarchy_Bendy_Leg.Herarchy()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )