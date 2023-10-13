from dz3.task1 import enter


def max_number(a):
    b = len(max(a, key=len))
    a.sort(key=lambda x: x * b, reverse=True)
    return int(''.join(a))


print(max_number(enter(input())))
