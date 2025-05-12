##
## Filename: fibonacci_n.py
## Description: The fibonacci series is a sequence of number where each number is the sum of the two precending ones starting with 0 and 1
##              
## Date : 12/05/2025
## 
##  Copyright by Muppala Anilkumar @2025
## 
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)
fib(7)                