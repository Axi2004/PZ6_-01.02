import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from list_utils import find_max


class TestListUtils:
    """Тесты для функции поиска максимального числа"""

    def test_find_max_positive_numbers(self):
        # Arrange
        numbers = [1, 2, 3]
        expected = 3

        # Act
        result = find_max(numbers)

        # Assert
        assert result == expected

    def test_find_max_negative_numbers(self):
        # Arrange
        numbers = [-5, -2, -10]
        expected = -2

        # Act
        result = find_max(numbers)

        # Assert
        assert result == expected

    def test_find_max_empty_list_raises_value_error(self):
        # Arrange
        numbers = []

        # Act & Assert
        with pytest.raises(ValueError):
            find_max(numbers)

    def test_find_max_mixed_types_raises_type_error(self):
        # Arrange
        numbers = [1, 2, "3"]

        # Act & Assert
        with pytest.raises(TypeError):
            find_max(numbers)