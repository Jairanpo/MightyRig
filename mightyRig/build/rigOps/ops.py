import pymel.core as pm
import mightyRig.build.rigOps.nomenclatures as nom
# ================================================================

reload(nom)


class Ops(nom.Nomenclatures):
    def __init__(self):
        super(Ops, self).__init__()

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def create_offsets(self, target, name, parent=True):
        result = []
        group = pm.group(
            name=name + "_" + self.nom["group"],
            empty=True)
        group.setAttr("useOutlinerColor", 1)
        group.setAttr("outlinerColor", self.color["dark"])

        locator = pm.spaceLocator(
            name=name + '_' + self.nom["locator"]
        )
        locator.getShape().setAttr("visibility", 0)

        locator.setAttr("useOutlinerColor", 1)
        locator.setAttr("outlinerColor", self.color["dark"])

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

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

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

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def add_attribute(self, node, attr, attributeType):
        if not pm.attributeQuery(attr, node=node, exists=True):
            node.addAttr(attr, attributeType=attributeType)
