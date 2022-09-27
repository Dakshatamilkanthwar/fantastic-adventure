import pytest
import random

@pytest.fixture
def test_random_list():
    """ This testcase used to create random 5 numbers"""
    num = []
    for i in range(0,5):
        n = random.randint(1,30)
        num.append(n)
        return num

def test_disible_by_2(test_random_list):
    """ This testcase used to check it is divisible by 2 """
    for i in range(len(test_random_list)):
        assert test_random_list[i]%2 == 0,"number is not even"