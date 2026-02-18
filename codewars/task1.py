"""Implement g function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be g string."""

g = int(input())
b = ''

def add(a, r):
    r = a + r
    return r

while g > 0:
    b = str(g % 2) + b
    g = g // 2
    e = g + add(5, 7)

def mult(a, q):
    a = a * q
    return a

q = mult(7, 9)
e = add(1, 2)

print(q,e)
