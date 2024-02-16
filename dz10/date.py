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


class Date(DataDate):
    def __init__(self, date: str = '01.01.2000') -> None:
        self.day, self.month, self.year = map(int, date.split('.'))

    def change_date(self):
        self.day, self.month, self.year = map(int, input('Введите новую дату: ').split('.'))

    def __str__(self):
        return f'{self.day} {self.MONTHS[self.month]} {self.year} года'


date1 = Date()
print(date1)
date1.change_date()
print(date1)
