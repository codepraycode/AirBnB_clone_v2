#!/usr/bin/python3
""" """
import unittest
from console import HBNBCommand;


class test_Console(unittest.TestCase):
    """Test Console """

    def test_help(self):
        """Test help in console"""
        out = HBNBCommand().onecmd("help")
        self.assertIsNone(out)
