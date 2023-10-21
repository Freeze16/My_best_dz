from dz3.task1 import enter


def shift(pos: list, k: int) -> list:
    k %= len(pos)
    return pos[-k:] + pos[:-k]


if __name__ == '__main__':
    print(shift(enter(input()), int(input())))
