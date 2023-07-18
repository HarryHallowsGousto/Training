import pytest
from src.main import odd_or_even


# RED GREEN REFACTOR
def test_4_input_even_case():
    # Arrange
    even_input = 4

    # Act
    output = odd_or_even(even_input)

    # Assert
    assert output == "even"


def test_22_input_even_case():
    # Arrange
    even_input = 22

    # Act
    output = odd_or_even(even_input)

    # Assert
    assert output == "even"


def test_1_input_odd_case():
    # Arrange
    odd_input = 1

    # Act
    output = odd_or_even(odd_input)

    # Assert
    assert output == "odd"


def test_dividable_by_3_and_even():
    # Arrange
    input = 6

    # Act
    output = odd_or_even(input)

    # Assert
    assert output == "three"


def test_dividable_by_3_and_odd():
    # Arrange
    input = 9

    # Act
    output = odd_or_even(input)

    # Assert
    assert output == "three"
