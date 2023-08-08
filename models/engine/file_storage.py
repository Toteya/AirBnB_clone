"""
file_storage module
Contains the FileStorage class
"""
import json


class FileStorage:
    """
    FileStorage class
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): Path to the JSON file (e.g. file.json)
        __objects (dict): Will store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary `__objects`
        """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with the key <obj class name>.id
        """
        if obj is not None:
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            objs = []
            for key, value in self.__objects.items():
                objs.append(value.to_dict())
            json.dump(objs, file)

    def reload(self):
        """ Deserializes the JSON file to __objects if the JSON
        file (__file_path) exits.
        """
        import models.base_model as bm
        objs = []
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objs = json.load(file)
        except FileNotFoundError:
            pass

        for obj in objs:
            bm.BaseModel(obj)
