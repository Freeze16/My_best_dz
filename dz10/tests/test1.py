import pytest
from dz10.date import Date, DateStamp

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
    assert str(d2) == '1 января 2000 года'


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


@pytest.mark.parametrize(
    ('date', 'result'),
    [
        ('2.2.2022', 2),
        ('11 сентября 2001', 9)
    ]
)
def test_convert_month_to_number(date, result):
    d2 = Date(date)
    assert d2.month == result


@pytest.mark.parametrize(
    ('date', 'result'),
    [
        ('11 сентября 2001', (11, 9, 2001)),
        ('12.11.2047', (12, 11, 2047)),
    ]
)
def test_date_stamp_init(date, result):
    ds = DateStamp(date)
    assert ds.day == result[0]
    assert ds.month == result[1]
    assert ds.year == result[2]


@pytest.mark.parametrize(
    ('date1', 'date2', 'result'),
    [
        ('11.06.2003', '12.03.2006', '23.09.4009'),
        ('01.12.2015', '01.12.2005', '02.12.4021'),
        ('28.02.2020', '01.01.01', '29.03.2021'),
        ('31.01.2000', '01.01.1000', '03.03.3000'),
    ]
)
def test_add(date1, date2, result):
    assert Date(date1) + Date(date2) == Date(result)


@pytest.mark.parametrize(
    ('date1', 'date2', 'result'),
    [
        ('15.03.2005', '10.02.2000', '05.01.05'),
        ('31.01.2000', '01.01.1000', '30.12.999'),
        ('01.04.2000', '01.01.1001', '28.02.999'),
        ('01.04.2000', '01.01.1000', '29.02.1000'),
    ]
)
def test_sub(date1, date2, result):
    assert Date(date1) - Date(date2) == Date(result)


@pytest.mark.parametrize(
    ('date1', 'date2'),
    [
        ('01.01.01', '1.1.1'),
        ('20.08.1508', '20.8.1508'),
    ]
)
def test_eq(date1, date2):
    assert Date(date1) == Date(date2)
