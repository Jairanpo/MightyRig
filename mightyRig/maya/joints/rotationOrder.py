import pymel.core as pm

# ================================================================

def set_rotation_order(list_of_joints, rotation_order_int):
    for each_joint in list_of_joints:
        if type(each_joint) == pm.nodetypes.Transform:
            each_joint.rotateOrder.set(rotation_order_int)
        else:
            pass


def set_rotation_order_from_list(list_of_joints, list_of_rotation_orders):
    index = 0
    if len(list_of_rotation_orders) > len(list_of_joints):
        pm.warning(
            'set_rotation_order: list_of_joints and lis_of_rotation_orders do not match')
    else:
        for each_joint in list_of_joints:
            each_joint.rotateOrder.set(list_of_rotation_orders[index])
            index += 1
