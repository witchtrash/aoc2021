from collections import defaultdict, deque

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def is_small_cave(cave: str) -> bool:
    return cave == cave.lower()


def bfs(
    graph: defaultdict[str, list[str]],
    start: str,
    end: str,
) -> list[list[str]]:
    visited: set[str]
    paths: list[list[str]] = []
    queue: deque[tuple[list[str], str]] = deque()

    for n in graph.keys():
        if is_small_cave(n) and (n != "start" and n != "end"):
            queue.append(([start], n))

    while len(queue) > 0:
        current_path, allowed_duplicate = queue.popleft()
        last_node = current_path[-1]
        visited = set(current_path)

        if last_node == end:
            paths.append(current_path)

        for node in graph[last_node]:
            if is_small_cave(node) and node in visited and node != allowed_duplicate:
                continue

            new_path = current_path.copy()
            new_path.append(node)

            if node == allowed_duplicate and node in visited:
                queue.append((new_path, "lol nope"))
            else:
                queue.append((new_path, allowed_duplicate))
            visited.add(node)

    return paths


def solve(problem_input: Input) -> int:
    graph: defaultdict[str, list[str]] = defaultdict(list)

    for line in problem_input.lines():
        a, b = line.split("-")
        graph[a].append(b)
        graph[b].append(a)

    paths = bfs(graph, "start", "end")
    unique_paths = [list(x) for x in set(tuple(y) for y in paths)]

    return len(unique_paths)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
