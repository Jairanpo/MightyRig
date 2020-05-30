import json
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex

import mightyRig.structure.biped.arm.fingers as fingers
import mightyRig.structure.biped.config as config

import os

# ================================================================


def insert(graph=None, side="left"):
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

    if graph is None:
        raise ValueError("graph parameter should be an instance of a Graph")
    if side.lower() not in ["left", "right"]:
        raise ValueError("side parameter should be \"right\" or \"left\"")

    #   .   .   .   .   .   .   .   .   .   .   .

    _side = "l_" if side == "left" else "r_"
    _x_mirror = 1 if side == "left" else -1

    _config = config.load("arm.json")["arm"]

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    for key, values in _config.items():
        _vertex = Vertex(_side + str(key), {
            "position": [
                values["position"]["x"] * _x_mirror,
                values["position"]["y"],
                values["position"]["z"],
            ]
        })

        _vertex.data = dict(values["data"])

        if side == "left":
            _vertex.add_data(
                "label",
                "left_arm")
        else:
            _vertex.add_data(
                "label",
                "right_arm")

        graph.add_vertex(_vertex)

    for key, values in _config.items():
        for value in values["children"]:
            graph.add_edge(_side + key, _side + str(value))

    # ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

    if side == "left":
        fingers.insert(
            graph,
            parent=graph.get_vertex("l_wrist"),
            side="left"
        )

    if side == "right":
        fingers.insert(
            graph,
            parent=graph.get_vertex("r_wrist"),
            side="right"
        )
