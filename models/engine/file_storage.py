#!/usr/bin/python3
"""Defines class Filestorage
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from utils import generateId


CLASSES = {
     "Amenity": Amenity, "User": User,
     "City": City, "Place":Place,
     "Review": Review, "State": State,
     "BaseModel": BaseModel,
}




class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        fs_objects = {}

        _cls = None  # Class object after evaluation in the next few lines
        
        if cls:
            if type(cls) is str and cls in CLASSES:

                _cls = cls
            elif cls.__name__ in CLASSES:
                _cls = cls.__name__

        if not _cls:
            return self.__objects;


        for key, val in self.__objects.items():
            if _cls == key.split('.')[0]:
                fs_objects[key] = val
        return fs_objects


    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id

            Aguments:
                obj : An instance object.
        """
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        key = generateObjId(obj)
        value_dict = obj
        FileStorage.__objects[key] = value_dict


    def save(self):
        """Serialize __object to JSON file"""

        object_dict = {}

        for key, val in FileStorage.__objects.items():
            object_dict[key] = val.to_dict()
        
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(object_dict, fd)


    def reload(self):
        """Deserialize from JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            
            for obj_Id, obj in FileStorage.__objects.items():
                class_name = obj["__class__"]
                _class = CLASSES[class_name]
                FileStorage.__objects[obj_Id] = _class(**obj)


        except FileNotFoundError as f_err:
            pass
    

    def delete(self, obj=None):
        """Delete obj from __object if it's present

        Args:
            obj (any, optional): Object to remove. Defaults to None.
        """

        if obj is None: return

        # re-construct the key, as it was when saving
        key = generateObjId(obj)
        
        if key in self.__objects:
            del self.__objects[key]
            self.save()
