#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_new = tuple_a + (0, 0)
    tuple_b_new = tuple_b + (0, 0)
    sum0 = tuple_a_new[0] + tuple_b_new[0]
    sum1 = tuple_a_new[1] + tuple_b_new[1]
    return sum0, sum1
