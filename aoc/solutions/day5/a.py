from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def is_diagonal(x1: int, x2: int, y1: int, y2: int) -> bool:
    return x1 != x2 and y1 != y2


def is_vertical(x1: int, x2: int) -> bool:
    return x1 == x2


def is_horizontal(y1: int, y2: int) -> bool:
    return y1 == y2


def solve(problem_input: Input) -> int:
    grid: list[list[int]] = [[0] * 1000 for _ in range(1000)]
    overlaps: set[tuple[int, int]] = set()

    for line in problem_input.lines():
        s = line.split(" -> ")
        x1, y1 = map(int, s[0].split(","))
        x2, y2 = map(int, s[1].split(","))

        if is_diagonal(x1, x2, y1, y2):
            continue

        if is_vertical(x1, x2):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1
                if grid[y][x1] > 1:
                    overlaps.add((x1, y))

        if is_horizontal(y1, y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
                if grid[y1][x] > 1:
                    overlaps.add((x, y1))

    return len(overlaps)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
