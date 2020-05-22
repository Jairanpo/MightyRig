class Vertex:
    """
      Vertex class
    """

    def __init__(self, key='', values={}):
        if not isinstance(key, str) or not len(key) > 0:
            raise ValueError('Invalid key value')
        else:
            self.key = key
            self.position = (
                [0, 0, 0] if "position"
                not in values.keys() else values["position"])
            self.children = (
                [] if "children"
                not in values.keys() else values["children"])
            self.data = (
                {} if "data"
                not in values.keys() else values["data"]
            )

    def __repr__(self):
        return str(self.as_dict)

    def __str__(self):
        return str(self.as_dict)

    def __eq__(self, other):
        result = False
        if (self.key == other.key
            and self.children == other.children
                and self.position == other.position):
            result = True

        return result
    #     .     .     .     .     .     .
    @property
    def as_dict(self):
        result = {}
        result[self.key] = {}
        result[self.key]["position"] = self.position
        result[self.key]["children"] = self.children
        result[self.key]["data"] = self.data
        return result

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, values_dictionary):
        if isinstance(
                values_dictionary, dict):
            self._data = values_dictionary
        else:
            raise (
                ValueError(
                    '''Cannot assingn a 
                    non dict type to 
                    data property'''))

    def add_data(self, key, value):
        self.data[key] = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def values(self):
        return {
            "position": self.position,
            "children": self.children
        }

    @values.setter
    def values(self, values):
        self.position = values["position"]
        self.children = values["children"]

    #     .     .     .     .     .     .

    def add_child(self, child_name):
        if child_name not in self.children:
            self.children.append(child_name)
