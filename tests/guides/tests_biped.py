from pytest import mark
import mightyRig.guides.biped as biped


@mark.biped
class BipedGuideTest:

    def test_biped_spine_default_guide():
        graph = biped.graph()
        assert graph.vertices == {
            "pelvis": {
                "position": [0, 10, 0],
                "children": ["r_upperLeg", "l_upperLeg", "spine_01"]
            },
            "spine_01": {
                "position": [0, 11, 0],
                "children": ["spine_02"]
            },
            "spine_02": {
                "position": [0, 12, 0],
                "children": ["spine_03"]
            },
            "spine_03": {
                "position": [0, 13, 0],
                "children": ["spine_03"]
            },
            "chest": {
                "position": [0, 13, 0],
                "children": []
            }
        }
