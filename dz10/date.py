from typing import Any


class Date:
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

    DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date: str = '01.01.2000') -> None:
        date = self._format_check(date)
        self.day, self.month, self.year = self._validity_check(date)

    @staticmethod
    def _format_check(date: Any) -> list[str]:
        if isinstance(date, str):
            date = date.split('.')
            if len(date) == 3:
                return date
        raise ValueError('Неверный формат данных!')

    @staticmethod
    def _validity_check(date: list) -> tuple:
        day, month, year = map(int, date)
        dop_day = 1 if not year % 4 else 0
        if month not in Date.MONTHS:
            month = 1
        if month == 2 and (day < 1 or day > Date.DAYS[month - 1] + dop_day):
            day = 1
        if month != 2 and (day < 1 or day > Date.DAYS[month - 1]):
            day = 1
        if year < 0:
            year = abs(year)
        return day, month, year

    def change_date(self):
        self.day, self.month, self.year = self._validity_check(input('Введите новую дату: ').split('.'))

    def __str__(self):
        return f'{self.day} {self.MONTHS[self.month]} {self.year} года'


d = Date('ЫЫЫ')
print(d)
print(d.day, d.month, d.year)
