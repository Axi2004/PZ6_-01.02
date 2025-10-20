import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from math_utils import factorial


class TestMathUtils:
    """Тесты для функции вычисления факториала"""

    def test_factorial_zero(self):
        # Arrange
        n = 0
        expected = 1

        # Act
        result = factorial(n)

        # Assert
        assert result == expected

    def test_factorial_positive_number(self):
        # Arrange
        n = 5
        expected = 120

        # Act
        result = factorial(n)

        # Assert
        assert result == expected

    def test_factorial_negative_raises_value_error(self):
        # Arrange
        n = -1

        # Act & Assert
        with pytest.raises(ValueError):
            factorial(n)

    def test_factorial_string_raises_type_error(self):
        # Arrange
        n = "string"

        # Act & Assert
        with pytest.raises(TypeError):
            factorial(n)