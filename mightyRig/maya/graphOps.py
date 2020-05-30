#import pymel.core as pm

# ================================================================


def build_parenting_list(graph):
    result = []
    for parent in graph.vertices:
        _vertex_parent = graph.get_vertex(parent)
        for child in _vertex_parent.children:
            result.append([parent, child])

    return result

