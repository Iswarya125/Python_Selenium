import pytest

@pytest.mark.smoke
def test_firstprogram():
    print("hello")

@pytest.mark.skip
def test_card():
    print("card program")