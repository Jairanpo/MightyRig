import maya.cmds as cmds
def Selection():
    if cmds.objExists('Joints_')==True:
        if cmds.objExists('J_Bind*'):
            cmds.select('J_Bind*')
        Joints_Skin=['J_Spine_1', 'J_Spine_2', 'J_Spine_3', 'J_Spine_4','J_Pelvis','J_Chest','J_Neck','J_Head','J_Clavicle_L','J_Clavicle_R','J_Ankle_Neutral_L','J_Toe_Neutral_L','J_Ankle_Neutral_R','J_Toe_Neutral_R']
        for Joint in Joints_Skin:
            if cmds.objExists(Joint):
                cmds.select(Joint,add=True) 
        Fingers=['Thumb','Index','Ring','Middle','Pinky']
        num=0
        for J in Fingers:
            for num in range(0,4):
                cmds.select('J_LeftHand'+J+'_'+str(num),add=True)
                cmds.select('J_RightHand'+J+'_'+str(num),add=True)
                num=num+1
        if cmds.objExists("Joints_Bind_Skin") ==True:
            cmds.delete("Joints_Bind_Skin")
            cmds.sets(n="Joints_Bind_Skin" )
        else:
            cmds.sets(n="Joints_Bind_Skin" )
        cmds.select(cl=True)
    else:
        cmds.warning('NO HAY JOINTS CREADOS')