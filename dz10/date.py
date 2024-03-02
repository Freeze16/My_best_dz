from typing import Any


class Date:
    MONTHS = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }

    DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date: str = '01.01.2000') -> None:
        date = self._format_check(date)
        self.day, self.month, self.year = self._validity_check(date)

    @staticmethod
    def _format_check(date: Any) -> list[str]:
        if isinstance(date, str):
            date = date.split('.') if '.' in date else date.split(' ')
            if len(date) == 3:
                return date

        raise ValueError('Неверный формат данных!')

    def _validity_check(self, date: list) -> tuple:
        date[1] = self._convert_month_to_number(date[1])
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

    def _convert_month_to_number(self, m: str) -> int:
        try:
            return int(m)
        except ValueError:
            for i in range(1, 13):
                if self.MONTHS[i] == m:
                    return i
            return 1

    def change_date(self):
        self.day, self.month, self.year = self._validity_check(input('Введите новую дату: ').split('.'))

    def __str__(self):
        return f'{self.day} {self.MONTHS[self.month]} {self.year} года'


class DateStamp(Date):
    def __init__(self, date: str = '01.01.2000'):
        super(DateStamp, self).__init__(date)


d = DateStamp('12 января 2023')
# d.change_date()
print(d)
print(d.day, d.month, d.year)
