import pytest
from dz8.task2 import quick_sort


@pytest.mark.parametrize(
    ('array', 'reverse', 'result'),
    [
        ([], False, []),
        ([1], False, [1]),
        ([2, 4, 64, 234, 12, 3, -32], False, [-32, 2, 3, 4, 12, 64, 234]),
        ([-234, -324, 0, 234234, 12, 1], True, [234234, 12, 1, 0, -234, -324]),
        ([7, 7, 12, 1, 3, -1], True, [12, 7, 7, 3, 1, -1]),
        ([7, 7, 12, 1, 3, -1], False, [-1, 1, 3, 7, 7, 12]),
    ]
)
def test(array, reverse, result):
    assert quick_sort(array, reverse) == result
456886