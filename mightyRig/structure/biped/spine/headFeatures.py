import json
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import mightyRig.graph.utils as utils
import mightyRig.structure.biped.config.utils as config
import os

# ================================================================


def insert(graph=None, parent=None):
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .
    """Create leg graph configuration.

    Keyword Arguments:
        graph {Graph} -- Graph data structure (default: {None})
        side {str} -- side to be created (default: {"left"})

    Raises:
        ValueError: graph parameter should be an instance of the Graph class.
        ValueError: parent parameter should be an instance of the Vertex class.
    """
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    utils.validate_graph(graph)
    utils.validate_vertex(parent)

    _config = config.load("face.json")["face"]
    _sides = [["l_", 1], ["r_", -1]]

    for side, value in _sides:
        new_vertex_name = side + "eye"

        _vertex = Vertex(new_vertex_name, {
            "position": [
                .5 * value,
                parent.position[1] + 0.5,
                1
            ]})

        config.add_data(_vertex, _config["eye"])

        graph.add_vertex(_vertex)
        graph.add_edge(parent.key, new_vertex_name)

    _jaw_vertex = Vertex("jaw", {
        "position":
        [
            0,
            parent.position[1] - 0.25,
            .5
        ]
    })

    config.add_data(_jaw_vertex, _config["jaw"])

    graph.add_vertex(_jaw_vertex)

    graph.add_edge(parent.key, "jaw")
