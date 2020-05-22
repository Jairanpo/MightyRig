import json
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex
import os

# ================================================================


def fill(graph=None, side="left"):
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

    _side = "l_" if side == "left" else "r_"
    _x_mirror = 1 if side == "left" else -1
    _json_path = os.path.dirname(__file__)
    _json_path = os.path.join(
        _json_path, "config", "arm.json")
    _config = None

    with open(_json_path, "r") as _data:
        _config = json.load(_data)["arm"]

    for key, values in _config.items():
        graph.add_vertex(Vertex(_side + str(key), {
            "position": [
                values["position"]["x"] * _x_mirror,
                values["position"]["y"],
                values["position"]["z"],
            ]
        }))

    for key, values in _config.items():
        for value in values["children"]:
            graph.add_edge(_side + key, _side + str(value))
