import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from calculator import add


class TestCalculatorUnittest(unittest.TestCase):
    """Тесты для функции сложения с использованием unittest"""

    def test_add_positive_numbers(self):
        # Arrange
        a, b = 2, 3
        expected = 5

        # Act
        result = add(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_add_negative_numbers(self):
        # Arrange
        a, b = -1, 1
        expected = 0

        # Act
        result = add(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_add_zeros(self):
        # Arrange
        a, b = 0, 0
        expected = 0

        # Act
        result = add(a, b)

        # Assert
        self.assertEqual(result, expected)

    def test_add_strings_raises_type_error(self):
        # Arrange
        a, b = "a", "b"

        # Act & Assert
        with self.assertRaises(TypeError):
            add(a, b)


if __name__ == '__main__':
    unittest.main()