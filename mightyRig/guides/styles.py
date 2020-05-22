import pymel.core as pm


def node(node, name=""):
    if name == "":
        raise ValueError("name parameter was not set")

    if isinstance(node, pm.nodetypes.Joint):
        node.setAttr("type", 18)
        node.setAttr("drawLabel", 1)
        node.setAttr("otherType", name)
        node.setAttr("overrideEnabled", 1)
        node.setAttr("overrideRGBColors", 1)
        if name.startswith("r_"):
            node.setAttr("overrideColorRGB", (0.3, .7, 0.2))
        elif name.startswith("l_"):
            node.setAttr("overrideColorRGB", (0, 0.2, 1))
        else:
            node.setAttr("overrideColorRGB", (0.9, 0.3, 0))
    elif isinstance(node, pm.nodetypes.NurbsCurve):
        node.setAttr("overrideEnabled", 1)
        node.setAttr("overrideRGBColors", 1)
        if name.startswith("r_"):
            node.setAttr("overrideColorRGB", (0.4, 0.8, 0.3))
        elif name.startswith("l_"):
            node.setAttr("overrideColorRGB", (0.1, 0.3, 1))
        else:
            node.setAttr("overrideColorRGB", (1, 0.4, .1))
