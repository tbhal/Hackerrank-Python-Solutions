# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 11:06:02 2017

@author: tushar
"""


def karatsuba(x, y):
    if (len(str(x)) == 1 or len(str(y)) == 1):
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2
        a = x // 10 ** (nby2)
        b = x % 10 ** (nby2)
        c = y // 10 ** (nby2)
        d = y % 10 ** (nby2)
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        adPlusbc = karatsuba(a + b, c + d) - ac - bd
        prod = ac * 10 ** (2 * nby2) + (adPlusbc) * 10 ** (nby2) + bd

        return prod


c = karatsuba(1234,12)
print(c)
