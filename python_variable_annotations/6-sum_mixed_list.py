#!/usr/bin/env python3

def sum_mixed_list(mxd_lst: list[float | int]) -> float:
    i = 0
    for num in mxd_lst:
        i += num
    return i
