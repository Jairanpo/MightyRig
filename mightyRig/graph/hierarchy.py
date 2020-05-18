from graph.vertex import Vertex


class Graph:
    """
      Directed Acyclic Graph for creating hierarchy
      structures in the rigging system.
    """

    def __init__(self):
        self._vertices = {}

    @property
    def vertices(self):
        return self._vertices

    def add_vertex(self, vertex):
        if (all(v in vertex.children for v in self.vertices.keys())
                and len(vertex.children) != 0):
            raise ValueError("Vertex children not in Graph")

        if (isinstance(vertex, Vertex)
                and vertex.key not in self.vertices.keys()):
            self.vertices[vertex.key] = vertex
            return True
        else:
            return False

    def get_vertex(self, vertex_name):
        if vertex_name not in self.vertices.keys():
            raise ValueError("Vertex name not in graph")
        else:
            return self.vertices[vertex_name]

    def add_edge(self, parent, child):
        if parent in self.vertices.keys() and child in self.vertices.keys():
            self.vertices[parent].add_child(child)
            return True
        else:
            return False

    def __repr__(self):
        result = ''
        if len(self.vertices.keys()) > 0:
            for vertex in self.vertices.values():
                result += str(vertex)
                result += ",\n"
        return result
