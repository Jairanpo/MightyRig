import maya.cmds as cmds
import sys
Path  = cmds.internalVar(usd = True)
print Path
PathRoot = Path + 'Autorig/Modules/Modules_Root'
sys.path.append(PathRoot)
def Base_Rig():
    window = cmds.window(title='Creating...')
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=8, width=300)    
    cmds.showWindow( window )
    #ARM_L
    import arm_l
    reload(arm_l)
    arm_l.Arm_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #ARM_R
    import arm_r
    reload(arm_r)
    arm_r.Arm_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #HAND_L
    import hand_l
    reload(hand_l)
    hand_l.Hand_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause(sec=0)
    #Attrs_Hand_L
    import Attr_Hand_L
    reload (Attr_Hand_L)
    Attr_Hand_L.Attrs_Hand_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause(sec=0)
    #HAND_R
    import hand_r
    reload(hand_r)
    hand_r.Hand_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause(sec=0)
    #Attrs_Hand_R
    import Attr_Hand_R
    reload (Attr_Hand_R)
    Attr_Hand_R.Attrs_Hand_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause(sec=0)
    #LEG_L
    import leg_l
    reload(leg_l)
    leg_l.Leg_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #FOOT_L
    import foot_l
    reload(foot_l)
    foot_l.Foot_L()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #LEG_R
    import leg_r
    reload(leg_r)
    leg_r.Leg_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #FOOT_R
    import foot_r
    reload(foot_r)
    foot_r.Foot_R()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    #SPINE
    import spine
    reload(spine)
    spine.Spine_Create()
    cmds.progressBar(progressControl, edit=True, step=1)
    #HERARCHY
    import herarchy
    reload(herarchy)
    herarchy.HERARCHY()
    cmds.progressBar(progressControl, edit=True, step=1)
    cmds.pause( sec=0)
    cmds.deleteUI( window, control=True )