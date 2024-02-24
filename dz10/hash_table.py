from typing import Any


class HashTable:
    def __init__(self, size: int = 5) -> None:
        self.tab, self.size = self._create_hash_table(size)

    @staticmethod
    def _create_hash_table(max_size: int) -> tuple[list[list], int]:
        return [[] for _ in range(max_size)], 0

    def contains(self, key: str | int) -> bool:
        for lst in self.tab[self.hash_func(key) % len(self.tab)]:
            if key in lst:
                return True
        return False

    def hash_func(self, key: str | int) -> int:
        own_hash = [ord(i) for i in key]
        if not len(self.tab):
            return sum(own_hash)
        return sum(own_hash) % len(self.tab)

    def set_value(self, key: str | int, value: Any) -> tuple[list, int]:
        if not self.contains(key):
            if len(self.tab) == self.size:
                old_tab = self.tab
                self.tab, self.size = self._create_hash_table(self.size * 2)
                for i in old_tab:
                    for j in i:
                        self.tab, self.size = self.set_value(j[0], j[1])

            self.tab[self.hash_func(key) % len(self.tab)].append([key, value])
            self.size += 1

        return self.tab, self.size

    def get_value(self, key: str | int) -> Any:
        bucket = self.tab[self.hash_func(key) % len(self.tab)]
        for k in bucket:
            if key == k[0]:
                return k[1]

    def del_value(self, key: str | int) -> bool:
        value = self.get_value(key)
        if self.contains(key):
            self.tab[self.hash_func(key) % len(self.tab)].remove([key, value])
            self.size -= 1
            return True
        return False

    def load_factor(self) -> float:
        return self.size / len(self.tab)

    def from_dict(self, dictionary: dict = None):
        self.__init__()
        for key, value in dictionary.items():
            self.set_value(key, value)

    def __str__(self) -> str:
        elements = [item for sublist in self.tab for item in sublist if item]
        return '{' + ', '.join('"{}": "{}"'.format(k, v) for k, v in elements) + '}'


if __name__ == '__main__':
    d = HashTable()
    d.from_dict({'abv': '123', 'gdz': 3})
    print(d)
    print(ord('ы') * 2 // ord('ы'))
