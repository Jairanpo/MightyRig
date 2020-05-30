from pytest import mark, raises
from mightyRig.graph.vertex import Vertex


@mark.graph
class VertexTests:
    vtx = Vertex("pelvis", {
        "position": [0, 1, 0],
        "children": ["spine_01", "spine_02"]
    })

    def test_vertex_creation_with_all_parameters(self):
        assert self.vtx == Vertex("pelvis", {
            "position": [0, 1, 0],
            "children": ["spine_01", "spine_02"]
        })

    def test_vertex_creation_with_key_type_dict(self):
        with raises(ValueError):
            Vertex({})

    def test_vertex_creation_with_key_type_array(self):
        with raises(ValueError):
            Vertex([], {})

    def test_vertex_creation_with_zero_length_key(self):
        with raises(ValueError):
            Vertex("")

    def test_vertex_equality(self):
        assert self.vtx == Vertex("pelvis", {
            "position": [0, 1, 0],
            "children": ["spine_01", "spine_02"]
        })

    def test_vertex_inequality(self):
        assert self.vtx != Vertex("pelvis", {
            "position": [0, 2, 0],
            "children": ["spine_01", "spine_02"]
        })

    def test_vertex_equality_dict(self):
        assert self.vtx.as_dict == {"pelvis": {
            "position": [0, 1, 0],
            "children": ["spine_01", "spine_02"],
            "data": {}
        }}

    def test_insert_data_one_level(self):
        vtx = Vertex("pelvis")
        vtx.add_data("foo", "bar")

        assert vtx.data == {"foo": "bar"}

    def test_insert_data_two_levels(self):
        vtx = Vertex("pelvis")
        vtx.add_data(["foo", "bar"], "baz")

        assert vtx.data == {"foo": {"bar": "baz"}}

    def test_insert_data_three_levels(self):
        vtx = Vertex("pelvis")
        vtx.add_data(["foo", "bar", "baz"], "var")
        assert vtx.data == {"foo": {"bar": {"baz": "var"}}}
