import mightyRig.guides.biped.spineGuide as spineGuide
import mightyRig.guides.biped.legGuide as legGuide
import mightyRig.guides.biped.armGuide as armGuide
import mightyRig.guides.biped.fingersGuide as fingersGuide
import mightyRig.guides.biped.headFeaturesGuide as headFeaturesGuide
import mightyRig.guides.biped.footPivotsGuide as footPivotsGuide
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex

reload(spineGuide)
reload(headFeaturesGuide)
reload(armGuide)
# ================================================================


def create(spine=3, neck=2, length=4):
    graph = Graph()

    spineGuide.fill(
        graph, spine=spine,
        neck=neck, length=length
    )
    headFeaturesGuide.fill(
        graph,
        graph.get_vertex("head")
    )

    legGuide.fill(graph, side="left")
    legGuide.fill(graph, side="right")
    graph.add_edge("pelvis", "l_femur")
    graph.add_edge("pelvis", "r_femur")

    footPivotsGuide.fill(
        graph,
        parent=graph.get_vertex("l_ball"),
        side="left"
    )
    footPivotsGuide.fill(
        graph,
        parent=graph.get_vertex("r_ball"),
        side="right"
    )

    armGuide.fill(graph, side="left")
    armGuide.fill(graph, side="right")
    for each in [
            "l_clavicle", "r_clavicle",
            "l_upperarm", "r_upperarm"
    ]:
        graph.add_edge("chest", each)

    fingersGuide.fill(
        graph,
        parent=graph.get_vertex("l_wrist"),
        side="left"
    )

    fingersGuide.fill(
        graph,
        parent=graph.get_vertex("r_wrist"),
        side="right"
    )

    return graph
