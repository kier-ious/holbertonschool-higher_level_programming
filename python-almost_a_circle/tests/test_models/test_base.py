#!/usr/bin/python3
"""Unittest for Base case

    Classes to test from base.py
        TestBase_test_create_instance
        TestBase_test_to_json_string
        TestBase_from_json_string
        TestBase_test_create
        TestBase_load from_from_file
        TestBase_test_create_with_invalid_arguments
        TestBase_test_create_with_negative_id
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """Testing for instantiation for Base class"""
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError, "too many arguments"):
            Base(1, 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

# Test for Create method ------------------------------------------------------
class test_create_instance(unittest.BaseCase):
    """Testing the create method for the Base class"""

    def test_create_rectangle_original(self):
        r1 = Rectangle(1, 3, 5, 7, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(1, 3, 5, 7, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_equals(self):
        r1 = Rectangle(1, 3, 5, 7, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

class TestBase_to_json_string(unittest.TestCase):
    """Testing to_json_string method of Base class"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(14, 12, 10, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(14, 12, 10, 8, 6)
        self.asserTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dict(self):
        r1 = Rectangle(14, 12, 10, 8, 6)
        r2 = Rectangle(15, 13, 11, 9, 7)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.asserTrue(len(Base.to_json_string(list_dicts)) == 107)

# Square Test to_json_string---------------------------------------------------
    def test_to_json_string_square_type(self):
        s = Square(14, 12, 10, 8)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(14, 12, 10, 8)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dict(self):
        s1 = Square(14, 12, 10, 8)
        s2 = Square(15, 13, 11, 9)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.asserTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_noargs(self):
        with self.assertRaisesRegex(TypeError):
            Base.to_json_string([], 1)

class from_json_string(unittest.TestCase):
        # Test w/ an empty JSON string
        result = Base.from_json_string('')
        Base.assertEqual(result, [])

        # Test w/ a JSON string
        json_string = '[{"key1": "value1", "key2": "value2"}]'
        result = Base.from_json_string(json_string)
        json_string.assertEqual(result, [{'key1': 'value1', 'key2': 'value2'}])

class test_load_from_file(unittest.TestCase):
    """Testing the load_from_file from Base class"""

    def test_load_from_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 9)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
