#!/usr/bin/python3
""" test_base module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class BaseTestCase(unittest.TestCase):
    """
    Run unittests to test Base class
    """
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(20)

    def test_base_instance(self):
        """
        test instances of base
        """
        self.assertEqual(Base, type(self.b1))
        self.assertEqual(Base, type(self.b2))
        self.assertEqual(type(self.b1), type(self.b2))

    def test_nb_instance(self):
        """
        test that nb_instance attr is private
        """
        with self.assertRaises(AttributeError):
            print(self.b1.__nb_instances)
            print(self.b2.__nb_instances)

    def test_id_after_nb_instance(self):
        """
        tests id value after passing a value
        """
        b3 = Base()
        self.assertEqual(self.b1.id, b3.id - 1)
        self.assertEqual(20, self.b2.id)

    def test_id_int(self):
        """
        test id with integers and None
        """
        b3 = Base(None)
        self.assertEqual(self.b1.id, b3.id - 1)
        self.b1.id = 15
        self.assertEqual(15, self.b1.id)
        self.b2.id = 15
        self.assertEqual(15, self.b2.id)

    def test_id_str(self):
        """
        test id with strings
        """
        b3 = Base("Ted")
        self.assertEqual('Ted', b3.id)
        self.b1.id = "Ted"
        self.assertEqual(self.b1.id, b3.id)

    def test_id_data_types(self):
        """
        test id with different data structures
        """
        b_list = Base([1, 2])
        b_dict = Base({"one": 1, "two": 2})
        b_tuple = Base((1, 2))
        b_set = Base({1, 2})
        self.assertEqual([1, 2], b_list.id)
        self.assertEqual({"one": 1, "two": 2}, b_dict.id)
        self.assertEqual((1, 2), b_tuple.id)
        self.assertEqual({1, 2}, b_set.id)

    def test_id_bool(self):
        """
        test instances with boolean values
        """
        b_true = Base(True)
        b_false = Base(False)
        self.assertTrue(b_true.id)
        self.assertFalse(b_false.id)

    def test_multiple_args(self):
        """
        Check if typeerror will be raised when we have
        excess arguments
        """
        with self.assertRaises(TypeError):
            b = Base(12, 10)


class TestToJsonString(unittest.TestCase):
    """
    Test to the to json string method
    """
    def test_to_json_string_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        self.assertIsInstance(Base.to_json_string([r.to_dictionary()]), str)

    def test_to_json_with_many_args_rectangle(self):
        r = Rectangle(1, 2, 5, 2, 12)
        r1 = Rectangle(1, 2, 5, 2, 12)
        r2 = Rectangle(1, 2, 5, 2, 12)
        list_dict = [r.to_dictionary(), r1.to_dictionary(), r2.to_dictionary()]
        self.assertIsInstance(Base.to_json_string(list_dict), str)

    def test_to_json_string_Square(self):
        s = Square(10, 7, 2, 8)
        self.assertIsInstance(Base.to_json_string([s.to_dictionary()]), str)

    def test_to_json_with_many_args_square(self):
        s = Square(1, 2, 5, 12)
        s1 = Square(1, 5, 2, 12)
        s2 = Square(2, 5, 2, 12)
        list_dict = [s.to_dictionary(), s1.to_dictionary(), s2.to_dictionary()]
        self.assertIsInstance(Base.to_json_string(list_dict), str)

    def test_with_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_with_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_with_excess_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestSaveToJson(unittest.TestCase):
    @classmethod
    def teardown(self):
        list_files = ["Rectangle.json", "Square.json", "Base.json"]
        for file in list_files:
            if os.path.exists(file):
                os.remove(file)

    def test_save_to_file_rectangle(self):
        r = Rectangle(7, 5, 4, 3, 9)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 52)

    def test_save_to_file__multiple_rectangle(self):
        r = Rectangle(7, 5, 4, 3, 9)
        r2 = Rectangle(2, 3, 4, 2, 5)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 104)

    def test_save_to_file_Square(self):
        s = Square(7, 5, 4, 3)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_multiple_Square(self):
        s = Square(7, 5, 4, 3)
        s2 = Square(10, 5, 4, 3)
        Square.save_to_file([s, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_ovewrite(self):
        s = Square(7, 5, 4, 3)
        Square.save_to_file([s])
        s2 = Square(10, 5, 4, 3)
        Square.save_to_file([s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_with_many_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])


class TestFromJsonString(unittest.TestCase):
    def test_from_json_string_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_output = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_output)
        self.assertIsInstance(list_output, list)

    def test_from_json_string_rectangle(self):
        list_input = [{'id': 89, 'size': 2}]
        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)
        self.assertIsInstance(list_output, list)

    def test_with_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_with_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_with_excess_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestCreate(unittest.TestCase):
    def test_create_type_rectangle(self):
        r = Rectangle(3, 5, 1)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertIsInstance(r1, Rectangle)
        self.assertNotIsInstance(r1, Square)

    def test_create_rectangle(self):
        r = Rectangle(3, 5, 1)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertEqual(str(r), str(r1))

    def test_create_rectangle_equal(self):
        r = Rectangle(3, 5, 1)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r1)

    def test_if_creates_the_same_object(self):
        r = Rectangle(3, 5, 1)
        r_dictionary = r.to_dictionary()
        r1 = Rectangle.create(**r_dictionary)
        self.assertIsNot(str(r), str(r1))

    def test_create_type_square(self):
        s = Square(3, 2)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertIsInstance(s1, Square)

    def test_create_square(self):
        s = Square(3, 2)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertEqual(str(s), str(s1))

    def test_create_square_equal(self):
        s = Square(3, 2)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertNotEqual(s, s1)

    def test_create_square_not_same_type(self):
        s = Square(3, 2)
        s_dictionary = s.to_dictionary()
        s1 = Square.create(**s_dictionary)
        self.assertIsNot(s, s1)

    def test_create_exception(self):
        with self.assertRaises(TypeError):
            s = Square(3)
            s_dictionary = s.to_dictionary()
            s1 = Square.create(s_dictionary)
            s2 = Square.create()
            s3 = Square.create(2, **s_dictionary)


class TestLoadFromFile(unittest.TestCase):
    @classmethod
    def teardown(self):
        list_files = ["Rectangle.json", "Square.json", "Base.json"]
        for file in list_files:
            if os.path.exists(file):
                os.remove(file)

    def test_load_from_file_rectangle(self):
        r = Rectangle(10, 4)
        r1 = Rectangle(23, 34, 10)
        list_rect_input = [r, r1]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        for i, rect in enumerate(list_rect_output):
            with self.subTest(rect=rect):
                self.assertEqual(str(list_rect_input[i]), str(rect))
                self.assertIsInstance(rect, Rectangle)
                self.assertIsNot(rect, list_rect_input[i])

    def test_load_from_file_square(self):
        s = Square(10)
        s1 = Square(23, 34, 10)
        list_square_input = [s, s1]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        for i, square in enumerate(list_square_output):
            with self.subTest(square=square):
                self.assertEqual(str(list_square_input[i]), str(square))
                self.assertIsInstance(square, Square)
                self.assertIsNot(square, list_square_input[i])

    def test_exeptions(self):
        with self.assertRaises(TypeError):
            Square.load_from_file(12)


if __name__ == '__main__':
    unittest.main()
