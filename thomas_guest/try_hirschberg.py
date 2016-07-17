import pure
from random import choice

DNA_LENGTH = 10000

def base():
    return choice('ACGT')

dna1 = [base() for _ in range(DNA_LENGTH)]
dna2 = [base() for _ in range(DNA_LENGTH)]

pure.lcs_hirschberg(dna1, dna2)

# when DNA_LENGTH = 10000
# CPython 2.7: 68.25s, 69.18s, 68.45s
# PyPy 5.0.1: 3.75s, 3.73s, 3.79s

# when DNA_LENGTH = 1000
# CPython 2.7: 0.75s, 0.78s, 0.79s
# PyPy 5.0.1: 0.25s, 0.27s, 0.28s
