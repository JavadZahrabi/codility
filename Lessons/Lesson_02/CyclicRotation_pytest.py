import pytest
import random
import CyclicRotation as test

ARRAY_RANGE = (-1000, 1000)
K_RANGE = (0, 100)
N_RANGE = (0, 100)

class TestClass:
    def test_example1(self):
        assert test.solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    def test_example2(self):
        assert test.solution([3, 8, 9, 7, 6], 4) == [8, 9, 7, 6, 3]

    def test_example3(self):
        assert test.solution([0, 0, 0], 1) == [0, 0, 0]

    def test_example3(self):
        assert test.solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]

    def test_example4(self):
        assert test.solution([], 2) == []

    def test_random(self):
        N = random.randint(*N_RANGE)
        K = random.randint(*K_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print (N, K, A)
        print (test.solution(A, K))

    