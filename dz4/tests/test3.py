import pytest
from dz4.task3 import check


@pytest.mark.parametrize(
    'pos',
    [
        [34, 'Hello, world!', False],
        '12345',
        tuple([23, '23']),
    ]
)
def test_true(pos):
    assert check(pos) is True


@pytest.mark.parametrize(
    'pos',
    [
        '1113',
        tuple([7, 7]),
    ]
)
def test_false(pos):
    assert check(pos) is False
