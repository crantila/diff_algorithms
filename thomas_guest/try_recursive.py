#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from timeit import timeit

NUMBER = 25

result = timeit(
    stmt="pure.lcs('human', 'chimpanzee')",
    setup='import pure',
    number=NUMBER,
)

print('Running the diff {num} times took {res} seconds.'.format(num=NUMBER, res=result))


# CPython 2.7 for 25 times:
# - 0.0337059497833
# - 0.0326609611511
# - 0.0325479507446

# PyPy 5.0.1 for 25 times:
# - 0.0409848690033
# - 0.0406219959259
# - 0.0398030281067
