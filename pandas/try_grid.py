#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

stmt = """DNA_LENGTH = 500
dna1 = [choice('ACGT') for _ in range(DNA_LENGTH)]
dna2 = [choice('ACGT') for _ in range(DNA_LENGTH)]
implementations.lcs_grid(dna1, dna2)"""

result = timeit(
    stmt=stmt,
    setup='import implementations; from random import choice',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 290.020524025
# - ?
# - ?
