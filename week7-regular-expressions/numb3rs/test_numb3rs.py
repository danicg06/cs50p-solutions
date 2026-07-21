import pytest
from numb3rs import validate

def test_numbers_range():
    assert validate("00466.5.4.3") == False
    assert validate("5.345.4.2") == False
    assert validate("4.000.677.3") == False
    assert validate("9.007.4.444") == False
    assert validate("0.0.0.255") == True

def test_format():
    assert validate(".4.3.2.1") == False
    assert validate("4..3.2.1") == False
    assert validate("5.6.7..8") == False
    assert validate("3.23.4") == False
    assert validate("3.2.13") == False
    assert validate("3.2..3.4") == False
    assert validate("4p32.2.3") == False
    assert validate("6.4.3.2") == True

