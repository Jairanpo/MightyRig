from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import mightyRig.structure.biped.spine.spineGuide as spineGuide
import mightyRig.structure.biped.leg.legGuide as legGuide
import mightyRig.structure.biped.arm.armGuide as armGuide


# ================================================================


def create(spine=4, neck=3, length=4):
    graph = Graph()

    spineGuide.insert(
        graph, spine=spine,
        neck=neck, length=length
    )

    legGuide.insert(graph, side="left")
    legGuide.insert(graph, side="right")
    graph.add_edge("pelvis", "l_femur")
    graph.add_edge("pelvis", "r_femur")

    armGuide.insert(graph, side="left")
    armGuide.insert(graph, side="right")
    for each in [
            "l_clavicle", "r_clavicle",
            "l_upperarm", "r_upperarm"
    ]:
        graph.add_edge("chest", each)

    return graph
