import pytest
from dz6.task1 import *


@pytest.mark.parametrize(
    ('tab', 'size', 'key', 'value', 'result'),
    [
        ([[], []], 0, 'Freeze', 'I want to sleep', [[['Freeze', 'I want to sleep']], []]),
        ([[['Freeze', 'I want to sleep']], []], 1, 'Freeze', 'I want to sleep', [[['Freeze', 'I want to sleep']], []]),
        ([[['Freeze', 'I want to sleep']], []], 1, 42, True, [[['Freeze', 'I want to sleep']], [[42, True]]]),
        (
                [[['Freeze', 'I want to sleep']], [[42, True]]],
                2, 'lrkovnowbaer', (1724, ':(', False),
                [[], [['lrkovnowbaer', (1724, ':(', False)]],
                 [['Free/home/freeze/projects/My_best_dz/dz6/task1.pyze', 'I want to sleep']], [[42, True]]]
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)]], [['Freeze', 'I want to sleep']], [[42, True]]],
                3, 'cringe', 1,
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [['Freeze', 'I want to sleep']],
                 [[42, True]]]
        )
    ]
)
def test_set_value(tab, size, key, value, result):
    assert set_value(tab, size, key, value)[0] == result


@pytest.mark.parametrize(
    ('tab', 'key', 'value'),
    [
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)]], [['Freeze', 'I want to sleep']], [[42, True]]],
                'lrkovnowbaer', (1724, ':(', False)
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)]], [['Freeze', 'I want to sleep']], [[42, True]]],
                42, True
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [['Freeze', 'I want to sleep']],
                 [[42, True]]],
                'cringe', 1
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [['Freeze', 'I want to sleep']],
                 [[42, True]]],
                'something else', None
        )
    ]
)
def test_get_value(tab, key, value):
    assert get_value(tab, key) is value


@pytest.mark.parametrize(
    ('tab', 'size', 'key', 'result'),
    [
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [['Freeze', 'I want to sleep']],
                 [[42, True]]],
                4, 'Freeze',
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [], [[42, True]]],
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [], [[42, True]]],
                3, 'ok',
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [], [[42, True]]],
        )
    ]
)
def test_del_value(tab, size, key, result):
    assert del_value(tab, size, key)[0] == result


@pytest.mark.parametrize(
    ('tab', 'size', 'result'),
    [
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [], [[42, True]]],
                3, 0.75
        ),
        (
                [[], [['lrkovnowbaer', (1724, ':(', False)], ['cringe', 1]], [['Freeze', 'I want to sleep']],
                 [[42, True]]],
                4, 1.0
        )
    ]
)
def test_load_factor(tab, size, result):
    assert load_factor(tab, size) == result
