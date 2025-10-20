import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from number_utils import is_even


class TestNumberUtils:
    """Тесты для функции проверки четности"""

    def test_is_even_even_number(self):
        # Arrange
        number = 4
        expected = True

        # Act
        result = is_even(number)

        # Assert
        assert result == expected

    def test_is_even_odd_number(self):
        # Arrange
        number = 7
        expected = False

        # Act
        result = is_even(number)

        # Assert
        assert result == expected

    def test_is_even_zero(self):
        # Arrange
        number = 0
        expected = True

        # Act
        result = is_even(number)

        # Assert
        assert result == expected

    def test_is_even_string_raises_type_error(self):
        # Arrange
        number = "string"

        # Act & Assert
        with pytest.raises(TypeError):
            is_even(number)