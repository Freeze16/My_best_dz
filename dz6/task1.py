from typing import Any


def create_hash_table(max_size: int = 5) -> tuple[list[list], int]:
    return [[] for _ in range(max_size)], 0


def contains(tab: list[list], key: str | int) -> bool:
    for lst in tab[hash_func(key) % len(tab)]:
        if key in lst:
            return True
    return False


def hash_func(key: str | int) -> int:
    hash_ = 5381
    for char in str(key):
        hash_ = ((hash_ << 5) + hash_) + ord(char)
    return hash_ & 0xFFFFFFFF


def set_value(tab: list[list], size: int, key: str | int, value: Any) -> tuple[list, int]:
    if not contains(tab, key):
        if len(tab) == size:
            tabl, size = create_hash_table(max_size=size * 2)
            for i in tab:
                for j in i:
                    tab, size = set_value(tabl, size, j[0], j[1])

        tab[hash_func(key) % len(tab)].append([key, value])
        size += 1

    return tab, size


def get_value(tab: list[list], key: str | int) -> Any:
    bucket = tab[hash_func(key) % len(tab)]
    for k in bucket:
        if key == k[0]:
            return k[1]


def del_value(tab: list[list], size: int, key: str | int) -> tuple[list[list], int]:
    value = get_value(tab, key)
    if contains(tab, key):
        tab[hash_func(key) % len(tab)].remove([key, value])
        size -= 1
    return tab, size


def load_factor(tab: list[list], size: int) -> float:
    return size / len(tab)
