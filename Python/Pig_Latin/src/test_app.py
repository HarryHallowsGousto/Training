import pytest
from app import pig_it


def test_single_word():
    # arrange
    input_value = "Pig"
    expected_output = "Igpay"

    # act
    result = pig_it(input_value)

    # assert
    assert result == expected_output


def test_sentence():
    # arrange
    input_value = "Pig latin is cool."
    expected_output = "Igpay atinlay siay oolcay."

    # act
    result = pig_it(input_value)

    # assert
    assert result == expected_output


def test_sentences():
    # arrange
    input_value = "pig latin is cool. pig latin is cool"
    expected_output = "Igpay atinlay siay oolcay. Igpay atinlay siay oolcay."

    # act
    result = pig_it(input_value)

    # assert
    assert result == expected_output
