
import random
import CyclicRotation as test

ARRAY_RANGE = (-1000, 1000)
K_RANGE = (0, 100)
N_RANGE = (0, 100)

#run as function
def test_random():
    N = random.randint(*N_RANGE)
    K = random.randint(*K_RANGE)
    A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
    print (N, K, A)
    print (test.solution(A, K))

test_random()


#run as class method and needs 'self' as a parameter
"""
class TestClass:    
    def test_random(self):
        N = random.randint(*N_RANGE)
        K = random.randint(*K_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        print (N, K, A)
        print (test.solution(A, K))

javad = TestClass()
javad.test_random()

"""