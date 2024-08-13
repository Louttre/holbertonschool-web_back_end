#!/usr/bin/env python3
from typing import Callable

def make_multiplier(v: float) -> Callable[[float], float]:
    def multiplier(a: float) -> float:
        return a * v
    return multiplier
