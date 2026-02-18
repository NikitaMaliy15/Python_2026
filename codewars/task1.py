"""Implement g function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be g string."""

g = int(input())
b = ''

while g > 0:
    b = str(g % 2) + b
    g = g // 2

    print((b + g) * 5)