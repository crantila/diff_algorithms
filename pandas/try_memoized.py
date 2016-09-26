#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

result = timeit(
    stmt="implementations.lcs_memoized('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA')",
    setup='import implementations',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 0.266017913818
# - 0.262498855591
# - 0.256153821945
