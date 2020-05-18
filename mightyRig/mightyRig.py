import guides.biped.spineGuide as spineGuide
import guides.biped.legGuide as legGuide
import guides.biped.armGuide as armGuide
import guides.biped.fingersGuide as fingersGuide
from graph.hierarchy import Graph
from graph.vertex import Vertex

# ================================================================

graph = Graph()

spineGuide.fill(graph)

legGuide.fill(graph, side="left")
legGuide.fill(graph, side="right")
graph.add_edge("pelvis", "l_femur")
graph.add_edge("pelvis", "r_femur")

armGuide.fill(graph, side="left")
armGuide.fill(graph, side="right")
graph.add_edge("chest", "l_upperarm")
graph.add_edge("chest", "r_upperarm")

fingersGuide.fill(graph, side="left")
graph.add_edge("l_wrist", "l_thumb_01")
graph.add_edge("l_wrist", "l_index_01")
graph.add_edge("l_wrist", "l_middle_01")
graph.add_edge("l_wrist", "l_ring_01")
graph.add_edge("l_wrist", "l_pinky_01")
fingersGuide.fill(graph, side="right")
graph.add_edge("r_wrist", "r_thumb_01")
graph.add_edge("r_wrist", "r_index_01")
graph.add_edge("r_wrist", "r_middle_01")
graph.add_edge("r_wrist", "r_ring_01")
graph.add_edge("r_wrist", "r_pinky_01")
