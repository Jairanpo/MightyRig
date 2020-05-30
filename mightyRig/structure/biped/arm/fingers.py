import json
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import mightyRig.structure.biped.config as config

import mightyRig.graph.utils as utils
import os

# ================================================================


def insert(graph=None, parent=None, side="left"):
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .
    """Create leg graph configuration.

    Keyword Arguments:
        graph {Graph} -- Graph data structure (default: {None})
        side {str} -- side to be created (default: {"left"})

    Raises:
        ValueError: graph parameter should be an instance of the Graph class.
        ValueError: side parameter should be either  \"right\" or  \"left\".
    """
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    utils.validate_graph(graph)
    utils.validate_vertex(parent)

    _side = "l_" if side == "left" else "r_"
    _x_mirror = 1 if side == "left" else -1

    _config = config.load("fingers.json")["fingers"]

    for key, values in _config.items():
        _phalange = _side + str(key)
        _thumb_modifier = 0 if "thumb" not in key else -0.5

        _vertex = Vertex(_phalange, {
            "position": [
                parent.position[0] + values["position"]["x"] * _x_mirror,
                parent.position[1] + _thumb_modifier,
                values["position"]["z"],
            ]
        })

        _vertex.data = dict(values["data"])

        if side == "left":
            _vertex.add_data(
                "label",
                "left_finger")
        else:
            _vertex.add_data(
                "label",
                "right_finger")

        graph.add_vertex(_vertex)

        if key.endswith("_01"):
            graph.add_edge(parent.key, _phalange)

    for key, values in _config.items():
        for value in values["children"]:
            graph.add_edge(_side + key, _side + str(value))
