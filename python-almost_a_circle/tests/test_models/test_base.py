#!/usr/bin/python3
"""Unittest for Base case"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    def __init__(self, value):
        # Initializing self
        self.value = value

    def print_value(self):
        # Self refers to the instance of MyClass
        print(f"The value is {self.value}")

    def test_create_instance(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 5)

    def test_to_json_string(self):
        # Test w/ an empty list of dicitonaries
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

        # Test w/ a list of dicitonaries
        data = [{'key1': 'value1', 'key2': 'value2'}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key1": "value1", "key2": "value2"}]')

    def from_json_string(json_string):
        # Test w/ an empty JSON string
        result = Base.from_json_string('')
        json_string.assertEqual(result, [])

        # Test w/ a JSON string
        json_string = '[{"key1": "value1", "key2": "value2"}]'
        result = Base.from_json_string(json_string)
        json_string.assertEqual(result, [{'key1': 'value1', 'key2': 'value2'}])

    def test_create(self):
        # Test creating a Rectangle object
        dictionary = {'width': 10, 'height': 20}
        result = Base.create(**dictionary)

        # Test creating a Square object
        dictionary = {'size': 5}
        result = Base.create(**dictionary)
        self.assertIsInstance(result, Base)

    def test_load_from_file(self):
        # Test loading from non-exisiting file
        result = Base.load_from_file()
        self.assertEqual(result, [])

        # Test loading from an exisiting file w/ objcts
        base1 = Base()
        base2 = Base()
        Base.save_to_file([base1, base2])
        result = Base.load_from_file()
        self.assertEqual(len(result), 2)

    def test_create_with_invalid_arguments(self):
        # Test creating a Base instance eith a negative ID
        with self.assertRaisesRegex(TypeError):
            obj = Base("invalid_argument")

    def test_create_with_negative_id(self):
        # Test creating a Base instance with a negative ID
        with self.assertRaisesRegex(ValueError):
            obj = Base(-1)
