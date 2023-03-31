#!/usr/bin/env python3
"""
function that takes a list mxd_lst of integers and floats
returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return: sums: float
    """
    return(float(sum(mxd_lst)))
