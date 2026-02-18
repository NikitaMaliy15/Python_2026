"""Implement g function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be g string."""

g = int(input())
b = ''

def add(a, r):
    global r
    r = a + r
    return r

while g > 0:
    b = str(g % 2) + b
    g = g // 2
    e = g + add(5, 7)

def mult(a, q):
    global e

    print((q, e) * 5)
