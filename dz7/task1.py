from collections import deque


def bfs(graph: dict[str, list[str]], start_el: str, need_el: str) -> int | None:
    visited = set()
    queue = deque([(start_el, 0)])

    while queue:
        el, distance = queue.popleft()
        if el == need_el:
            return distance
        for near_el in graph.get(el, []):
            if near_el not in visited:
                visited.add(near_el)
                queue.append((near_el, distance + 1))


if __name__ == '__main__':
    print(bfs({'a': ['b', 'c']}))
