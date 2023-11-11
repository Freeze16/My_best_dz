from dz3.task1 import enter
from typing import Union


def bin_search(pos: list[Union[int, float]], el: Union[int, float]) -> int:
    index, min_index, max_index = len(pos) // 2, 0, len(pos) - 1
    while pos[index] != el and min_index <= max_index:
        if pos[index] < el:
            min_index = index + 1
        else:
            max_index = index - 1

        index = (min_index + max_index) // 2

    if min_index <= max_index:
        return index


if __name__ == '__main__':
    print(bin_search(list(map(float, enter(input()))), float(input())))
