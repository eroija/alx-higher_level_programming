#!/usr/bin/python3

"""Defines a base model class."""
import json
import os
import csv


class Base:

    """
    Base model represents the "base" for all
    other classes in project 0x0C python.

    Private class attribute:
        __nb_object (int): Number of instantiated
        Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
        Constructor for the Base class.

        Args:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of
        list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation
        of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries from the
        JSON string representation.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from the JSON file.
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
            list_dict = cls.from_json_string(json_str)
            return [cls.create(**obj) for obj in list_dict]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in cvs
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for dictionary in dict_list:
                writer.writerow(dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes in csv
        """
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            list_dict = []
            with open(filename, 'r', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    dictionary = {key: int(v) for key, v in row.items()}
                    list_dict.append(dictionary)
                return [cls.create(**obj) for obj in list_dict]
        else:
            return []
