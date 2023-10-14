def fib(n: int) -> list:
    f = [0, 1, 1]
    for _ in range(n - 2):
        f.append(f[-2] + f[-1])

    return f[:n]  # При 2, 1 или 0


print(*fib(int(input())), sep=', ')
