import pytest
import BinaryGap as test

class TestClass:

    def test_example1(self):
        assert test.solution(9) == 2
    
    def test_example2(self):
        assert test.solution(529) == 4

    def test_example3(self):
        assert test.solution(20) == 1

    def test_example4(self):
        assert test.solution(15) == 0

    def test_example5(self):
        assert test.solution(32) == 0

    def test_example6(self):
        assert test.solution(1041) == 5

    def test_example7(self):
        assert test.solution(2147483647) == 0