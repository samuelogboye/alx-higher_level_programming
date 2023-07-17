#!/usr/bin/python3
"""The Base class"""

import json

class Base:
    """Defining Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ a function that returns the JSON representation of an
        object (list_dictionaries)"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                json_file.write(Base.to_json_string(list_dicts))
