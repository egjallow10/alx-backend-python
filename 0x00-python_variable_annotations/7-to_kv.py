#!/usr/bin/env python3
"""Function that  takes str float or int, returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns str, square of v """
    return k, v**2.0
