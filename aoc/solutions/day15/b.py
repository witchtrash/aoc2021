from dataclasses import dataclass, field
from queue import PriorityQueue

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)

Point = tuple[int, int]
Grid = list[list[int]]
VertexMap = dict[Point, list[tuple[Point, int]]]


@dataclass(order=True)
class WeightedPoint:
    item: Point = field(compare=False)
    priority: int


def get_vertices(grid: Grid, point: Point) -> list[tuple[Point, int]]:
    adjacent_directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    neighbors: list[tuple[Point, int]] = []

    for direction in adjacent_directions:
        try:
            dx, dy = direction
            x, y = point

            if x + dx < 0 or y + dy < 0:
                continue
            weight = grid[y + dy][x + dx]
            neighbors.append(((x + dx, y + dy), weight))

        except IndexError:
            pass

    return neighbors


def build_shortest_paths(grid: Grid, vertices: VertexMap, start: Point) -> Grid:
    queue: PriorityQueue[WeightedPoint] = PriorityQueue()
    weights = [[2 ** 64 for _ in row] for row in grid]
    weights[0][0] = 0

    queue.put(WeightedPoint(item=start, priority=0))

    while queue.qsize() > 0:
        p = queue.get()
        point = p.item
        x, y = point
        for v in vertices[point]:
            v_point, v_weight = v
            vx, vy = v_point

            distance = weights[y][x] + v_weight
            if distance < weights[vy][vx]:
                weights[vy][vx] = distance
                queue.put(WeightedPoint(v_point, weights[vy][vx]))

    return weights


def increment(x: int, i: int) -> int:
    value = x + i
    value = value % 10 + 1 if value > 9 else value
    return value


def solve(problem_input: Input) -> int:
    grid: Grid = [[int(p) for p in row] for row in problem_input.lines()]
    height = len(grid)

    for y, row in enumerate(grid):
        new_row = row.copy()
        for i in range(1, 5):
            for x in row:
                new_row.append(increment(x, i))
        grid[y] = new_row

    for i in range(1, 5):
        for y in range(height):
            grid.append([increment(x, i) for x in grid[y]])

    vertices: VertexMap = {}
    bx = len(grid[0]) - 1
    by = len(grid) - 1

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            p = (x, y)
            vertices[p] = get_vertices(grid, p)

    weights = build_shortest_paths(grid, vertices, (0, 0))

    return weights[by][bx]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
