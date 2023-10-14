from collections import Counter


def ans(txt: list[str]) -> list:
    x = Counter(txt)
    return [x.most_common(1)[0][0], max(txt, key=len)]


print(*ans(input().split()))
