import json
from graph.hierarchy import Graph
from graph.vertex import Vertex
import os

# ================================================================


def fill(graph=None, side="left"):
    """Create leg graph configuration.

    Keyword Arguments:
        graph {Graph} -- Graph data structure (default: {None})
        side {str} -- side to be created (default: {"left"})

    Raises:
        ValueError: graph parameter should be an instance of the Graph class.
        ValueError: side parameter should be either  \"right\" or  \"left\".
    """
    if graph is None:
        raise ValueError("graph parameter should be an instance of a Graph")
    if side.lower() not in ["left", "right"]:
        raise ValueError("side parameter should be \"right\" or \"left\"")

    _json_path = os.path.abspath('.')
    _json_path = os.path.join(
        _json_path, "mightyRig", "guides", "biped", "config", "leg.json")
    _config = None

    with open(_json_path, "r") as _data:
        _config = json.load(_data)["leg"]

    x_offset = 1 if side == "left" else -1
    _side = "l_" if side == "left" else "r_"

    for key in _config.keys():
        graph.add_vertex(
            Vertex(_side + str(key), {
                "position": [
                    _config[key]["position"]["x"] + x_offset,
                    _config[key]["position"]["y"],
                    _config[key]["position"]["z"]
                ]
            }))

    for key, values in _config.items():
        for value in values["children"]:
            graph.add_edge(_side + key, _side + str(value))
