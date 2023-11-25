"""DB Storage manager for project
"""

from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from utils.generateId import generateObjId as generateId


CLASSES = {
    # "Amenity": Amenity,
    "User": User,
    "City": City,
    # "Place": Place,
    # "Review": Review,
    "State": State,
    # "BaseModel": BaseModel,
}

DATABASE = getenv("HBNB_MYSQL_DB")
USER = getenv("HBNB_MYSQL_USER")
HOST = getenv("HBNB_MYSQL_HOST")
PASSWORD = getenv("HBNB_MYSQL_PWD")
ENV = getenv("HBNB_ENV", 'none')



class DBStorage:
    """DB storage for project"""
    
    __engine = None
    __session = None

    def __init__(self):
        """Initialize class instance"""

        user = USER
        pwd = PASSWORD
        host = HOST
        db = DATABASE
        envv = ENV

        _connection_string = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(_connection_string)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns Dictionary of instance attributes

        Args:
            cls (obj, optional): Memory address of class. Defaults to None.

        Returns:
            dictionary of objects
        """

        db_obj = {}

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = generateId(elem)
                db_obj[key] = elem
        
        else:
            _classes = CLASSES.values()
            for _class in _classes:
                query = self.__session.query(_class)
                for elem in query:
                    key = generateId(elem)
                    db_obj[key] = elem
        

        return db_obj


    def new(self, obj):
        """Added obj to current database session

        Args:
            obj (obj): Object to save
        """

        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to database sesion
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete object from database session if it is not None

        Args:
            obj (obj, optional): Object to delete. Defaults to None.
        """
        
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in database and the current session
        """

        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        
        
        self.__session = Session()

    def close(self):
        """Close db session"""
        self.__session.close()
