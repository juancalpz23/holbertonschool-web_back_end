#!/usr/bin/env python3
"""
    7-to_kv.py
    Write a type-annotated function to_kv that
    takes a string k and an int OR float v as arguments
    and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Returns a tuple with the string k
        and the square of int/float v.
    """
    return (k, v ** 2)
