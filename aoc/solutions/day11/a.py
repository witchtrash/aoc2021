from __future__ import annotations

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)

Point = tuple[int, int]


def neighbors(p: Point) -> list[Point]:
    adjacent_directions: list[Point] = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
    ]

    neighbors: list[Point] = []

    for direction in adjacent_directions:
        x, y = p
        dx, dy = direction

        ydx, xdx = y + dy, x + dx
        if ydx < 0 or xdx < 0 or ydx > 9 or xdx > 9:
            continue
        neighbors.append((xdx, ydx))

    return neighbors


def solve(problem_input: Input) -> int:
    flashes = 0
    octopi = [[int(x) for x in line] for line in problem_input.lines()]
    octopi_neighbors: dict[Point, list[Point]] = {}

    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            octopi_neighbors[(x, y)] = neighbors((x, y))

    for _ in range(100):
        flashed: set[Point] = set()
        pending: list[Point] = []

        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x] += 1
                if octopi[y][x] > 9:
                    pending.append((x, y))

        while len(pending) > 0:
            pending = []
            for y in range(len(octopi)):
                for x in range(len(octopi[y])):
                    if octopi[y][x] > 9 and (x, y) not in flashed:
                        pending.append((x, y))
                        flashed.add((x, y))

                        for neighbor in octopi_neighbors[(x, y)]:
                            nx, ny = neighbor
                            octopi[ny][nx] += 1

        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                if octopi[y][x] > 9:
                    octopi[y][x] = 0
        flashes += len(flashed)
    return flashes


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
