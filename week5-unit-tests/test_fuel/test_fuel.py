from fuel import convert, gauge
import pytest

def test_convert_no_errors():
    assert convert("5/5") == 100
    assert convert("0/4") == 0
    assert convert("1/4") == 25

def test_errors_convert():
    with pytest.raises(ValueError):
        convert("10/5")
        convert("7.8/9")
        convert("7/8.9")
        convert("-7/8")
        convert("2/-4")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
