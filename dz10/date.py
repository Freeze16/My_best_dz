class DataDate:
    MONTHS = {
        1: 'Января',
        2: 'Февраля',
        3: 'Марта',
        4: 'Апреля',
        5: 'Мая',
        6: 'Июня',
        7: 'Июля',
        8: 'Августа',
        9: 'Сентября',
        10: 'Октября',
        11: 'Ноября',
        12: 'Декабря'
    }

    DAYS = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }


class Date(DataDate):
    def __init__(self, date: str = '01.01.2000') -> None:
        if not isinstance(date, str):
            raise ValueError('Неверный формат даты!')
        self.day, self.month, self.year = self._validity_check(date.split('.'))

    def _validity_check(self, date: list) -> tuple:
        if len(date) != 3:
            raise ValueError('Неверный формат даты!')
        day, month, year = map(int, date)
        dop_day = 1 if not year % 4 else 0
        if month not in self.DAYS:
            month = 1
        if month == 2 and (day < 1 or day > self.DAYS[month] + dop_day):
            day = 1
        if month != 2 and (day < 1 or day > self.DAYS[month]):
            day = 1
        if year < 0:
            year = abs(year)
        return day, month, year

    def change_date(self):
        self.day, self.month, self.year = self._validity_check(input('Введите новую дату: ').split('.'))

    def __str__(self):
        return f'{self.day} {self.MONTHS[self.month]} {self.year} года'
