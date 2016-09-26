#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

stmt = """DNA_LENGTH = 500
dna1 = [choice('ACGT') for _ in range(DNA_LENGTH)]
dna2 = [choice('ACGT') for _ in range(DNA_LENGTH)]
pure.lcs_hirschberg(dna1, dna2)"""

result = timeit(
    stmt=stmt,
    setup='import pure; from random import choice',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 4.8526699543
# - 4.80305504799
# - 4.98720383644

# PyPy 5.0.1 for 25 times:
# - 0.699461221695
# - 0.418462991714
# - 0.423987865448
