#!/usr/bin/env python3
"""
list of input_list of floats as argument
returns  sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum from the list
    """
    return float(sum(input_list))
