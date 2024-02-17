import pytest
from dz10.date import Date

d = Date()


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
        ('Hello, world!', 'Неверный формат даты!'),
        (['aaa'], 'Неверный формат даты!'),
        (tuple(), 'Неверный формат даты!'),
        (set(), 'Неверный формат даты!'),
    ]
)
def test_validity_check_exception(date, result):
    with pytest.raises(ValueError) as ex:
        d._validity_check(date)
    assert ex.value.args[0] == result
