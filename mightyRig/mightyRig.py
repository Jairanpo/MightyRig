import guides.biped.spineGuide as spineGuide
import guides.biped.legGuide as legGuide
import guides.biped.armGuide as armGuide
from graph.hierarchy import Graph
from graph.vertex import Vertex

# ================================================================

graph = Graph()

spineGuide.fill(graph)
legGuide.fill(graph, side="left")
legGuide.fill(graph, side="right")

armGuide.fill(graph, side="left")
armGuide.fill(graph, side="right")

graph.add_edge("pelvis", "l_femur")
graph.add_edge("pelvis", "r_femur")

graph.add_edge("chest", "l_upperarm")
graph.add_edge("chest", "r_upperarm")

print(graph)
