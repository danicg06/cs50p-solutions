from plates import is_valid

def test_first_two_letters():
    assert is_valid("hG304") == True
    assert is_valid("G603") == False
    assert is_valid("603") == False

def test_characters_num():
    assert is_valid("htt800000") == False
    assert is_valid("tT") == True
    assert is_valid("tttddw") == True

def test_numbers_position():
    assert is_valid("Tt666") == True
    assert is_valid("5555") == False
    assert is_valid("tt66tt") == False
    assert is_valid("tt00") == False

def test_no_punctuation_spaces():
    assert is_valid("dada") == True
    assert is_valid("fre 66") == False
    assert is_valid("fr...3") == False
    assert is_valid("TT 54") == False

