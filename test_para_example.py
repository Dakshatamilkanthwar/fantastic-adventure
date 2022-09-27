import pytest

@pytest.mark.parametrize("num",(15,20,80))
def test_divisible_by_5(num):
    """This is checking divisible by 5"""
    assert num%5 == 0,"it is not divisible by 5"

@pytest.mark.parametrize("num",(11,20,72))
def test_divisible_by_5(num):
    """This is checking divisible by 5"""
    assert num%5 == 0,"it is not divisible by 5"