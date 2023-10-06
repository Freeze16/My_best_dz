def ans(txt: list) -> [str, str]:
    return [max(txt, key=lambda x: txt.count(x)), max(txt, key=len)]


print(*ans(input().split()))
