import pytest
from dz4.task1 import shift


@pytest.mark.parametrize(
    ('pos', 'k', 'result'),
    [
        (['1', '2', '3', '4', '5'], 2, ['4', '5', '1', '2', '3']),
        (['1', '2', '3', '4', '5'], 3, ['3', '4', '5', '1', '2']),
        (['1', '2', '3', '4', '5'], 0, ['1', '2', '3', '4', '5']),
        (['1', '2', '3', '4', '5'], 7, ['4', '5', '1', '2', '3']),
    ]
)
def test(pos, k, result):
    assert shift(pos, k) == result
