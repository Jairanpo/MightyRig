class Nomenclatures(object):
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
            "skinCluster": "SKN",
            "multiplyDivide": "MDN",
            "curveInfo": "CVI"
        }
        self.prefix = {
            "middle": "m",
            "left": "l",
            "right": "r"
        }

        self.color = {
            "dark": (0.5, 0.5, 0.5),
            "warning": (.8, .3, .3),
            "controller": (0.5, 0.5, 9)
        }
