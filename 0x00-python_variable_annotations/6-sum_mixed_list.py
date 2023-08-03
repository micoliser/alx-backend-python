#!/usr/bin/env python3
""" This module contains a type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """ sums a list and returns the result """

    total = 0
    for num in mxd_list:
        total += num
    return total
