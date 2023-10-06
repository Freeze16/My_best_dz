def check(n: int) -> bool:
    if n in range(4):
        return False

    for i in (2, n // 2):
        if not n % i:
            return False
    return True


print(check(int(input())))
