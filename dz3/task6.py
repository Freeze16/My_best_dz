def check_simple(number: int):
    if number in (1, 4):
        return False

    for i in range(2, number // 2):
        if not number % i:
            return False

    return True


print(check_simple(int(input())))
