
from tkinter import N




MAXINT = 2147483647

def solution(N):
    
    if not isinstance(N, int):
        raise TypeError("Input must be an Integer")
    
    if N < 1:
        raise ValueError("Input must be a positive Integer")

    if N > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")
    
    binary_string = str(bin(N))[2:]


N = input ("Enter a positive integer number:")
solution(N)