from twttr import shorten

def test_shorten_A():
    assert shorten("CATA") == "CT"
    assert shorten("nada") == "nd"


def test_shorten_E():
    assert shorten("PEPE") == "PP"
    assert shorten("12E") == "12"

def test_shorten_I():
    assert shorten("Lili") == "Ll"
    assert shorten("LELO") == "LL"

def test_shorten_O():
    assert shorten("cono") == "cn"
    assert shorten("COJO") == "CJ"

def test_shorten_U():
    assert shorten("TURURU") == "TRR"
    assert shorten("puru") == "pr"

def test_shorten_all():
    assert shorten("murcie.lago") == "mrc.lg"
    assert shorten("educacion") == "dccn"

