import mightyRig.guides.styles as style
import pymel.core as pm


def create(graph, vertex, guides_transform):
    for child_vertex in vertex.children:
        end_pos = (
            graph.get_vertex(child_vertex).position
        )

        curve = pm.curve(
            p=[
                vertex.position,
                vertex.position,
                end_pos,
                end_pos
            ]
        )
        shape = curve.getShape()
        style.node(
            shape,
            graph.get_vertex(child_vertex).key)
        pm.parent(
            shape, guides_transform,
            shape=True, relative=True)
        pm.delete(curve)
