from math import factorial as fac


def diagonal(n: int, p: int) -> int:
    if not p:
        return n + 1

    summa = 1
    const_fac = fac(p)
    current_fac1, current_fac2 = const_fac, 1

    for i in range(p + 1, n + 1):
        current_fac1 *= i
        current_fac2 *= (i - p)
        summa += current_fac1 // (const_fac * current_fac2)

    return summa


if __name__ == '__main__':
    print(diagonal(int(input()), int(input())))
