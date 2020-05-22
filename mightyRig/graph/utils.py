from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex


def validate_graph(graph):
    """Validate graph instance

    Keyword Arguments:
        graph {[type]} -- Graph node (default: {None})

    Raises:
        ValueError: "graph parameter should be an instance of a Graph class"
    """

    if not isinstance(graph, Graph):
        raise ValueError(
            "graph parameter should be an instance of a Graph class")


def validate_vertex(vertex=None):
    """Validate vertex instance

    Keyword Arguments:
        vertex {[type]} -- Vertex node (default: {None})

    Raises:
        ValueError: vertex parameter should be an instance of a Vertex class
    """
    if not isinstance(vertex, Vertex):
        raise ValueError(
            "vertex parameter should be an instance of a Vertex class")
