import pytest
from dz4.task2 import fac


@pytest.mark.parametrize(
    ('x', 'result'),
    [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1)
    ]
)
def test(x, result):
    assert fac(x) == result
