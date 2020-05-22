from mightyRig.graph.vertex import Vertex
from mightyRig.graph.hierarchy import Graph

# ================================================================


def fill(graph=None, spine=3, neck=2, length=4):
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .
    """Create spine graph configuration.

    Arguments:
        graph {Graph} -- Graph data structure.

    Keyword Arguments:
        spine {int} -- Amount of spine joints. (default: {3})

    Raises:
        ValueError: graph parameter should be an instance of the Graph Class.
        ValueError: spine parameter should be between 2 and 9.
        ValueError: neck parameter should be between 1 and 9
    """
    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    if graph is None:
        raise ValueError(
            "graph parameter should be a Graph instance")

    if spine < 2 or spine > 9:
        raise ValueError(
            "spine parameter should be between 2 and 9")
    _y = 10

    if neck < 1 or neck > 9:
        raise ValueError(
            "neck parameter should be between 1 and 5")

    #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  .

    spine_list = []
    spine_list.append(["pelvis", [0, _y, 0]])
    spine_segment = length / float(spine)

    for i in range(1, spine + 1):
        _name = None

        if i == spine:
            _name = "chest"
        else:
            _name = "spine_0{0}".format(i)

        spine_list.append(
            [
                _name,
                [0, _y + (spine_segment * i), 0]
            ]
        )

    #   .   .   .   .   .   .   .   .   .   .   .

    neck_length = float(length) * 0.3
    neck_y = _y + length + 2.5
    neck_segment = neck_length/neck
    for i in range(1, neck + 1):
        _name = None
        if i == neck:
            _name = "head"
        else:
            _name = "neck_0{0}".format(i)

        spine_list.append(
            [
                _name,
                [
                    0,
                    neck_y + (neck_segment * i),
                    0
                ]
            ])

   #   .   .   .   .   .   .   .   .   .   .   .
    for each in spine_list:
        graph.add_vertex(
            Vertex(each[0], {
                "position": each[1],
            })
        )

    for i in range(len(spine_list) - 1):
        graph.add_edge(spine_list[i][0], spine_list[i + 1][0])
