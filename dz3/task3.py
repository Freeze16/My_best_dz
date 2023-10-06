def fib(n: int) -> list:
    f = [1, 1]
    if n > 2:
        for _ in range(n - 2):
            f.append(f[-2] + f[-1])
    return f[:n]


print(*fib(int(input())), sep=', ')
