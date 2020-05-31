import pymel.core as pm
import mightyRig.maya.styles as style
import mightyRig.maya.wireCurve as wireCurve
import mightyRig.maya.graphOps as graphOps
import mightyRig.maya.shader as shader

# ================================================================


def insert_data_nodes(vertex):
    _group_name = vertex.key + "_GRP"
    _controller_name = vertex.key + "_CTL"
    _joint_name = vertex.key + "_JNT"
    _locator_name = vertex.key + "_Guide_LOC"

    left_shader = (
        pm.ls("l_Guide_SHD")
        if len(pm.ls("l_Guide_SHD")) > 0
        else shader.create("surfaceShader", "l_Guide_SHD")
    )

    right_shader = (
        pm.ls("r_Guide_SHD")
        if len(pm.ls("r_Guide_SHD")) > 0
        else shader.create("surfaceShader", "r_Guide_SHD")
    )

    middle_shader = (
        pm.ls("m_Guide_SHD")
        if len(pm.ls("m_Guide_SHD")) > 0
        else shader.create("surfaceShader", "m_Guide_SHD")
    )

    right_shader[0].setAttr("outColor", (0, .5, .4))
    left_shader[0].setAttr("outColor", (.1, .3, .8))
    middle_shader[0].setAttr("outColor", (.6, .2, .1))

    group = pm.group(
        name=_group_name,
        empty=True,
        world=True)

    controller = pm.sphere(
        name="{0}_CTL".format(vertex.key),
        radius=vertex.data["guide"]["controller_size"]
    )

    if vertex.key.startswith("l_"):
        pm.select(d=True)
        pm.select(controller[0])
        pm.hyperShade(assign=left_shader[0])
    elif vertex.key.startswith("r_"):
        pm.select(d=True)
        pm.select(controller[0])
        pm.hyperShade(assign=right_shader[0])
    else:
        pm.select(d=True)
        pm.select(controller[0])
        pm.hyperShade(assign=middle_shader[0])

    joint = pm.joint(
        name=_joint_name,
        radius=0.2)

    joint.setAttr("overrideEnabled", 1)
    joint.setAttr("overrideDisplayType", 2)

    locator = \
        pm.spaceLocator(
            name=_locator_name)

    locator.setAttr("visibility", 0)

    style.node(joint, vertex.key)

    locator.setParent(joint)
    joint.setParent(controller[0])
    controller[0].setParent(group)

    group.setTranslation(vertex.position)

    vertex.add_data("maya_guide",
                    {
                        "group": group,
                        "controller": controller,
                        "joint": joint
                    })

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def bind_skin(graph, guides):
    kwargs = {
        # or whatever you want to call it...
        'name': 'Mighty_Guide_skinCluster',
        'toSelectedBones': True,
        'bindMethod': 0,
        'skinMethod': 0,
        'normalizeWeights': 1
    }

    _joints = []
    for each in graph.get_vertices():
        _joints.append(each.data["maya_guide"]["joint"])

    for each_shape in guides.listRelatives(shapes=True):
        pm.skinCluster(_joints, each_shape, **kwargs)


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

def setup(graph=None):
    nodes = graph.depth_first("pelvis")
    root_group = pm.group(
        name="Mighty_Guide_GRP",
        empty=True,
        world=True
    )
    parenting_list = \
        graphOps.build_parenting_list(graph)

    guides_geometry = \
        pm.group(
            name="Guides_GEO",
            empty=True,
            world=True
        )

    for each in nodes:
        vertex = graph.get_vertex(each)

        insert_data_nodes(vertex)

        wireCurve.create(
            graph,
            vertex,
            guides_geometry
        )

    for parent, child in parenting_list:
        _parent_controller = \
            graph.get_vertex(parent).data["maya_guide"]["controller"][0]
        _child_joint = \
            graph.get_vertex(child).data["maya_guide"]["group"]

        _child_joint.setParent(_parent_controller)

    main_group = pm.group(name="Main_GRP", empty=True, world=True)
    main_controller = pm.circle(name="Main_CTL", normal=[0, 1, 0], radius=3)
    main_controller[0].setParent(main_group)
    graph.get_vertex(
        "pelvis").data["maya_guide"]["group"].setParent(
        main_controller[0])
    graph.get_vertex(
        "l_femur").data["maya_guide"]["group"].setParent(
        main_controller[0])
    graph.get_vertex(
        "r_femur").data["maya_guide"]["group"].setParent(
        main_controller[0])
    main_group.setParent(root_group)

    geometry_group = pm.group(name="Geometry_GRP", empty=True, world=True)
    guides_geometry.setParent(geometry_group)
    geometry_group.setParent(root_group)

    bind_skin(graph, guides_geometry)
