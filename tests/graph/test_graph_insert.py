from pytest import mark, raises
from mightyRig.graph.hierarchy import Graph
from mightyRig.graph.vertex import Vertex


@mark.graph
class GraphInsertTests:
    def test_vertex_without_values(self):
        graph = Graph()
        vtx = Vertex("pelvis")
        graph.add_vertex(vtx)

        assert graph.get_vertex("pelvis") == Vertex("pelvis", {
            "position": [0, 0, 0],
            "children": []
        })

    def test_vertex_without_values_dict(self):
        graph = Graph()
        vtx = Vertex("pelvis")
        graph.add_vertex(vtx)

        assert graph.get_vertex("pelvis").as_dict == {
            "pelvis": {
                "position": [0, 0, 0],
                "children": [],
                "data": {}
            }
        }

    def test_only_with_position(self):
        graph = Graph()
        vtx = Vertex("vertex", {"position": [1, 3, 7]})
        graph.add_vertex(vtx)
        assert graph.get_vertex("vertex").position == [1, 3, 7]

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex(Vertex("vertex_01"))
        graph.add_vertex(Vertex("vertex_02"))

        graph.add_edge("vertex_01", "vertex_02")

        assert (
            graph.get_vertex("vertex_01").children == ["vertex_02"]
            and graph.get_vertex("vertex_02").children == []
        )

    def test_graph_vertex_several_insertions(self):
        graph = Graph()
        vtx_01 = Vertex("vertex_01")
        vtx_02 = Vertex("vertex_02")
        graph.add_vertex(vtx_01)
        graph.add_vertex(vtx_02)

        assert (
            graph.vertices == {
                "vertex_01": Vertex("vertex_01"),
                "vertex_02": Vertex("vertex_02")
            }
            and graph.get_vertex("vertex_01").as_dict == {
                "vertex_01": {
                    "position": [0, 0, 0],
                    "children": [],
                    "data": {}
                }
            }
            and graph.get_vertex("vertex_01").as_dict == {
                "vertex_01": {
                    "position": [0, 0, 0],
                    "children": [],
                    "data": {}
                }
            }
        )

    def test_graph_vertex_insertion_with_invalid_children(self):
        graph = Graph()
        vtx_01 = Vertex("vertex_01", {
            "children": ["vertex_02"]
        })

        with raises(ValueError):
            graph.add_vertex(vtx_01)
