import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    """This will check value is greater than 100"""
    num = 100
    assert num > 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    """This will check value is greater than 100"""
    num = 100
    assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less():
    """This will check value is greater than 100"""
    num = 100
    assert num < 200