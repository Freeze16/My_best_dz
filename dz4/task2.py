def fac(n):
    if n < 2:
        return 1
    return n * fac(n - 1)


if __name__ == '__main__':
    print(fac(int(input())))
