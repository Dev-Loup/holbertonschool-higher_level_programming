#!/usr/bin/python3
""" SuperClass module
    Creates the geometric base
    Classes:
        Base: set Base geometry parameters
"""

import json


class Base():
    """ Set geometry Base parameters
        Priv Class Attributes:
            __nb_objects: number of objects
        Pub instance attributes:
            id: instance identification
        Static methods:
            to_json_string: from dict_list to json_str
            from_json_string: from json_str to dict_list
        Class methods:
            save_to_file: from inst_list to json_file
            class_method: make an instance from **kwargs
            load_from_file: instantiate and list a json_file of
                            kwargs
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instance constructor
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a JSON string
            Args:
                list_dictionaries: data to represent
        """

        if list_dictionaries in (None, []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write a Json file with list_objs
            Args:
                cls: class name
                list_objs: list of instances
        """

        file = cls.__name__ + '.json'
        dict_list = []
        with open(file, 'w') as docfile:
            if list_objs is None:
                docfile.write([])
            else:
                for instance in list_objs:
                    dict_list.append(instance.to_dictionary())
                docfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Return a list from a json string
            Args:
                json_string: json string
        """

        if json_string in (None, []):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create and set a new instance
            Args:
                **dictionary: kwargs of class
        """

        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Instantiate and return a list of
            instances from json file
        """

        file = cls.__name__ + '.json'
        inst_list = []
        try:
            with open(file, 'r') as docfile:
                docread = docfile.read()
                doclist = Base.from_json_string(docread)
            for kwargs in doclist:
                inst_list.append(cls.create(**kwargs))
            return inst_list
        except IOError:
            return inst_list
