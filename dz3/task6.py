def check_simple(number: int):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            return False
    return True


print(check_simple(int(input())))
