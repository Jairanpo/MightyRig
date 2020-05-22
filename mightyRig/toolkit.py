import mightyRig.guides.biped.structure as structure
import pymel.core as pm
import mightyRig.guides.styles as style
import mightyRig.guides.wireCurve as wireCurve
reload(wireCurve)

# ================================================================

# code for testing the graph inside maya, this should be refactored


def create_graph(
        spine=3,
        neck=3,
        length=4
):
    return structure.create(
        spine=spine,
        neck=neck,
        length=length)


def create_guide(graph=None):
    nodes = graph.depth_first("pelvis")
    root_group = pm.group(
        name="Skell_GRP",
        empty=True,
        world=True
    )

    guides_geometry = pm.group(
        name="Guides_GEO",
        empty=True,
        world=True
    )

    for each in nodes:
        vertex = graph.get_vertex(each)
        _joint_name = vertex.key + "_GDE"
        _group_name = vertex.key + "_GRP"

        group = pm.group(
            name=_group_name,
            empty=True,
            world=True)
        joint = pm.joint(
            name=_joint_name)
        joint.rename(vertex.key)
        style.node(joint, vertex.key)
        group.setTranslation(vertex.position)
        vertex.add_data("group", group)
        vertex.add_data("joint", joint)
        wireCurve.create(graph, vertex, guides_geometry)
