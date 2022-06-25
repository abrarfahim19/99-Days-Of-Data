from string_to_test import hello

def test_default():
    assert hello() == "Hello, World"


def test_value():
    assert hello("Abrar") == "Hello, Abrar"