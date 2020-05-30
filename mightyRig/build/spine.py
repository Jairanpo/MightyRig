
# Maya imports
import pymel.core as pm

# ================================================================


class Spine:
    def __init__(self, graph, pelvis="pelvis", label="spine"):
        self._graph = graph
        self._order = []
        self._pelvis = pelvis
        self._label = label
        self._list_of_joints = []
        self._spine = graph.traverse_label(
            self._pelvis,
            self._label
        )

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
    def create_joints(self):
        for name in self.spine:
            _joint_name = ""
            vertex = self.graph.get_vertex(name)

            if name.endswith("_end"):
                _joint_name = "{0}_JNT".format(name)
            else:
                _joint_name = "{0}_BN_JNT".format(name)

            _joint = pm.joint(name=_joint_name, p=vertex.position)

            self._list_of_joints.append(_joint)
            vertex.add_data(["build", "joint"], _joint)

        self.orient_joints()

    def orient_joints(self):
        for name in self.spine[:-1]:
            vertex = self.graph.get_vertex(name)
            print(vertex)
            pm.joint(
                vertex.data["build"]["joint"],
                edit=True,
                orientJoint=vertex.data["orientation"]["orientJoint"],
                secondaryAxisOrient=vertex.data["orientation"]["secondaryAxisOrient"],
                children=False
            )
