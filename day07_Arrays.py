#!/bin/python3

import math
import os
import random
import re
import sys


def print_in_reversed_order(array: list[int]):
    arr.reverse()
    print(" ".join(str(item) for item in arr))
    pass


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    assert 1 <= n <= 1_000
    assert 1 <= max(arr) <= 10_000
    assert len(arr) == n
    
    print_in_reversed_order(arr)
