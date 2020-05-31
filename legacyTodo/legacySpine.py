import maya.mel as mel
import maya.cmds as cmds
def Spine_Create():
    # TODO: Get positions from guide
    # Create spine joints
    # Orient joints
    # Create Ik Spline
    # TODO: Align controllers to last spine joint before getting to the chest
    # Offset nodes for spine_01

    # Pelvis:
    # Get graph position for the pelvis.
    # Offset nodes for the pelvis 
    # TODO: Align and create controller for the pelvis.
    # TODO: parent constraint the pelvis joint to the pelvis controller maintaining offset,
    #       - In the legacy version, the pelvis controller was aligned to the spine_01,
    #         see if this is still necessary
    

    # COG:
    # Create a joint and a group for the COG.
    # Move the COG to the pelvis position in translation and rotation.
    # TODO: Create a controller and constraint the joint to that controller.

    # Create Joints_CV_Spine
    # TODO: Create a joint at the begining, middle and end of the spine ik curve
    #       Each of this joints should be parented under their offset group.
    # TODO: Make an skinCluster from this joints to the spine IK curve  
    #       resulting from the creation of the IKHandle from the first spine joint to 
    #       the chest joint
          

    start_CV_position = cmds.xform ('joint_Spine_1', ws=True, q=True, t=True)
    start_CV_rotation = cmds.xform ('joint_Spine_1', ws=True, q=True, ro=True)
    start_CV_joint= cmds.joint(n=('joint_Ctrl_Spine_1'))
    spine_01_CV_group= cmds.group (n=("Z_joint_Ctrl_Spine_1"))
    cmds.xform (spine_01_CV_group, ws=True, t=start_CV_position)
    cmds.xform (spine_01_CV_group, ws=True, ro=start_CV_rotation)
    cmds.select( d=True )
    
    #CV_Spine_Mid#
    trans_CV_Ctrl_Spine_Mid = cmds.xform ('joint_Spine_3', ws=True, q=True, t=True)
    rot_CV_Ctrl_Spine_Mid = cmds.xform ('joint_Spine_3', ws=True, q=True, ro=True)
    joint_CV_Ctrl_Spine_Mid= cmds.joint(n=('joint_Ctrl_Spine_Mid'))
    middle_CV_joint= cmds.group (n=("Z_joint_Ctrl_Spine_Mid"))
    emp_trans_joint_Spine_2 = cmds.xform (middle_CV_joint, ws=True, t=trans_CV_Ctrl_Spine_Mid)
    emp_rot_joint_Spine_2 = cmds.xform (middle_CV_joint, ws=True, ro=rot_CV_Ctrl_Spine_Mid)
    cmds.select( d=True )

    #CV_Spine_Chest#
    trans_CV_Ctrl_Spine_Chest = cmds.xform ('joint_Spine_5', ws=True, q=True, t=True)
    rot_CV_Ctrl_Spine_Chest = cmds.xform ('joint_Spine_5', ws=True, q=True, ro=True)
    joint_CV_Ctrl_Spine_Chest= cmds.joint(n=('joint_Ctrl_Spine_Chest'))
    Zjoint_CV_Ctrl_Spine_Chest= cmds.group (n=("Z_joint_Ctrl_Spine_Chest"))
    emp_trans_joint_Spine_3 = cmds.xform (Zjoint_CV_Ctrl_Spine_Chest, ws=True, t=trans_CV_Ctrl_Spine_Chest)
    emp_rot_joint_Spine_2 = cmds.xform (Zjoint_CV_Ctrl_Spine_Chest, ws=True, ro=rot_CV_Ctrl_Spine_Chest )
    cmds.select( d=True )

    #SKIN_CV
    Select_Joints_CV_1= cmds.select(start_CV_joint, r=True )
    Select_Joints_CV_3= cmds.select(joint_CV_Ctrl_Spine_Mid, add=True)
    Select_Joints_CV_5= cmds.select(joint_CV_Ctrl_Spine_Chest, add=True)
    Seelct_CV= cmds.select('CV_Spine_1',add=True)
    Skin_CV=cmds.skinCluster( 'joint_Ctrl_Spine_1','joint_Ctrl_Spine_Mid','joint_Ctrl_Spine_Chest', 'CV_Spine_1', dr=4)[0]
    
    #M_SpineFK_00_CTL
    translate = cmds.xform ('joint_Spine_2', ws=True, q=True, t=True)
    rot = cmds.xform ('joint_Spine_2', ws=True, q=True, ro=True)
    Position = cmds.xform ('P_M_SpineFK_00_CTL', ws=True, t=translate)
    Rotation= cmds.xform ('P_M_SpineFK_00_CTL', ws=True, ro=rot)
    #SpineMidAJUSTE
    translateCtrl_Spine_Mid = cmds.xform ('joint_Ctrl_Spine_Mid', ws=True, q=True, t=True)
    rotCtrl_Spine_Mid = cmds.xform ('joint_Ctrl_Spine_Mid', ws=True, q=True, ro=True)
    Position = cmds.xform ('P_M_SpineAdjoint_CTL', ws=True, t=translateCtrl_Spine_Mid)
    Rotation= cmds.xform ('P_M_SpineAdjoint_CTL', ws=True, ro=rotCtrl_Spine_Mid)
    cmds.select(d=True)
    #Create_joint_Chest#
    trans_Guide_Chest = cmds.xform ('Guide_Chest', ws=True, q=True, t=True)
    rot_Guide_Chest = cmds.xform ('Guide_Chest', ws=True, q=True, ro=True)
    Joint_Chest= cmds.joint(n=('joint_Chest'),rad=1*Scale_Guide)
    Grp_joint_Chest=cmds.group(n='Z_joint_Chest')
    emparentarTrans_joint_Chest = cmds.xform (Grp_joint_Chest, ws=True, t=trans_Guide_Chest)
    emparentarRot_joint_Chest = cmds.xform (Grp_joint_Chest, ws=True, ro=rot_Guide_Chest)
    #M_Chest_CTL#
    translate_joint_Chest  = cmds.xform ('Z_joint_Chest', ws=True, q=True, t=True)
    rotate_joint_Chest = cmds.xform ('Z_joint_Chest', ws=True, q=True, ro=True)
    Position_Chest = cmds.xform ("P_M_Chest_CTL", ws=True, t=translate_joint_Chest)
    Orientation_Chest= cmds.xform ("P_M_Chest_CTL", ws=True, ro=rotate_joint_Chest)
    Parent_Constraint_Chest=cmds.parentConstraint ('M_Chest_CTL', 'joint_Chest',mo=True)
    #Constraints#
    Orient_joint_Ctrl_Spine_1_Ctrl_Spine_1= cmds.orientConstraint('M_SpineFK_00_CTL',spine_01_CV_group,mo=True)
    Parent_joint_Ctrl_Spine_Mid_Ctrl_Spine_Mid= cmds.parentConstraint('M_SpineAdjoint_CTL',joint_CV_Ctrl_Spine_Mid,mo=True)
    Parent_joint_Ctrl_Spine_Chest_Ctrl_Spine_Chest= cmds.parentConstraint("M_Chest_CTL",joint_CV_Ctrl_Spine_Chest,mo=True)
    Point_Ctrl_Pelvis_start_CV_joint=cmds.pointConstraint('M_Pelvis_CTL',start_CV_joint)
    #Herarchy_Spine#
    Parent_Ctrl_Spine_Mid_Ctrl_Spine_Mid2= cmds.parent("P_M_SpineFK_01_CTL","M_SpineFK_00_CTL")
    Parent_Ctrl_Spine_Fk_2_Ctrl_Chest=cmds.parent("P_M_Chest_CTL","M_SpineFK_01_CTL")
    #Squash_Stretch#
    #Arclen#
    Cv_Info=cmds.arclen('CV_Spine_1', ch=True)
    Valor=cmds.getAttr('curveInfo1.arcLength')
    #MultiplyDivide_Stretch#
    NodeMultiplyDivide_Stretch_Spine= cmds.shadingNode('multiplyDivide',au=True, n="MD_Stretch_Spine")
    Operation_NodeMultiplyDivide_Stretch_Spine= cmds.setAttr((NodeMultiplyDivide_Stretch_Spine)+".operation",2)
    Set_Input2X_MD_Stretch= cmds.setAttr((NodeMultiplyDivide_Stretch_Spine)+".input2X",Valor)
    #MultiplyDivide_MASS_LOSS#
    NodeMultiplyDivide_MASS_LOSS_Spine= cmds.shadingNode('multiplyDivide',au=True, n="MD_MASS_LOSS_Spine")
    Operation_NodeMultiplyDivide_MASS_LOSS_Spine= cmds.setAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".operation",2)
    Set_Input2X_MD_MASS_LOSS= cmds.setAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".input1X",Valor)
    #Average_Spine_Mass_Loss#
    NodeplusMinusAverage= cmds.shadingNode('plusMinusAverage',au=True, n='AV_Spine_Mass_Loss')
    Set_Operation_Average=cmds.setAttr (NodeplusMinusAverage+".operation",3)
    #Conect Arclen_MD_STRETCH#
    ConectArclen_MD_Stretch= cmds.connectAttr((Cv_Info)+".arcLength",(NodeMultiplyDivide_Stretch_Spine)+".input1X")
    #Conect Arclen_MASS_LOSS_STRETCH#
    ConectArclen_MD_MASS_LOSS= cmds.connectAttr((Cv_Info)+".arcLength",(NodeMultiplyDivide_MASS_LOSS_Spine)+".input2X")
    #Conect_MD_Stretch_Joints#
    Conect_MD_Stretch_J1= cmds.connectAttr((NodeMultiplyDivide_Stretch_Spine)+".outputX","joint_Spine_1.scaleY")
    Conect_MD_Stretch_J2= cmds.connectAttr((NodeMultiplyDivide_Stretch_Spine)+".outputX","joint_Spine_2.scaleY")
    Conect_MD_Stretch_J3= cmds.connectAttr((NodeMultiplyDivide_Stretch_Spine)+".outputX","joint_Spine_3.scaleY")
    Conect_MD_Stretch_J4= cmds.connectAttr((NodeMultiplyDivide_Stretch_Spine)+".outputX","joint_Spine_4.scaleY")
    #Conect_MD_MASS_LOSS_Joints#
    Conect_MD_Stretch_J2= cmds.connectAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".outputX","joint_Spine_2.scaleX")
    Conect_MD_Stretch_J2= cmds.connectAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".outputX","joint_Spine_2.scaleZ")
    Conect_MD_Stretch_J2= cmds.connectAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".outputX","joint_Spine_3.scaleX")
    Conect_MD_Stretch_J2= cmds.connectAttr((NodeMultiplyDivide_MASS_LOSS_Spine)+".outputX","joint_Spine_3.scaleZ")   
    Connect_MD_MASS_LOSS_AV_0_Spine=cmds.connectAttr(NodeMultiplyDivide_MASS_LOSS_Spine+'.outputX', NodeplusMinusAverage+'.input3D[0].input3Dx',f=True)
    Connect_MD_MASS_LOSS_AV_1_Spine=cmds.connectAttr(NodeMultiplyDivide_MASS_LOSS_Spine+'.outputX', NodeplusMinusAverage+'.input3D[1].input3Dx',f=True)
    Disconnect_MD_AV=cmds.disconnectAttr (NodeMultiplyDivide_MASS_LOSS_Spine+'.outputX', NodeplusMinusAverage+'.input3D[1].input3Dx')
    Connect_AV_joint_Spine_1_X=cmds.connectAttr ('AV_Spine_Mass_Loss.output3Dx', 'joint_Spine_1.scaleX',f=True)
    Connect_AV_joint_Spine_1_Z=cmds.connectAttr ('AV_Spine_Mass_Loss.output3Dx', 'joint_Spine_1.scaleZ',f=True)
    Connect_AV_joint_Spine_4_X=cmds.connectAttr ('AV_Spine_Mass_Loss.output3Dx', 'joint_Spine_4.scaleX',f=True)
    Connect_AV_joint_Spine_4_Z=cmds.connectAttr ('AV_Spine_Mass_Loss.output3Dx', 'joint_Spine_4.scaleZ',f=True)
    ##Herarchy_Ctrl_Clavicle_L_Ctrl_Chest
    Parent_Ctrl_Clavicle_L_Ctrl_Chest= cmds.parent("P_L_Clavicle_CTL","M_Chest_CTL")
    ##Herarchy_Ctrl_Clavicle_R_Ctrl_Chest
    Parent_Ctrl_Clavicle_R_Ctrl_Chest= cmds.parent("P_R_Clavicle_CTL","M_Chest_CTL")
    #Grp_HiddenSpine
    Grp_Hidden_Spine=cmds.group( em=True, name='Hidden_Spine' )
    Parent_CV_Spine_Group=cmds.parent('CV_Spine_1','Hidden_Spine')
    Parent_Ik_Spline_Spine_Group=cmds.parent('IkSpline_Spine','Hidden_Spine')
    Hidde_IK_Handle_Arm_L=cmds.hide(Grp_Hidden_Spine)
    cmds.select(d=True)
    #Loc_Follow_Spine_Mid
    Loc_Follow_Spine_Mid=cmds.spaceLocator(n='Loc_Follow_Spine_Mid',p=(0, 0, 0))
    Grp_Loc_Follow_Spine_Mid=cmds.group(n='Z_Loc_Follow_Spine_Mid')
    ZGrp_Loc_Follow_Spine_Mid=cmds.group(n='P_Loc_Follow_Spine_Mid')
    cmds.select(d=True)
    #Loc_Follow_Spine_Pelvis
    Loc_Follow_Spine_Pelvis=cmds.spaceLocator(n='Loc_Follow_Spine_Pelvis',p=(0, 0, 0))
    Grp_Loc_Follow_Spine_Pelvis=cmds.group(n='Z_Loc_Follow_Spine_Pelvis')
    ZGrp_Loc_Follow_Spine_Pelvis=cmds.group(n='P_Loc_Follow_Spine_Pelvis')
    Position_Loc_Follow_Spine_Pelvis = cmds.xform (ZGrp_Loc_Follow_Spine_Pelvis, ws=True, t=translate_Guide_Pelvis)
    Rotation_Loc_Follow_Spine_Pelvis= cmds.xform (ZGrp_Loc_Follow_Spine_Pelvis, ws=True, ro=rot_Guide_Pelvis)
    cmds.select(d=True)
    #Loc_Follow_Spine_Chest
    Loc_Follow_Spine_Chest=cmds.spaceLocator(n='Loc_Follow_Spine_Chest',p=(0, 0, 0))
    Grp_Loc_Follow_Spine_Chest=cmds.group(n='Z_Loc_Follow_Spine_Chest')
    ZGrp_Loc_Follow_Spine_Chest=cmds.group(n='P_Loc_Follow_Spine_Chest')
    Position_Loc_Follow_Spine_Chest = cmds.xform (ZGrp_Loc_Follow_Spine_Chest, ws=True, t=translate_joint_Chest)
    Rotation_Loc_Follow_Spine_Chest= cmds.xform (ZGrp_Loc_Follow_Spine_Chest, ws=True, ro=rotate_joint_Chest)
    cmds.select(d=True)
    Position_Loc_Follow_Spine_Mid = cmds.xform (ZGrp_Loc_Follow_Spine_Mid, ws=True, t=translateCtrl_Spine_Mid)
    Rotation_Loc_Follow_Spine_Mid= cmds.xform (ZGrp_Loc_Follow_Spine_Mid, ws=True, ro=rotCtrl_Spine_Mid)
    NodeBColors_Follow_Ctrl_Spine_Mid= cmds.shadingNode('blendColors',au=True, n='BC_Follow_Ctrl_Spine_Mid')
    Connect_Pelvis_BC_Follow_Spine=cmds.connectAttr('M_Pelvis_CTL.translate',NodeBColors_Follow_Ctrl_Spine_Mid+'.color1')
    Connect_Chest_BC_Follow_Spine=cmds.connectAttr('M_Chest_CTL.translate',NodeBColors_Follow_Ctrl_Spine_Mid+'.color2')
    Connect_BC_Follow_Spine_Loc_Follow=cmds.connectAttr(NodeBColors_Follow_Ctrl_Spine_Mid+'.output','Loc_Follow_Spine_Mid.translate')
    Aim_Cons_Pelvis_Loc_Follow_Spine=cmds.aimConstraint ('Loc_Follow_Spine_Chest','Loc_Follow_Spine_Pelvis',w=1,aim=(0,1,0),u=(0,1,0),wut="objectrotation",wu=(1,0,0),wuo=('Loc_Follow_Spine_Chest'),mo=True)
    Connect_Ctrl_Chest_Loc_Follow_Spine_Chest=cmds.connectAttr('M_Chest_CTL'+'.translate','Loc_Follow_Spine_Chest.translate')
    Connect_Ctrl_Pelvis_Loc_Follow_Spine_Pelvis=cmds.connectAttr('M_Pelvis_CTL'+'.translate','Loc_Follow_Spine_Pelvis.translate')
    Connect_Loc_Follow_Spine_Z_Ctrl_Spine_Ajuste_Rot=cmds.connectAttr('Loc_Follow_Spine_Pelvis'+'.rotate','Loc_Follow_Spine_Mid.rotate')
    Connect_Loc_Follow_Spine_Z_Ctrl_Spine_Ajuste_Trans=cmds.connectAttr('Loc_Follow_Spine_Mid'+'.translate','Z_M_SpineAdjoint_CTL.translate')
    Connect_Loc_Follow_Spine_Z_Ctrl_Spine_Ajuste_Rot=cmds.connectAttr('Loc_Follow_Spine_Mid'+'.rotate','Z_M_SpineAdjoint_CTL.rotate')
    ParentCons_Ctrl_Spine_Fk_2_Ctrl_Spine_Ajuste=cmds.parentConstraint('M_SpineFK_01_CTL','P_M_SpineAdjoint_CTL',mo=True)
    ParentCons_Ctrl_Spine_Mid_Ctrl_Spine_Ajuste=cmds.parentConstraint('M_SpineFK_00_CTL','P_M_SpineAdjoint_CTL',mo=True)
    Herarchy_P_Loc_Follow_Spine_Mid_Ctrl_COG=cmds.parent(ZGrp_Loc_Follow_Spine_Mid,'M_Cog_CTL')
    Herarchy_P_Loc_Follow_Spine_Pelvis_Ctrl_COG=cmds.parent(ZGrp_Loc_Follow_Spine_Pelvis,'M_Cog_CTL')
    Herarchy_P_Loc_Follow_Spine_Chest_Ctrl_COG=cmds.parent(ZGrp_Loc_Follow_Spine_Chest,'M_Cog_CTL')
    #Herarchy_COG_Pelvis_Spine#
    Herarchy_Pelvis_COG=cmds.parent('Z_joint_Pelvis','joint_COG')
    Herarchy_P_Ctrl_Pelvis_Ctrl_COG=cmds.parent('P_M_Pelvis_CTL','M_Cog_CTL')
    Herarchy_P_Ctrl_Spine_Fk_1_Ctrl_COG=cmds.parent('P_M_SpineFK_00_CTL','M_Cog_CTL')
    #TwistSpine#
    Set_Enable_Twist_Control=cmds.setAttr ("IkSpline_Spine.dTwistControlEnable",1)
    Set_WorldUpType=cmds.setAttr ("IkSpline_Spine.dWorldUpType",4)
    Set_FowardAxis=cmds.setAttr ("IkSpline_Spine.dForwardAxis" ,2)
    Set_WorldUpAxis=cmds.setAttr ("IkSpline_Spine.dWorldUpAxis" ,3)
    Set_WorldUpVectorY_0=cmds.setAttr ("IkSpline_Spine.dWorldUpVectorY", 0)
    Set_WorldUpVectorEndY_0=cmds.setAttr ("IkSpline_Spine.dWorldUpVectorEndY", 0)
    Set_WorldUpVectorZ_1=cmds.setAttr ("IkSpline_Spine.dWorldUpVectorZ" ,1)
    Set_WorldUpVectorEndZ_1=cmds.setAttr ("IkSpline_Spine.dWorldUpVectorEndZ", 1)
    Connect_World_Matrix_World_Up_Matrix=cmds.connectAttr ('M_Pelvis_CTL.worldMatrix[0]', 'IkSpline_Spine.dWorldUpMatrix',f=True)
    Connect_World_Matrix_World_Up_MatrixEnd=cmds.connectAttr ('M_Chest_CTL.worldMatrix[0]', 'IkSpline_Spine.dWorldUpMatrixEnd',f=True)
    cmds.select(d=True)
    #Neck#
    rot_Guide_Neck = cmds.xform ('Guide_Neck', ws=True, q=True, ro=True)
    trans_Guide_Neck = cmds.xform ('Guide_Neck', ws=True, q=True, t=True)
    joint_Neck= cmds.joint(p=trans_Guide_Neck,n=('joint_Neck'),rad=.6*Scale_Guide)
    Grp_joint_Neck=cmds.group(n='Z_joint_Neck')
    cmds.select(d=True)
    #Head#
    rot_Guide_Head = cmds.xform ('Guide_Head', ws=True, q=True, ro=True)
    trans_Guide_Head = cmds.xform ('Guide_Head', ws=True, q=True, t=True)
    joint_Head= cmds.joint(p=trans_Guide_Head,n=('joint_Head'),rad=.6*Scale_Guide)
    Grp_joint_Head=cmds.group(n='Z_joint_Head')
    cmds.select(d=True)
    #M_Head_CTL#
    Position_Ctrl_Head = cmds.xform ("P_M_Head_CTL", ws=True, t=trans_Guide_Head)
    Rotate_Ctrl_Head = cmds.xform ("P_M_Head_CTL", ws=True, ro=rot_Guide_Head)
    Parent_Constraint_Chest=cmds.parentConstraint ('M_Head_CTL', 'joint_Head',mo=True)
    #M_Neck_CTL#
    Position_Ctrl_Neck = cmds.xform ("P_M_Neck_CTL", ws=True, t=trans_Guide_Neck)
    Rotate_Ctrl_Neck = cmds.xform ("P_M_Neck_CTL", ws=True, ro=rot_Guide_Neck)
    Parent_Constraint_Chest=cmds.parentConstraint ('M_Neck_CTL', 'joint_Neck',mo=True)
    #Herarchy_Joints#
    Grp_joint_Head_joint_Neck=cmds.parent(Grp_joint_Head,joint_Neck)
    Grp_joint_Neck_joint_Chest=cmds.parent(Grp_joint_Neck,Joint_Chest)
    #Herarchy_Ctrls#
    Grp_Ctrl_Head_Ctrl_Neck=cmds.parent('P_M_Head_CTL','M_Neck_CTL')
    Grp_Ctrl_Neck_Ctrl_Chest=cmds.parent('P_M_Neck_CTL','M_Chest_CTL')
    cmds.select(d=True)
    cmds.rename('curveInfo1','Cv_Info_Spine')