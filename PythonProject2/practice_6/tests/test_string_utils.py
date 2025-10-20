import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_utils import count_vowels


class TestStringUtils:
    """Тесты для функции подсчета гласных"""

    def test_count_vowels_simple_word(self):
        # Arrange
        text = "hello"
        expected = 2

        # Act
        result = count_vowels(text)

        # Assert
        assert result == expected

    def test_count_vowels_sentence(self):
        # Arrange
        text = "Python is awesome"
        expected = 6

        # Act
        result = count_vowels(text)

        # Assert
        assert result == expected

    def test_count_vowels_empty_string(self):
        # Arrange
        text = ""
        expected = 0

        # Act
        result = count_vowels(text)

        # Assert
        assert result == expected

    def test_count_vowels_uppercase(self):
        # Arrange
        text = "AEIOU"
        expected = 5

        # Act
        result = count_vowels(text)

        # Assert
        assert result == expected