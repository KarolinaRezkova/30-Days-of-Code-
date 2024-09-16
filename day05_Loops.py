#!/bin/python3

RESULT_STRING_TEMPLATE = "{multiplier} x {multiplicand} = {product}"


def print_multiples(multiplier: int):
    for i in range(1, 11):
        print(RESULT_STRING_TEMPLATE.format(multiplier=multiplier, multiplicand=i, product=i*n))


if __name__ == '__main__':
    n = int(input().strip())

    print_multiples(n)