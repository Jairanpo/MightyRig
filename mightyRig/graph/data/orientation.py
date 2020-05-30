

def compose(
        orientJoint="yxz",
        secondaryAxisOrient="xup",
        children=False,
        reverse=False):
    return {
        "orientJoint": orientJoint,
        "secondaryAxisOrient": secondaryAxisOrient,
        "children": children,
        "reverse": reverse
    }
