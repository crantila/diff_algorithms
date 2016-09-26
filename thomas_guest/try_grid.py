#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

stmt = """DNA_LENGTH = 500
dna1 = [choice('ACGT') for _ in range(DNA_LENGTH)]
dna2 = [choice('ACGT') for _ in range(DNA_LENGTH)]
pure.lcs_grid(dna1, dna2)"""

result = timeit(
    stmt=stmt,
    setup='import pure; from random import choice',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 11.7696919441
# - 11.7794809341
# - 11.8586730957

# PyPy 5.0.1 for 25 times:
# - 5.71276402473
# - 5.67904400826
# - 6.1371948719
