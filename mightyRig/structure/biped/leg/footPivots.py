from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import mightyRig.graph.utils as utils
import mightyRig.structure.biped.config as config

# ================================================================


def insert(graph=None, parent=None, side="left"):
    utils.validate_graph(graph)
    utils.validate_vertex(parent)

    _config = config.load("pivots.json")["foot"]

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    outer_bank = (
        ["l_outterBank", 0.5] if side == "left" else [
            "r_outterBank", -0.5])
    inner_bank = (
        ["l_innerBank", -0.5] if side == "left" else [
            "r_innerBank", 0.5])

    for name, amount in [outer_bank, inner_bank]:
        _vertex = Vertex(name, {
            "position": [
                parent.position[0] + amount,
                parent.position[1],
                parent.position[2]
            ]
        })

        _vertex.data = dict(_config["bank"]["data"])

        graph.add_vertex(_vertex)

        graph.add_edge(parent.key, name)

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    heel = "l_heel" if side == "left" else "r_heel"
    _heel_vertex = Vertex(heel, {
        "position":
        [
            parent.position[0],
            parent.position[1],
            parent.position[2] - 1.5
        ]
    })

    _heel_vertex.data = _config["heel"]["data"]

    graph.add_vertex(_heel_vertex)
    graph.add_edge(parent.key, heel)
