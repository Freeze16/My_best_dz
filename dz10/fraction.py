class Fraction:
    def __init__(self, num: float = 1, den: float = 1):
        self.numerator = num
        self.denominator = den

    def input_digits(self):
        res = input('Введите числите и знаменатель через пробел:').split(' ')

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
