import pymel.core as pm
import mightyRig.build.rigOps.ops as ops
# ================================================================

reload(ops)


class StretchSpline(ops.Ops):
    def __init__(self):
        super(StretchSpline, self).__init__()
        self._curve_info_node = None
        self._ik_handle = None
        self._ik_handle_curve = None
        self._ik_handle_effector = None

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def setup(self):
        pass

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    @property
    def curve_info_node(self):
        return self._curve_info_node

    @curve_info_node.setter
    def curve_info_node(self, value):
        if isinstance(value, pm.nt.CurveInfo):
            self._curve_info_node = value
        else:
            raise ValueError(
                "Value is not an instance of a CurveInfo")

    @property
    def ik_handle(self):
        return self._ik_handle

    @ik_handle.setter
    def ik_handle(self, value):
        if isinstance(value, pm.nt.IkHandle):
            self._ik_handle = value
        else:
            raise ValueError(
                "Value is not an instance of an IkHandle")

    @property
    def ik_handle_curve(self):
        return self._ik_handle_curve

    @ik_handle_curve.setter
    def ik_handle_curve(self, value):
        if isinstance(value, pm.nt.NurbsCurve):
            self._ik_handle_curve = value
        else:
            raise ValueError(
                "Value is not an instance of an NurbsCurve")

    @property
    def ik_handle_effector(self):
        return self._ik_handle_effector

    @ik_handle_effector.setter
    def ik_handle_effector(self, value):
        if isinstance(value, pm.nt.IkEffector):
            self._ik_handle_effector = value
        else:
            raise ValueError(
                "Value is not an instance of an IkEffector"
            )

    @property
    def joint_list(self):
        if self._ik_handle is None:
            raise ReferenceError(
                "ik handle node hasn't being assigned yet.")
        else:
            return self._ik_handle.getJointList()

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def create_curve_info_node(
            self,
            curve_node,
            name="default_curveInfo"):
        _name = pm.arclen(
            curve_node,
            constructionHistory=True)

        self.curve_info_node = pm.ls(
            _name, type="curveInfo")[0]

        print(self.nom)
        self.curve_info_node.rename(
            "{0}_{1}".format(
                name, self.nom["curveInfo"]))

        self.curve_info_node.addAttr(
            "normalizedScale",
            attributeType="double")

        #   .   .   .   .   .   .   .   .   .   .   .

        _quotient_node = \
            pm.createNode(
                "multiplyDivide",
                name="{0}Division_{1}"
                .format(
                    name, self.nom["multiplyDivide"])
            )
        _quotient_node.setAttr("operation", 2)

        self.curve_info_node\
            .arcLength.connect(_quotient_node.input1X)
        _quotient_node.setAttr(
            "input2X", curve_node.length())

        _quotient_node.outputX.connect(
            self.curve_info_node.normalizedScale)

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def get_joints_primary_axis(self, list_of_joints):
        _child = list_of_joints[1]
        result = []
        if _child.tx.get() > _child.ty.get() \
                and _child.tx.get() > _child.tz.get():
            result = ["tx", "ty", "tz"]
        elif _child.ty.get() > _child.tx.get() \
                and _child.ty.get > _child.tz.get():

            result = ["ty", "tx", "tz"]
        elif _child.tz.get() > _child.tx.get() \
                and _child.tz.get() > _child.ty.get():
            result = ["tz", "tx", "ty"]
        else:
            raise ValueError('''
                The given list of joints does not 
                have a primary axis, this problem 
                might be caused by a list of joints 
                where all the joints have the same 
                position or there are only one 
                joint in the chain
            ''')
        return result

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    def create_test_chain(self):
        _pos_matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 2, 0],
            [0, 3, 0],
            [0, 4, 0],
        ]
        _joints = []
        for i, each in enumerate(_pos_matrix):
            _joints.append(
                pm.joint(
                    n="{}_{}_{}".format(
                        self.prefix["middle"],
                        "joint0" + str(i+1),
                        self.nom["joint"]),
                    p=each)
            )

        _ik_handle_nodes = self.ikHandle(
            startJoint=_joints[0],
            endEffector=_joints[-1],
        )
        self.ik_handle = _ik_handle_nodes[0]
        self.ik_handle_effector = _ik_handle_nodes[1]
        self.ik_handle_curve = _ik_handle_nodes[2].getShape()
