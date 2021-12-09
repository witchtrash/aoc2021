from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    heightmap = problem_input.lines()
    risk = 0

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
                risk += p + 1

    return risk


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
