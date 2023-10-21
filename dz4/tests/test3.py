import pytest
from dz4.task3 import is_the_same


@pytest.mark.parametrize(
    'pos',
    [
        [34, 'Hello, world!', False],
        '12345',
        tuple([23, '23']),
        [1, True],
    ]
)
def test_true(pos):
    assert is_the_same(pos) is True


@pytest.mark.parametrize(
    'pos',
    [
        '1113',
        tuple([7, 7]),
    ]
)
def test_false(pos):
    assert is_the_same(pos) is False
