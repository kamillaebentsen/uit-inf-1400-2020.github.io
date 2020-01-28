# Program: gcd.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
# Edit: Minor modifications for Python 3 + pep8


def gcd(u, v):
    r = u % v
    while r != 0:
        u = v
        v = r
        r = u % v
    return v
