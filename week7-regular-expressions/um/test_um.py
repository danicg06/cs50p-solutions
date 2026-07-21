import pytest
from um import count

def test_no_whitespaces():
    assert count("UM,um,Um") == 3
    assert count("um.Um:um,um") == 4
    assert count("Umda,um,uma") == 1

def test_um_in_words():
    assert count("um, umamaum") == 1
    assert count("umauma") == 0
    assert count("Hello, um, yummy") == 1

def test_start_end_um():
    assert count("Um, mama, um") == 2
    assert count("umama, um") == 1
    assert count("Um, umaum") == 1
    assert count("Um, umama, um") == 2
