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

    def test_rectangle(self):
        """ Tests the initialization of a rectangle. """
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rectangle_2(self):
        """ Tests the initialization with all attributes. """
        r = Rectangle(12, 4, 3, 2, 24)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 24)

    def test_new_rectangles(self):
        """ Tests new rectangles. """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        self.assertEqual(False, r1 is r2)
        self.assertEqual(False, r1.id == r2.id)

    def test_is_Base_instance(self):
        """ Tests Ractangle is a Base instance. """
        r = Rectangle(10, 2)
        self.assertEqual(True, isinstance(r, Base))

    def test_less_ammount_attr(self):
        """ Test when no/less arg is passed. """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10)
            r2 = Rectangle()

    def test_access_private_attr(self):
        """ Trying to access the private attributes. """
        r = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r.__width
            r.__height
            r.__x
            r.__y

    def test_type_attr(self):
        """ Tests if width, height, x, y type values are correct. """
        with self.assertRaises(TypeError):
            r1 = Rectangle("2", 10, 3, 3, 3)
            r2 = Rectangle(2, "10", 3, 3, 3)
            r3 = Rectangle(2, 10, "3", 3, 3)
            r4 = Rectangle(2, 10, 3, "3", 3)

    def test_value_attr(self):
        """ Tests if width and height values are > 0. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-4, 2)
            r2 = Rectangle(2, -4)

    def test_value_attr_2(self):
        """ Tests if x and y values are >= 0. """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -3, 0, 3)
            r2 = Rectangle(10, 2, 0, -3, 4)

    def test_area(self):
        """ Tests the area of the rectangle. """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
