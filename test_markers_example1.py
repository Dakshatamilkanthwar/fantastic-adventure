import pytest
class ClassTest:
    @pytest.mark.xfail
    @pytest.mark.great
    def test_greater(self,num):
        """This will check value is greater than 100"""
        self.num = 100
        assert self.num > 100

    @pytest.mark.xfail
    @pytest.mark.great
    def test_greater_equal(self):
        """This will check value is greater than 100"""
        self.num = 100
        assert self.num >= 100

    @pytest.mark.skip
    @pytest.mark.others
    def test_less(self,num):
        """This will check value is greater than 100"""
        self.num = 100
        assert self.num < 200
