import pure
from random import choice

DNA_LENGTH = 1000

def base():
    return choice('ACGT')

dna1 = [base() for _ in range(DNA_LENGTH)]
dna2 = [base() for _ in range(DNA_LENGTH)]

pure.lcs_grid(dna1, dna2)

# when DNA_LENGTH = 10000
# CPython 2.7 made it to 14.9G memory in 4:40 before I killed it
# PyPy 5.0.1 made it to 14.9G memory in 1:50 before I killed it

# when DNA_LENGTH = 1000
# CPython 2.7: 2.96s, 2.91s, 2.89s
# PyPy 5.0.1: 1.2s, 1.09s, 1.08s
