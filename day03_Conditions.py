#!/bin/python3

import math
import os
import random
import re
import sys


def is_weird(n: int) -> bool:
    if n % 2 == 1:
        return True
    elif 6 <= n <= 20:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input().strip())

    assert 1 <= N <= 100

    if is_weird(N):
        print("Weird")
    else:
        print("Not Weird")
