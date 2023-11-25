#!/usr/bin/python3
""" Test case for Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Tests amenity class

    Args:
        test_basemodel (class): Inherits from this
    """

    def __init__(self, *args, **kwargs):
        """Initalize instance """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
