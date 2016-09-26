#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Algorithms with pandas.

Written in Python 2 so both CPython and PyPy will work.
'''
from collections import namedtuple, defaultdict
from itertools import product
import pandas


def recursive(xs, ys):
    """
    Return a longest common subsequence of xs and ys.

    Example:
    >>> recursive("HUMAN", "CHIMPANZEE")
    ['H', 'M', 'A', 'N']
    """
    xs = pandas.Series(list(xs))
    ys = pandas.Series(list(ys))

    def lcs_(xi, yi):
        """
        Arguments are the last index of the strings to be matching against. Start with the final
        character in the strings; lcs_() moves itself to the start.

        The return value is the LCS characters in a list.
        """
        if xi > -1 and yi > -1:
            xb = xi - 1
            yb = yi - 1
            if xs.iat[xi] == ys.iat[yi]:
                return lcs_(xb, yb) + [xs.iat[xi]]
            else:
                return max(lcs_(xi, yb), lcs_(xb, yi), key=len)
        else:
            return []

    return lcs_(len(xs) - 1, len(ys) - 1)


def _memoize(fn):
    '''
    Return a memoized version of the input function.

    The returned function caches the results of previous calls.
    Useful if a function call is expensive, and the function
    is called repeatedly with the same arguments.
    '''
    cache = dict()
    def wrapped(*v):
        key = tuple(v) # tuples are hashable, and can be used as dict keys
        if key not in cache:
            cache[key] = fn(*v)
        return cache[key]
    return wrapped


def lcs_memoized(xs, ys):
    """
    Memoized version of recursive().
    """
    xs = pandas.Series(list(xs))
    ys = pandas.Series(list(ys))

    @_memoize
    def lcs_(xi, yi):
        """
        Arguments are the last index of the strings to be matching against. Start with the final
        character in the strings; lcs_() moves itself to the start.

        The return value is the LCS characters in a list.
        """
        if xi > -1 and yi > -1:
            xb = xi - 1
            yb = yi - 1
            if xs.iat[xi] == ys.iat[yi]:
                return lcs_(xb, yb) + [xs.iat[xi]]
            else:
                return max(lcs_(xi, yb), lcs_(xb, yi), key=len)
        else:
            return []

    return lcs_(len(xs) - 1, len(ys) - 1)


def make_lcs_grid(xs, ys):
    """
    Create a grid for longest common subsequence calculations.

    Returns a grid where grid[(j, i)] is a pair (n, move) such that
    - n is the length of the LCS of prefixes xs[:i], ys[:j]
    - move is \, ^, <, or e, depending on whether the best move
      to (j, i) was diagonal, downwards, or rightwards, or None.

    Example:
       T  A  R  O  T
    A 0< 1\ 1< 1< 1<
    R 0< 1^ 2\ 2< 2<
    T 1\ 1< 2^ 2< 3\

    NOTE: for the directions, this function uses:
    - 1 instead of '\\'
    - 2 instead of '^'
    - 3 instead of '<'
    """
    grid_length = pandas.DataFrame({j: pandas.Series([None for _ in xrange(len(xs))]) for j in xrange(len(ys))})
    grid_move = pandas.DataFrame({j: pandas.Series([None for _ in xrange(len(xs))]) for j in xrange(len(ys))})
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:
        new_length = None
        new_move = None
        if x == y:
            new_length = grid_length.iat[i-1, j-1] + 1 if (i > 0 and j > 0) else 1
            new_move = 1
        else:
            left = grid_length.iat[i-1, j] if i > 0 else 0
            over = grid_length.iat[i, j-1] if j > 0 else 0
            if left < over:
                new_length = over
                new_move = 2
            else:
                new_length = left
                new_move = 3
        grid_length.iat[i, j] = new_length
        grid_move.iat[i, j] = new_move

    # the length isn't important to lcs_grid()
    return grid_move


def lcs_grid(xs, ys):
    """
    Use the bottom-up algorithm.
    """
    # Create the LCS grid, then walk back from the bottom right corner
    grid = make_lcs_grid(xs, ys)
    i, j = len(xs) - 1, len(ys) - 1
    lcs = list()
    for move in iter(lambda: grid.iat[i, j] if (i >= 0 and j >= 0) else None, None):
        if move == 1:
            lcs.append(xs[i])
            i -= 1
            j -= 1
        elif move == 2:
            j -= 1
        elif move == 3:
            i -= 1
    lcs.reverse()
    return lcs


def lcs_hirschberg(*args, **kwargs):
    raise NotImplementedError("It's just going to be slower than pure Python; why bother?")
