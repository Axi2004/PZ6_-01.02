import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import add


class TestCalculator:
    """Тесты для функции сложения"""

    def test_add_positive_numbers(self):
        # Arrange
        a, b = 2, 3
        expected = 5

        # Act
        result = add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        # Arrange
        a, b = -1, 1
        expected = 0

        # Act
        result = add(a, b)

        # Assert
        assert result == expected

    def test_add_zeros(self):
        # Arrange
        a, b = 0, 0
        expected = 0

        # Act
        result = add(a, b)

        # Assert
        assert result == expected

    def test_add_strings_raises_type_error(self):
        # Arrange
        a, b = "a", "b"

        # Act & Assert
        with pytest.raises(TypeError):
            add(a, b)