#!/usr/bin/python3
""" Module for test Square class """
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    def test_instance(self):
        s = Square(2)
        self.assertIsInstance(s, Rectangle)

    def test_id(self):
        s = Square(2)
        s1 = Square(4, 0, 0, 67)
        s2 = Square(3)
        self.assertEqual(s.id, s2.id - 1)
        self.assertEqual(67, s1.id)
        s.id = 30
        self.assertEqual(30, s.id)

    def test_x(self):
        s = Square(2)
        s1 = Square(2, 1)
        self.assertEqual(0, s.x)
        self.assertEqual(1, s1.x)
        s.x = 3
        self.assertEqual(3, s.x)

    def test_y(self):
        s = Square(2)
        s1 = Square(2, 1, 5)
        self.assertEqual(0, s.y)
        self.assertEqual(5, s1.y)
        s.y = 6
        self.assertEqual(6, s.y)

    def test_size(self):
        s = Square(2)
        self.assertEqual(s.width, s.height)
        self.assertEqual(2, s.size)
        s.size = 20
        self.assertEqual(20, s.size)

    def test_square_with_no_args(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_square_with_many_args(self):
        with self.assertRaises(TypeError):
            s = Square(2, 2, 2, 20, 23, 34, 34)


class TestSquareAttrValidation(unittest.TestCase):
    def test_size_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("12")
            Square(2.3)
            Square((1, 2))
            Square([1, 2])
            Square({1, 2})
            Square({"a": 1, "b": 1})
            Square(None)
            Square(True)

    def test__size_less_than_1(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test__size_is_not_0(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_exceptions(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "12")
            Square(2, 2.3)
            Square(2, (1, 2))
            Square(2, [1, 2])
            Square(2, {1, 2})
            Square(2, {"a": 1, "b": 1})
            Square(2, None)
            Square(2, True)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)

    def test_y_exceptions(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, "12")
            Square(2, 2, 2.3)
            Square(2, 2, (1, 2))
            Square(2, 2, [1, 2])
            Square(2, 2, {1, 2})
            Square(2, 2, {"a": 1, "b": 1})
            Square(2, 2, None)
            Square(2, 2, True)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 2, -1)


class TestInheritedMethods(unittest.TestCase):
    def test_area(self):
        s = Square(2)
        s1 = Square(22, 2, 2, 30)
        self.assertEqual(4, s.area())
        self.assertEqual(484, s1.area())

    def test_area_with_extra_args(self):
        with self.assertRaises(TypeError):
            s = Square(2)
            s.area(1)

    def test_display_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s = Square(2)
            s.display()
            self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s = Square(2, 2)
            s.display()
            self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s = Square(2, 0, 2)
            s.display()
            self.assertEqual(f.getvalue(), "\n\n##\n##\n")

    def test_display_with_both_xy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s = Square(2, 2, 2)
            s.display()
            self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n")

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            s = Square(2)
            s.display(1)

    def test_str_representation(self):
        s = Square(2)
        output = "[Square] ({}) 0/0 - 2".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_str_with_xy(self):
        s = Square(2, 2, 2)
        output = "[Square] ({}) 2/2 - 2".format(s.id)
        self.assertEqual(output, s.__str__())

    def test_str_with_id(self):
        s = Square(2, 2, 2, 20)
        output = "[Square] (20) 2/2 - 2"
        self.assertEqual(output, s.__str__())

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            Square(2).__str__(1)


class TestUpdate(unittest.TestCase):
    def test_with_no_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        output = "[Square] (10) 10/10 - 10"
        self.assertEqual(output, s.__str__())

    def test_update_id(self):
        s = Square(10, 2, 3, 40)
        s.update(89)
        output = "[Square] (89) 2/3 - 10"
        self.assertEqual(output, s.__str__())

    def test_id_size(self):
        s = Square(10, 2, 3, 40)
        s.update(89, 15)
        output = "[Square] (89) 2/3 - 15"
        self.assertEqual(output, s.__str__())

    def test_with_all_args(self):
        s = Square(10, 2, 3, 40)
        s.update(89, 15, 5, 6)
        output = "[Square] (89) 5/6 - 15"
        self.assertEqual(output, s.__str__())

    def test_excess_args(self):
        s = Square(10, 2, 3, 40)
        s.update(89, 20, 5, 6, 80, 90, 100)
        output = "[Square] (89) 5/6 - 20"
        self.assertEqual(output, s.__str__())

    def test_with_kwargs_with_one_kwarg(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89)
        output = "[Square] (89) 10/10 - 10"
        self.assertEqual(output, s.__str__())
        s.update(x=1)
        output = "[Square] (89) 1/10 - 10"
        self.assertEqual(output, s.__str__())
        s.update(y=1)
        output = "[Square] (89) 1/1 - 10"
        self.assertEqual(output, s.__str__())
        s.update(size=1)
        output = "[Rectangle] (89) 1/1 - 1"


class TestSquareToDictionary(unittest.TestCase):
    """
    Test the to_dictionary method
    """
    def test_to_dict_output(self):
        s = Square(10, 2, 1, 10)
        output = {'id': 10, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(output, s.to_dictionary())

    def test_to_dictionary_with_update(self):
        s = Square(10, 2, 1, 10)
        s1 = Square(1, 1)
        s1.update(**s.to_dictionary())
        self.assertEqual(s.to_dictionary(), s1.to_dictionary())
        self.assertNotEqual(s, s1)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            s = Square(10, 2, 1, 9)
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
