import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def k_name():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_str(k_name):
    assert str(k_name) == "Dark Project KD87A"
    assert str(k_name.language) == "EN"


def test_repr(k_name):
    assert repr(k_name) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_change_lang(k_name):
    k_name.change_lang()
    assert str(k_name.language) == "RU"
    k_name.change_lang().change_lang()
    assert str(k_name.language) == "RU"
