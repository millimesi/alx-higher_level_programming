#!/usr/bin/python3
'''almost circle module'''

import json

class Base:
    '''class is created'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        ''' to json representation of dicts'''
        if not list_dictionaries or list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if not json_string or json_string == None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes to a file'''
        if list_objs == None:
            list_objs = []
        with open((cls.__name__ + ".json"), 'w') as f_name:
            f_name.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        dummy_obj = cls(1, 1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        '''that returns a list of instances from files'''
        try:
            with open(cls.__name__ + ".json", 'r') as f_name:
                data = f_name.read()
                if not data:
                    return []
                list_obj = cls.from_json_string(data)
                return [cls.create(**obj_dict) for obj_dict in list_obj]
        except FileNotFoundError:
            return []

                
    