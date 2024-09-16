#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT


def process_input(n: int):
    for i in range(n):
        line = input()
        assert 2 <= len(line) <= 10_000

        even = line[0::2]
        odd = line[1::2]
        print(even + " " + odd)


if __name__ == '__main__':
    n = int(input().strip())
    assert 1 <= n <= 10

    process_input(n)
