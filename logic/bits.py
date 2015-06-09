__author__ = 'percentcer'
# Chapter 5
# Bits
from math import log2
from math import floor

def insert_number(m, n, i, j):
    if (i - j + 1) < log2(m):
        raise ValueError("M doesn't fit in the given range!")
    elif floor(log2(m)) > floor(log2(n)):
        raise ValueError("M has more bits than N!")

    region = 0xffffffff
    region <<= i
    region >>= i
    region <<= j

    m_shifted = m
    m_shifted <<= j

    stamped = n & ~region
    incoming = 0xffffffff & m_shifted

    return stamped + incoming

def count_right_repeats(i, v):
    count = 0
    while i % 2 == v:
        count += 1
        i >>= 1
    return count

def shift_count_smaller(i):
    if i % 2 is 0:
        return count_right_repeats(i, 0) - 1
    else:
        return count_right_repeats(i, 1)

def shift_count_larger(i):
    if i % 2 is 1:
        return count_right_repeats(i, 1) - 1
    else:
        return count_right_repeats(i, 0)

def next_smallest_with_same_one_count(i):
    return i - (1 << shift_count_smaller(i))

def next_largest_with_same_one_count(i):
    return i + (1 << shift_count_larger(i))
