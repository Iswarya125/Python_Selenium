import pytest


@pytest.mark.xfail
def test_programcard():
    msg = "hello"
    assert msg == "hi","Failure in string matching"