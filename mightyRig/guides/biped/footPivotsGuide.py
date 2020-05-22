from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import mightyRig.graph.utils as utils

# ================================================================


def fill(graph=None, parent=None, side="left"):
    utils.validate_graph(graph)
    utils.validate_vertex(parent)

    outer_bank = (
        ["l_outterBank", 0.5] if side == "left" else [
            "r_outterBank", -0.5])
    inner_bank = (
        ["l_innerBank", -0.5] if side == "left" else [
            "r_innerBank", 0.5])

    heel = "l_heel" if side == "left" else "r_heel"

    for name, amount in [outer_bank, inner_bank]:
        graph.add_vertex(Vertex(name, {
            "position": [
                parent.position[0] + amount,
                parent.position[1],
                parent.position[2]
            ]
        }))
        graph.add_edge(parent.key, name)

    graph.add_vertex(Vertex(heel, {
        "position":
        [
            parent.position[0],
            parent.position[1],
            parent.position[2] - 1
        ]
    }))
    graph.add_edge(parent.key, heel)
