import pymel.core as pm

# ================================================================


class RigOps(object):
    def __init__(self):
        self.nom = {
            "controller": "CTL",
            "joint": "JNT",
            "bindJoint": "bind_JNT",
            "locator": "LOC",
            "group": "GRP",
            "ikHandle": "IKH",
            "ikEffector": "IKE",
            "ikCurve": "IKC",
            "skinCluster": "SKN"
        }
        self.prefix = {
            "middle": "m",
            "left": "l",
            "right": "r"
        }

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def create_offsets(self, target, name, parent=True):
        result = []
        group = pm.group(
            name=name + "_" + self.nom["group"],
            empty=True)

        locator = pm.spaceLocator(
            name=name + '_' + self.nom["locator"]
        )
        locator.getShape().setAttr("visibility", 0)

        locator.setParent(group)
        group.setTranslation(
            target.getTranslation(space="world"))
        group.setRotation(
            target.getRotation(space="world"))
        result.append(group)
        result.append(locator)

        if parent:
            target.setParent(locator)

        return result

    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    def ikHandle(
            self,
            startJoint,
            endEffector,
            name="default_ikHandle",
            solver="ikSplineSolver"
    ):
        result = pm.ikHandle(
            startJoint=startJoint,
            endEffector=endEffector,
            solver=solver
        )

        result[0].rename(name + "_" + self.nom["ikHandle"])
        result[1].rename(name + "_" + self.nom["ikEffector"])
        result[2].rename(name + "_" + self.nom["ikCurve"])
        return result
