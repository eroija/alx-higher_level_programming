#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class testRectangle(unittest.TestCase):
    """
    This are unittests to test a Rectangle instances
    """

    def test_id_assignment(self):

        """
        (test cases for ID assignment,
        similar to Base class tests)
        """

    def test_initialization(self):

        """Cases for correct initialization"""
        rect = Rectangle(5, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_width_setter_validation(self):

        rect = Rectangle(5, 4)

        with self.assertRaises(TypeError):
            rect.width = "invalid"
        with self.assertRaises(ValueError):
            rect.width = -2
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_area(self):
        rect = Rectangle(5, 4)
        self.assertEqual(rect.area(), 20)

    def test_display_small_rectangle(self, mock_print):
        rect = Rectangle(3, 2)
        rect.display()

        mock_print.assert_called_with("#" * 3)
        mock_print.assert_called_with("#" * 3)

    def test_display_larger_rectangle(self, mock_print):
        rect = Rectangle(10, 5)
        rect.display()

        for _ in range(5):
            mock_print.assert_called_with("#" * 10)

    def test_str_method(self):
        rect = Rectangle(5, 4, 2, 3)
        expected_str = "[Rectangle] (1) 2/3 - 5/4"
        self.assertEqual(str(rect), expected_str)

    def test_str_edge_cases(self):
        """Test with x, y, width, height at 0"""
        rect = Rectangle(0, 0, 0, 0)
        expected_str = "[Rectangle] (1) 0/0 - 0/0"
        self.assertEqual(str(rect), expected_str)

        """Test with large values"""
        rect = Rectangle(100, 200, 50, 75)
        expected_str = "[Rectangle] (2) 50/75 - 100/200"
        self.assertEqual(str(rect), expected_str)

    def test_display_with_x_and_y(self, mock_print):
        rect = Rectangle(3, 2, 4, 5)
        rect.display()

    def test_update_valid_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        rect.update(2, 10, 6, 7, 8)

        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

    def test_update_insufficient_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        with self.assertRaises(ValueError):
            rect.update(2, 10, 6)

    def test_update_excessive_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        with self.assertRaises(ValueError):
            rect.update(2, 10, 6, 7, 8, 9)

    def test_update_positional_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        rect.update(2, 10, 6, 7, 8)

    def test_update_keyword_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        rect.update(id=2, width=10, height=6, x=7, y=8)

    def test_update_mixed_arguments(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        with self.assertRaises(ValueError):
            rect.update(2, 10, 6, x=7, y=8)

    def test_update_invalid_keyword(self):
        rect = Rectangle(1, 5, 4, 2, 3)
        with self.assertRaises(ValueError):
            rect.update(invalid_key=10)

    def test_rectangle_instances(self):
        r = Rectangle(10, 2)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertTrue(isinstance(r1, Base))
        self.assertEqual(type(r), type(r))

    def test_id(self):
        r = Rectangle(3, 4)
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2)
        self.assertEqual(r.id, r2.id - 1)
        self.assertEqual(12, r1.id)

    def test_with_little_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(1)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 3)

    def test_private_attributes(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(10, 2)
            print(r.__width)
            print(r.__height)
            print(r.__x)
            print(r.__y)

    def test_valueerror(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_valueerror(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestSetterGetter(unittest.TestCase):
    """
    Tests a rectangles setter and getter methods
    """
    def test_get_width(self):
        r = Rectangle(5, 2)
        self.assertEqual(5, r.width)

    def test_set_width(self):
        r = Rectangle(5, 2)
        r.width = 7
        self.assertEqual(7, r.width)

    def test_get_height(self):
        r = Rectangle(5, 2)
        self.assertEqual(2, r.height)

    def test_set_height(self):
        r = Rectangle(5, 2)
        r.height = 7
        self.assertEqual(7, r.height)

    def test_get_x(self):
        r = Rectangle(5, 2, 9)
        self.assertEqual(9, r.x)

    def test_set_x(self):
        r = Rectangle(5, 2, 9, 8)
        r.x = 7
        self.assertEqual(7, r.x)

    def test_set_y(self):
        r = Rectangle(5, 2, 9, 8)
        self.assertEqual(8, r.y)

    def test_set_y(self):
        r = Rectangle(5, 2, 9, 8)
        r.y = 70
        self.assertEqual(70, r.y)

    def test_width_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
            Rectangle("12", 2)
            Rectangle(2.2, 2)
            Rectangle([1, 2], 2)
            Rectangle({"a": 1, "b": 2}, 2)
            Rectangle((1, 2), 2)
            Rectangle({1, 2}, 2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
            Rectangle(0, 2)

    def test_height_exception(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
            Rectangle(2, "12")
            Rectangle(2, 2.2)
            Rectangle(2, [1, 2])
            Rectangle(2, {'a': 1, 'b': 2})
            Rectangle(2, (1, 2))
            Rectangle(2, {1, 2})
            Rectangle(2, True)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
            Rectangle(2, 0)

    def test_x_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, None)
            Rectangle(2, 4, "12")
            Rectangle(2, 5, 2.2)
            Rectangle(2, 5, [1, 2])
            Rectangle(2, 5, {'a': 1, 'b': 2})
            Rectangle(2, 5, (1, 2))
            Rectangle(2, 5, {1, 2})
            Rectangle(2, 5, True)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 5, -2)

    def test_y_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 4, None)
            Rectangle(2, 4, 4, "12")
            Rectangle(2, 5, 4, 2.2)
            Rectangle(2, 5, 4, [1, 2])
            Rectangle(2, 5, 4, {'a': 1, 'b': 2})
            Rectangle(2, 5, 4, (1, 2))
            Rectangle(2, 5, 4, {1, 2})
            Rectangle(2, 5, 4, True)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 5, 3, -2)


class TestaAreaDisplay(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 2)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(6, r.area())
        self.assertEqual(56, r2.area())

    def test_big_number_area(self):
        r = Rectangle(5555555, 5555555)
        self.assertEqual(30864191358025, r.area())

    def test_area_with_changed_attributes(self):
        r = Rectangle(3, 2)
        r.width = 10
        r.height = 5
        self.assertEqual(50, r.area())

    def test_exception_with_extra_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.area(1)

    def test_display_to_stdout(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(3, 2)
            r.display()
            self.assertEqual(f.getvalue(), "###\n###\n")

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.display(1)

    def test_str_representation(self):
        r = Rectangle(3, 2)
        expected_out = "[Rectangle] ({}) 0/0 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_x(self):
        r = Rectangle(3, 2, 5)
        expected_out = "[Rectangle] ({}) 5/0 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_xy(self):
        r = Rectangle(3, 2, 5, 6)
        expected_out = "[Rectangle] ({}) 5/6 - 3/2".format(r.id)
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_id(self):
        r = Rectangle(2, 5, 3, 2, 12)
        expected_out = "[Rectangle] (12) 3/2 - 2/5"
        self.assertEqual(expected_out, r.__str__())

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.__str__(1)

    def test_display_with_x(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(2, 2, 2)
            output = "  ##\n  ##\n"
            r.display()
            self.assertEqual(f.getvalue(), output)

    def test_display_with_y(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(2, 2, 0, 2)
            output = "\n\n##\n##\n"
            r.display()
            self.assertEqual(f.getvalue(), output)

    def test_display_with_both_xy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(3, 2, 2, 2)
            output = "\n\n  ###\n  ###\n"
            r.display()
            self.assertEqual(f.getvalue(), output)


class TestUpdate(unittest.TestCase):
    def test_with_no_args(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update()
        output = "[Rectangle] (40) 2/3 - 5/10"
        self.assertEqual(output, r.__str__())

    def test_update_id(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update(89)
        output = "[Rectangle] (89) 2/3 - 5/10"
        self.assertEqual(output, r.__str__())

    def test_id_width(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update(89, 15)
        output = "[Rectangle] (89) 2/3 - 15/10"
        self.assertEqual(output, r.__str__())

    def test_id_width_height(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update(89, 15, 20)
        output = "[Rectangle] (89) 2/3 - 15/20"
        self.assertEqual(output, r.__str__())

    def test_with_all_args(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update(89, 15, 20, 5, 6)
        output = "[Rectangle] (89) 5/6 - 15/20"
        self.assertEqual(output, r.__str__())

    def test_excess_args(self):
        r = Rectangle(5, 10, 2, 3, 40)
        r.update(89, 15, 20, 5, 6, 80, 90, 100)
        output = "[Rectangle] (89) 5/6 - 15/20"
        self.assertEqual(output, r.__str__())

    def test_with_kwargs_with_one_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89)
        output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(output, r.__str__())
        r.update(x=1)
        output = "[Rectangle] (89) 1/10 - 10/10"
        self.assertEqual(output, r.__str__())
        r.update(y=1)
        output = "[Rectangle] (89) 1/1 - 10/10"
        self.assertEqual(output, r.__str__())
        r.update(width=1)
        output = "[Rectangle] (89) 1/1 - 1/10"
        self.assertEqual(output, r.__str__())
        r.update(height=1)
        output = "[Rectangle] (89) 1/1 - 1/1"
        self.assertEqual(output, r.__str__())

    def test_kwargs_with_partial_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, height=1, id=89)
        output = "[Rectangle] (89) 10/10 - 1/1"
        self.assertEqual(output, r.__str__())
        r.update(x=1, y=1)
        output = "[Rectangle] (89) 1/1 - 1/1"
        self.assertEqual(output, r.__str__())

    def test_with_all_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, height=1, x=1, y=1, id=89)
        output = "[Rectangle] (89) 1/1 - 1/1"
        self.assertEqual(output, r.__str__())

    def test_with_excess_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, height=1, x=1, y=1, id=89, z=1)
        output = "[Rectangle] (89) 1/1 - 1/1"
        self.assertEqual(output, r.__str__())

    def test_kwargs_and_ags(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, id=89, width=1)
        output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(output, r.__str__())

    def test_kwargs_with_key_that_dont_exist(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(z=1)
        output = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(output, r.__str__())


class TestRectToDict(unittest.TestCase):
    """
    Test the to_dict method
    """
    def test_to_dict_output(self):
        r = Rectangle(10, 2, 1, 9, 10)
        output = {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10}
        self.assertEqual(output, r.to_dictionary())

    def test_to_dictionary_with_update(self):
        r = Rectangle(10, 2, 1, 9, 10)
        r1 = Rectangle(1, 1)
        r1.update(**r.to_dictionary())
        self.assertEqual(r.to_dictionary(), r1.to_dictionary())
        self.assertNotEqual(r, r1)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, 9)
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
