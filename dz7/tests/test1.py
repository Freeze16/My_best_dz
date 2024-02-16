import pytest
from dz7.task1 import *


@pytest.mark.parametrize(
    ('graph', 'start_el', 'need_el', 'condition', 'distance'),
    [
        ({'Aboba': ['Boba', 'Biba']}, 'Aboba', 'Biba', lambda a, b: a == b, 1),
        ({'Aboba': ['Boba', 'Biba']}, 'Aboba', 'Biba', lambda a, b: a == b, 1),
        ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'D', 'E',
         lambda a, b: a == b, 1),
        ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'D',
         lambda a, b: a == b, 2),
        ({'A': ['B', 'E'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['A', 'D']}, 'A', 'F',
         lambda a, b: a == b, None),
        ({1: [2, 0], 0: [-1], 2: [3, 2.5]}, 1, 3, lambda a, b: a == b - 1, 1),
        ({1: [2, 0], 0: [-1], 2: [3, 2.5, 4]}, 1, 4, lambda a, b: a * 2 == b, 1),
        ({'Ivan': ['Karabanow', 'Tafincev']}, 'Ivan', 'karabanow', lambda a, b: a.lower() == b.lower(), 1),
    ]
)
def test_bfs(graph, start_el, need_el, condition, distance):
    assert bfs(graph, start_el, need_el, condition) == distance
