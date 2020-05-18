from graph.vertex import Vertex
from graph.hierarchy import Graph

# ================================================================


def fill(graph=None, spine=3):
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .
    """Create spine graph configuration.

    Arguments:
        graph {Graph} -- Graph data structure.

    Keyword Arguments:
        spine {int} -- Amount of spine joints. (default: {3})

    Raises:
        ValueError: graph parameter should be an instance of the Graph Class.
        ValueError: spine parameter should be between 2 and 9.
    """
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    if graph is None:
        raise ValueError("graph parameter should be a Graph instance")

    if spine > 9 or spine < 2:
        raise ValueError("spine_joints parameter should be between 2 and 9")
    _y = 10

    _spine = []
    _spine.append(["pelvis", [0, _y, 0]])
    for i in range(1, spine + 1):
        _spine.append(
            [
                "spine_0{0}".format(i),
                [0, _y + i, 0]
            ]
        )
    _spine.append(["chest", [0, _y + spine + 1, 0]])

    #   .   .   .   .   .   .   .   .   .   .   .
    for each in _spine:
        graph.add_vertex(
            Vertex(each[0], {
                "position": each[1]
            })
        )

    for i in range(spine + 1):
        graph.add_edge(_spine[i][0], _spine[i + 1][0])

    return _spine[0][0]
