#!/usr/bin/python3
""" Module for testing the Base class. """
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Suite to test the Base class. """
    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Testing assigned id. """
        new = Base(12)
        self.assertEqual(new.id, 12)

    def test_default_id(self):
        """ test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_nb_objects_id(self):
        """ Test the nb object attribute. """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(12)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 12)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id. """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args. """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes. """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
