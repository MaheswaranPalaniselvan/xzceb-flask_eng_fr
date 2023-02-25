import pytest
import translator

@pytest.mark.parametrize("input, expected", [("", ""), ("Hello", "Bonjour")])
def test_english_to_french(input, expected):
    assert translator.english_to_french(input) == expected

@pytest.mark.parametrize("input, expected", [("", ""), ("Bonjour", "Hello")])
def test_french_to_english(input, expected):
    assert translator.french_to_english(input) == expected

