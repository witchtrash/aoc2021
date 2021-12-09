from collections import deque

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def size_of_basin(heightmap: list[str], point: tuple[int, int]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q: deque[tuple[int, int]] = deque()
    q.append(point)

    found: set[tuple[int, int]] = set()
    basin: set[tuple[int, int]] = {point}

    while len(q) > 0:
        p = q.popleft()
        x, y = p

        found.add(p)
        basin.add(p)

        for direction in directions:
            dx, dy = direction
            try:
                if x + dx < 0 or y + dy < 0:
                    continue

                d = int(heightmap[y + dy][x + dx])

                if d != 9:
                    px = (x + dx, y + dy)
                    if px not in found:
                        q.append((x + dx, y + dy))
            except IndexError:
                pass

    return len(basin)


def solve(problem_input: Input) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    heightmap = problem_input.lines()
    basins: list[int] = []

    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            p = int(heightmap[y][x])
            if p == 9:
                continue
            for direction in directions:
                dx, dy = direction
                try:
                    d = int(heightmap[y + dy][x + dx])
                    if p > d:
                        break
                except IndexError:
                    pass
            else:
                # Lowest point of basin found
                basins.append(size_of_basin(heightmap, (x, y)))

    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
