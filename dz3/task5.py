def sub(*args: float) -> float:
    return sum(args) / len(args)


print(sub(*list(map(float, input().split()))))
