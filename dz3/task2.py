def ans(n: int) -> str:
    match n:
        case 12 | 1 | 2:
            return 'зима'
        case 3 | 4 | 5:
            return 'весна'
        case 6 | 7 | 8:
            return 'лето'
        case 9 | 10 | 11:
            return 'осень'
        case _:
            return 'числа должны лежать в промежутке от 1 до 12'


print(ans(int(input())))
