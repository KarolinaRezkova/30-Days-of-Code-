#!/bin/python3


def convert_to_binary(number: int) -> list[int]:
    binary_number = []
    while number > 0:
        reminder = number % 2
        binary_number.insert(0, reminder)
        number = number // 2
    return binary_number


def count_max_consecutive_ones(binary_number: list[int]) -> int:
    indices_of_zeros = [index for index, key in enumerate(binary_number) if key == 0]
    indices_of_zeros.append(len(binary_number))
    maximal_consecutive_ones = 0
    last_zero_index = -1
    for index in indices_of_zeros:
        consecutive_ones = index - last_zero_index - 1
        if consecutive_ones > maximal_consecutive_ones:
            maximal_consecutive_ones = consecutive_ones
        last_zero_index = index
    return maximal_consecutive_ones


if __name__ == '__main__':
    n = int(input().strip())
    assert 1 <= n <= 1_000_000, "Invalid input, the input should be 1<= n <= 1_000_000"
    binary_n = convert_to_binary(n)
    max_consecutive_ones = count_max_consecutive_ones(binary_n)
    print(max_consecutive_ones)
