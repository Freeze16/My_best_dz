import pytest
from dz5.task1 import diagonal


@pytest.mark.parametrize(
    ('n', 'p', 'result'),
    [
        (7, 0, 8),
        (7, 1, 28),
        (7, 2, 56),
        (20, 3, 5985),
        (20, 4, 20349),
        (0, 0, 1),
        (1, 0, 2),
        (1, 1, 1),
    ]
)
def test(n, p, result):
    assert diagonal(n, p) == result
