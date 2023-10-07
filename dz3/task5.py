from task1 import enter


def sub(*args) -> float:
    return sum(args) / len(args)


print(sub(*map(int, enter(input()))))
