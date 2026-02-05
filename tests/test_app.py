from app import say_hello


def test_hello():
    assert say_hello("Bob1") == "Hello Bob"
