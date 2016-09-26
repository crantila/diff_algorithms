#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

result = timeit(
    stmt="implementations.recursive('human', 'chimpanzee')",
    setup='import implementations',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))

# CPython 2.7 for 25 times
# - 0.604655981064
# - 0.615916013718
# - 0.620596885681
