import pytest
from working import convert

def test_convert_valid():
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"
    assert convert("1:13 AM to 7:45 AM") == "01:13 to 07:45"
    assert convert("9 PM to 11 PM") == "21:00 to 23:00"
    assert convert("1:13 PM to 7:45 PM") == "13:13 to 19:45"
    assert convert("5:27 AM to 4:44 PM") == "05:27 to 16:44"
    assert convert("3:33 PM to 8:01 AM") == "15:33 to 08:01"

def test_convert_invalid_format():
    # Probamos específicamente la falta de " to "
    with pytest.raises(ValueError):
        convert("9 AM 10 AM")
    with pytest.raises(ValueError):
        convert("9:00 AM 10:00 AM")
    with pytest.raises(ValueError):
        convert("9 AM-10 AM")

def test_convert_invalid_times():
    # Probamos horas y minutos fuera de rango
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 AM")
    with pytest.raises(ValueError):
        convert("09:66 AM to 10:00 AM")
    with pytest.raises(ValueError):
        convert("00:45 PM to 5:00 AM")
    with pytest.raises(ValueError):
        convert("11:78 AM to 10:00 PM")
