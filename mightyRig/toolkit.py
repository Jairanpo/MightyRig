import mightyRig.build.biped.guide as bipedGuide

# ================================================================


def create_guide(**kwargs):
    graph = bipedGuide.create_graph(**kwargs)
    bipedGuide.create_guide(graph)
    return graph
