#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

result = timeit(
    stmt="pure.lcs_memoized('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA')",
    setup='import pure',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 0.0297160148621
# - 0.0413601398468
# - 0.0220589637756

# PyPy 5.0.1 for 25 times:
# - 0.0660061836243
# - 0.0679309368134
# - 0.0687580108643
