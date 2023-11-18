import pytest
from dz6.task1 import *


# Тесты допишу немного позже
@pytest.mark.parametrize(
    ('tab', 'size', 'key', 'value', 'result'),
    [
        ([{}, {}, {}, {}, {}], 0, 1, 'one', ([{1: 'one'}, {}, {}, {}, {}], 1)),
        ([{1: 'one'}, {}, {}, {}, {}], 1, 'Hello, world!', 42, ([{1: 'one'}, {}, {}, {'Hello, world!': 42}, {}], 2)),
    ]
)
def test_set(tab, size, key, value, result):
    assert set_value(tab, size, key, value) == result
