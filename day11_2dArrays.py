#!/bin/python3

import numpy as np

INPUT_SIZE = 6
HOURGLASS = np.array([[1, 1, 1],
                      [0, 1, 0],
                      [1, 1, 1]])

MIN_HOURGLASS_SUM = - 9 * 7


def calculate_hourglass_sum(numpy_array: np.ndarray) -> int:
    assert np.size(numpy_array) == np.size(HOURGLASS)
    element_wise_product = numpy_array * HOURGLASS
    hourglass_sum = int(np.sum(element_wise_product))
    return hourglass_sum


if __name__ == '__main__':

    # load input
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # init variables
    numpy_arr = np.array(arr)
    max_hour_glass_sum = MIN_HOURGLASS_SUM

    # calculate maximal hourglass sum
    for x_index in range(INPUT_SIZE - 3):
        for y_index in range(INPUT_SIZE - 3):
            current_hourglass_sum = calculate_hourglass_sum(numpy_arr[x_index:x_index + 3, y_index:y_index + 3])
            max_hour_glass_sum = max(max_hour_glass_sum, current_hourglass_sum)

    # print result
    print(max_hour_glass_sum)
