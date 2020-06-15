
import pymel.core as pm
import mightyRig.build.rigOps.ops as ops

# ================================================================

reload(ops)


class AnimCurveControl(ops.Ops):
    def __init__(self):
        super(AnimCurveControl, self).__init__()

    def setup(
            self,
            driver={"node": None, "attr": None},
            driven={"nodes": [], "attr": None}
    ):

        _driven_nodes_amount = len(driven["nodes"])

        self.add_attribute(
            driver["node"],
            driver["attr"],
            "double"
        )

        pm.setKeyframe(
            driver["node"],
            attribute=driver["attr"],
            time=1,
            value=0
        )

        pm.setKeyframe(
            driver["node"],
            attribute=driver["attr"],
            time=_driven_nodes_amount,
            value=0
        )

        pm.keyTangent(
            driver["node"],
            attribute=driver["attr"],
            weightedTangents=True,
            weightLock=False
        )

        pm.keyTangent(
            driver["node"],
            edit=True,
            attribute=driver["attr"],
            outAngle=50,
            time=1
        )

        pm.keyTangent(
            driver["node"],
            edit=True,
            attribute=driver["attr"],
            inAngle=50,
            time=_driven_nodes_amount
        )

        for i, each in enumerate(driven["nodes"]):
            _name = each.name().split("_")
            _name = "_".join(_name[:-1])
            _frame_cache_node = pm.createNode("frameCache")
            _frame_cache_node.rename(_name + "_FCH")
            pm.connectAttr(
                "{0}.{1}".format(driver["node"].name(), driver["attr"]),
                "{0}.{1}".format(_frame_cache_node.name(), "stream")
            )
            _frame_cache_node.varyTime.set(i + 1)

            self.add_attribute(each, driven["attr"], "double")
            each.setAttr(driven["attr"], keyable=True)

            pm.connectAttr(
                "{0}.{1}".format(_frame_cache_node.name(), "varying"),
                "{0}.{1}".format(each.name(), driven["attr"]),
            )

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def test(self):
        _test_group = pm.group(
            name="testAnimCurveControl_GRP",
            empty=True
        )
        _cubes_pos = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 2, 0],
            [0, 3, 0],
            [0, 4, 0],
        ]
        _cubes = []
        _controller = pm.circle(nr=[0, 1, 0])
        _controller[0].setParent(_test_group)
        for i in range(len(_cubes_pos)):
            _cube = pm.polyCube(
                name="cube_{0}_GEO".format(i),
            )
            _cube[0].setTranslation(_cubes_pos[i])
            _cube[0].setParent(_test_group)
            _cubes.append(_cube[0])

        _driver = {
            "node": _controller[0],
            "attr": "myAttr"
        }

        _driven = {
            "nodes": _cubes,
            "attr": "ty"
        }

        self.setup(driver=_driver, driven=_driven)

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
