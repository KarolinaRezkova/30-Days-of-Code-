#!/bin/python3

INPUT_SIZE = 6
HOURGLASS = [[1, 1, 1],
             [0, 1, 0],
             [1, 1, 1]]

MIN_HOURGLASS_SUM = - 9 * 7


def calculate_hourglass_sum(input_array: list[list[int]], index_x: int, index_y: int) -> int:
    current_sum = 0
    for i in range(3):
        for j in range(3):
            current_sum += HOURGLASS[i][j] * input_array[index_x + i][index_y + j]
    return current_sum


if __name__ == '__main__':

    # load input
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # init variables
    max_hour_glass_sum = MIN_HOURGLASS_SUM

    # calculate maximal hourglass sum
    for x_index in range(INPUT_SIZE - 2):
        for y_index in range(INPUT_SIZE - 2):
            current_hourglass_sum = calculate_hourglass_sum(arr, x_index, y_index)
            max_hour_glass_sum = max(max_hour_glass_sum, current_hourglass_sum)

    # print result
    print(max_hour_glass_sum)
