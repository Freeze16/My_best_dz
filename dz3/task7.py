from collections import Counter


def ans(txt: list) -> []:
    x = Counter(txt)
    return [max(x, key=lambda y: x[y]), max(txt, key=len)]


print(*ans(input().split()))
