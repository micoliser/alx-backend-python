#!/usr/bin/env python3
""" This module contains a type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """ sums a list and returns the result """

    return sum(mxd_list)

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
