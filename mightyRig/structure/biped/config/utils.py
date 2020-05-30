import json
import os

# ================================================================


def load(filename):
    _json_path = os.path.dirname(__file__)
    _json_path = os.path.join(
        _json_path, filename)

    _config = None

    if os.path.isfile(_json_path):
        with open(_json_path, "r") as _data:
            _config = json.load(_data)
    else:
        raise ValueError("{0} is not a valid file path".format(_json_path))

    return _config


def add_data(vertex, values):
    if "data" in values.keys():
        for data_name, data_value in values["data"].items():
            vertex.add_data(data_name, data_value)
