#!/usr/bin/python3
""" Module for testing Rectangle class. """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ Suite for testing rectangle class. """
    def setUp(self):
        """ setting up nb objects. """
        Base._Base__nb_objects = 0

    def test_new_rect(self):
        """ Testing default rectangle id. """
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_assigned_rect_id(self):
        """ Testing assigned id. """
        r = Rectangle(10, 2, 0, 3, 24)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 24)

    def test_type_errors(self):
        """ Testing type of width, height, x and y. """
        r = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            r.width = "10"
            r.height = "Th"
            r.width = [2, 3, 4]
            r.height = (2, 4)
            r.width = {}
            r.height = {}
            r.x = {}
            r.x = "th"
            r.x = [2, 3, 4]
            r.y = {}
            r.y = "3"
            r.y = [5, 6, 7]

    def test_dimen_value(self):
        """ Testing if width and height are > 0. """
        r = Rectangle(24, 8)
        with self.assertRaises(ValueError):
            r.width = -10
            r.width = 0
            r.height = -4
            r.height = 0
