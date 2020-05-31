# Maya imports
import mightyRig.build.rigOps as rigOps
import pymel.core as pm

# ================================================================

reload(rigOps)


class Spine(rigOps.RigOps):
    def __init__(self, graph, pelvis="pelvis", label="spine"):
        super(Spine, self).__init__()
        self._graph = graph
        self._order = []
        self._pelvis = pelvis
        self._label = label
        self._list_of_joints = []
        self._spine = graph.traverse_label(
            self._pelvis,
            self._label
        )
        self.m = self.prefix["middle"]

    @property
    def spine(self):
        return self._spine

    @property
    def order(self):
        for i in range(len(self.spine)):
            if i != len(self.spine) - 1:
                self._order.append(
                    [self.spine[i], self.spine[i+1]])
        return self._order

    @property
    def graph(self):
        return self._graph

    @property
    def list_of_joints(self):
        return self._list_of_joints

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    # Maya functionality:
    def setup(self):
        for name in self.spine:
            _joint_name = ""
            vertex = self.graph.get_vertex(name)

            if name.endswith("_end"):
                _joint_name = \
                    "{0}_{1}_{2}" \
                    .format(self.m, name, self.nom["joint"])
            else:
                _joint_name = \
                    "{0}_{1}_{2}"\
                    .format(self.m, name, self.nom["bindJoint"])

            _joint = pm.joint(
                name=_joint_name, p=vertex.position)

            self._list_of_joints.append(_joint)
            vertex.add_data(["build", "joint"], _joint)

         #   .   .   .   .   .   .   .   .   .   .

        self.orient_joints()
        self.create_COG()

        #   .   .   .   .   .   .   .   .   .   .

        spine_01_vertex = \
            self.graph.get_vertex("spine_01")

        spine_offsets = self.create_offsets(
            spine_01_vertex.data["build"]["joint"],
            "{0}_spine_01".format(self.m)
        )

        #   .   .   .   .   .   .   .   .   .   .

        pelvis_vertex = self.graph.get_vertex("pelvis")
        pelvis_offsets = self.create_offsets(
            pelvis_vertex.data["build"]["joint"],
            "{0}_pelvis".format(self.m)
        )

        self.spine_ik()

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def orient_joints(self):
        for name in self.spine[:-1]:
            vertex = self.graph.get_vertex(name)
            _ori = "orientation"
            _sec = "secondaryAxisOrient"
            _oj = "orientJoint"
            pm.joint(
                vertex.data["build"]["joint"],
                edit=True,
                orientJoint=vertex.data[_ori][_oj],
                secondaryAxisOrient=(
                    vertex.data[_ori][_sec]
                ),
                children=False
            )

        self.graph.get_vertex(self.spine[-1])

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def create_COG(self):
        _pelvis_joint = \
            self.graph.get_vertex("pelvis")\
                .data["build"]["joint"]

        _joint = pm.joint(
            name="{0}_COG_{1}".format(
                self.m,
                self.nom["joint"]),
        )
        _offsets = self.create_offsets(
            _joint,
            "{0}_COG".format(self.m)
        )
        _offsets[0].setTranslation(
            _pelvis_joint
            .getTranslation(space="world"))

        _offsets[0].setRotation(
            _pelvis_joint
            .getRotation(space="world"))

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def spine_ik(self):
        chest_jnt = self.graph \
            .get_vertex("chest")\
            .data["build"]["joint"]

        _spine_ik_nodes = self.ikHandle(
            name="{0}_spine".format(self.m),
            startJoint=self.graph.get_vertex(
                "spine_01").data["build"]["joint"],
            endEffector=chest_jnt
        )

        for node in _spine_ik_nodes:
            node.setAttr("useOutlinerColor", 1)
            node.setAttr(
                "outlinerColor",
                self.color["warning"]
            )

        #   .   .   .   .   .   .   .   .   .   .

        _ik_curve = _spine_ik_nodes[-1]

        _start_pos = _ik_curve.getPointAtParam(0)
        _mid_pos = \
            _ik_curve \
            .getPointAtParam(_ik_curve.length()/2)

        truncated_length = float("{0:.4f}".format(_ik_curve.length()))

        _end_pos = \
            _ik_curve\
            .getPointAtParam(truncated_length)

        _start_joint = pm.joint(
            name="{0}_iKCurve{1}_{2}".format(
                self.m, "Start", self.nom["joint"]),
            p=_start_pos
        )
        self.create_offsets(
            _start_joint,
            "{0}_iKCurveStart".format(self.m))

        _mid_joint = pm.joint(
            name="{0}_iKCurve{1}_{2}".format(
                self.m, "Mid", self.nom["joint"]),
            p=_mid_pos
        )
        self.create_offsets(
            _mid_joint,
            "{0}_iKCurveMid".format(self.m))

        _end_joint = pm.joint(
            name="{0}_iKCurve{1}_{2}".format(
                self.m, "End", self.nom["joint"]),
            p=_end_pos
        )
        self.create_offsets(
            _end_joint,
            "{0}_iKCurveEnd".format(self.m))

        kwargs = {
            'name': '{0}_ikCurve_{1}'.format(
                self.m,
                self.nom["skinCluster"]
            ),

            'toSelectedBones': True,
            'bindMethod': 0,
            'skinMethod': 0,
            'normalizeWeights': 1
        }

        pm.skinCluster(
            [_start_joint, _mid_joint, _end_joint],
            _ik_curve, **kwargs)

     #   .   .   .   .   .   .   .   .   .   .
