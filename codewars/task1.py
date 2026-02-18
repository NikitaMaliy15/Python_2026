"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string."""

a = int(input())
b = ''

while a > 0:
    b = str(a % 2) + b
    a = a // 2

    print(b)