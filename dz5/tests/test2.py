import pytest
from dz5.task2 import bin_search


@pytest.mark.parametrize(
    ('pos', 'el', 'index'),
    [
        (list(map(float, [1, 2, 3, 4, 5])), 4.0, 3),
        (list(map(float, [1, 2, 3, 4, 5])), 6.0, None),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 3.0, 2),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 4.0, 3),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), 1.0, 0),
        (list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), -1.0, None),
        (list(map(float, [1, 2, 3, 3, 3, 4, 5])), 3.0, 3),
        (list(map(float, [1, 1, 2, 2, 3, 3, 3, 27, 28, 56])), 2.0, 2),
        (list(map(float, [56, 230, 234, 747, 83274, 823573723])), 823573723.0, 5),
        (list(map(float, [1])), 1.0, 0),
    ]
)
def test(pos, el, index):
    assert bin_search(pos, el) == index
