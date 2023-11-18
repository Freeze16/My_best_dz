from typing import Any


def create_hash_table(max_size: int = 5) -> tuple[list[dict], int]:
    return [{} for _ in range(max_size)], 0


def contains(tab: list[dict], size: int, key: str | int) -> bool:
    return key in tab[hash_func(tab, size) % len(tab)]


def hash_func(tab: list[dict], size: int, const: float = (5 ** 0.5 - 1) / 2) -> int:
    return int(len(tab) * ((size * const) % 1))


def set_value(tab: list[dict], size: int, key: str | int, value: Any) -> tuple[list, int]:
    if not contains(tab, size, key):
        if len(tab) == size:
            tabl, size = create_hash_table(max_size=size * 2)
            for i in tab:
                for j in i:
                    tab, size = set_value(tabl, size, j, i[j])

        tab[hash_func(tab, size) % len(tab)][key] = value
        size += 1

    return tab, size


def get_value(tab: list[dict], size: int, key: str | int) -> Any:
    return tab[hash_func(tab, size) % len(tab)].get(key)


def del_value(tab: list[dict], size: int, key: str | int) -> tuple[list[dict], int]:
    if contains(tab, size, key):
        del tab[hash_func(tab, size) % len(tab)][key]
        size -= 1
    return tab, size


def load_factor(tab: list[dict], size: int) -> float:
    return size / len(tab)


def main():
    print(set_value([{}, {}, {}, {}, {}], 0, 1, 'one'))
    print(set_value([{1: 'one'}, {}, {}, {}, {}], 1, 'Hello, world!', 42))


if __name__ == '__main__':
    main()
