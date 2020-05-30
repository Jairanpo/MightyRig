import pymel.core as pm

# ================================================================


def set_joint_orientation(
        list_of_joints,
        orientation,
        secondary_axis):
    for each_joint in list_of_joints:

        if each_joint == list_of_joints[-1]:
            orient_last_joint(list_of_joints)

        else:
            pm.joint(
                each_joint,
                edit=True,
                orientJoint=orientation,
                secondaryAxisOrient=secondary_axis,
                children=False)

            each_joint.rotateOrder.set(0)
        pm.makeIdentity(
            each_joint, apply=True, rotate=True)


def orient_last_joint(list_of_joints):
    oc = pm.orientConstraint(
        list_of_joints[-2],
        list_of_joints[-1],
        maintainOffset=False)
    list_of_joints[-1].jointOrient.set(0, 0, 0)
    pm.delete(oc)
