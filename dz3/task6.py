def check(number: int, current_number=2):
    if number % current_number == 0:
        return current_number

    return check(number, current_number + 1)


def check_simple(n: int) -> bool:
    if n == 1:
        return False
    return bool(check(n) == n)


print(check_simple(3))
