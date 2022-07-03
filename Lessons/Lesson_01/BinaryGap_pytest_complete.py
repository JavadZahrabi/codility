import pytest

MAXINT = 2147483647

def solution(N):
    
    if not isinstance(N, int):
        raise TypeError("Input must be an Integer")
    
    if N < 1:
        raise ValueError("Input must be a positive Integer")

    if N > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")
    
    binary_string = str(bin(N))[2:]
    max_count = None
    this_count = 0
    was_zero = None

    for bit in binary_string:
        is_zero = bit == '0'

        if bool(was_zero) != bool(is_zero):
            if max_count is None:
                max_count = 0
            elif this_count > max_count:
                max_count = this_count
            this_count = 1
        else:
            this_count += 1

        was_zero = is_zero
    
    if max_count is not None:
        return max_count
    else:
        return 0

"""
N = int(input ("Enter a positive integer number:"))
result = solution(N)
print(result)
"""
class TestClass:
    def test_example1(self):
        assert solution(9) == 2
    
    def test_example2(self):
        assert solution(529) == 4

    def test_example3(self):
        assert solution(20) == 1

    def test_example4(self):
        assert solution(15) == 0

    def test_example5(self):
        assert solution(32) == 0

    def test_example6(self):
        assert solution(1041) == 5

    def test_example7(self):
        assert solution(2147483647) == 0

if __name__ == '__main__':
    pytest.main()