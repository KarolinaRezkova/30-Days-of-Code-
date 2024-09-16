#!/bin/python3

import os


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def factorial(number: int) -> int:
    if number <= 1:
        return 1
    else:
        return number * (factorial(number - 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    #print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
