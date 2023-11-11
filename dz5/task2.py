from typing import Sequence, Any


def bin_search(pos: Sequence, el: Any) -> int | None:
    min_index, max_index = 0, len(pos) - 1
    result = None
    while min_index <= max_index:
        index = (min_index + max_index) // 2
        if pos[index] == el:
            result = index
            max_index = index - 1
        elif pos[index] > el:
            max_index = index - 1
        else:
            min_index = index + 1
    return result


if __name__ == '__main__':
    # print(bin_search([-2, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
    # print(bin_search([1, 1, 1, 1, 1, 1], 1))
    # print(bin_search([1, 2, 3, 4, 5, 6], 4))
    print(bin_search([1, 2, 3, 4, 5], 2))
