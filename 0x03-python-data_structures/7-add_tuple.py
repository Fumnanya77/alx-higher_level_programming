#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = tuple(map(sum, zip(tuple_a, tuple_b)))
    if len(tuple_a) >= 2 or len(tuple_b) >= 2:
        return tuple_c
