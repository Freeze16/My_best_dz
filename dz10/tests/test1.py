import pytest
from dz10.date import Date

d = Date()


@pytest.mark.parametrize(
    ('date', 'data'),
    [
        ('12.02.2005', (12, 2, 2005)),
        ('29.02.2005', (1, 2, 2005)),
        ('128.07.10249242', (1, 7, 10249242)),
    ]
)
def test_init(date, data):
    d1 = Date(date)
    assert d1.day == data[0]
    assert d1.month == data[1]
    assert d1.year == data[2]


def test_str():
    d2 = Date()
    assert str(d2) == '1 Января 2000 года'


@pytest.mark.parametrize(
    ('date', 'valid_day'),
    [
        (['12', '02', '2007'], (12, 2, 2007)),
        (['31', '12', '2024'], (31, 12, 2024)),
        (['31', '11', '2000'], (1, 11, 2000)),
        (['31', '13', '2000'], (31, 1, 2000)),
        (['128', '13', '2000'], (1, 1, 2000)),
        (['128', '13', '-2000'], (1, 1, 2000)),
        (['29', '02', '2023'], (1, 2, 2023)),
        (['29', '02', '2024'], (29, 2, 2024)),
    ]
)
def test_validity_check(date, valid_day):
    assert d._validity_check(date) == valid_day


@pytest.mark.parametrize(
    ('date', 'result'),
    [
        ('Hello, world!', 'Неверный формат данных!'),
        (['aaa'], 'Неверный формат данных!'),
        (tuple(), 'Неверный формат данных!'),
        (set(), 'Неверный формат данных!'),
    ]
)
def test_format_check_exception(date, result):
    with pytest.raises(ValueError) as ex:
        d._format_check(date)
    assert ex.value.args[0] == result


@pytest.mark.parametrize(
    ('date', 'result'),
    [
        ('12.03.78', ['12', '03', '78']),
        ('12.1234235235252.78', ['12', '1234235235252', '78']),
    ]
)
def test_format_check(date, result):
    assert d._format_check(date) == result
