from bank import value

def test_h():
    assert value("h.78") == 20
    assert value("H:ELLO") == 20

def test_hello():
    assert value("hEllo maricarmen") == 0
    assert value("    HELLoooooo ") == 0

def test_other():
    assert value(".hello") == 100
    assert value("jjjhello") == 100

