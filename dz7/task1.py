from collections import deque
from typing import Any, Callable


def check(a, b) -> bool:
    # return a * 2 == b:
    # return a == b / 2:
    return a.lower() == b.lower()


def bfs(graph: dict[Any, list[Any]], start_el: Any, need_el: Any, condition: Callable) -> int | None:
    visited = set()
    queue = deque([(start_el, 0)])

    while queue:
        el, distance = queue.popleft()
        if condition(el, need_el):
            return distance
        for near_el in graph.get(el, []):
            if near_el not in visited:
                visited.add(near_el)
                queue.append((near_el, distance + 1))


if __name__ == '__main__':
    print(bfs({'A': ['b', 'c']}, 'A', 'b', check))
