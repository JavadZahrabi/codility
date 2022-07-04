
def solution (A, K):

    if len(A) == 0:
        return A

    K = K % len(A)

    if K > 0:
        return A[-K:] + A[:-K]

    else:
       return A


