def is_the_same(x) -> bool:
    x = [(i, type(i)) for i in x]
    return len(x) == len(set(x))


if __name__ == '__main__':
    print(is_the_same(input().split()))
