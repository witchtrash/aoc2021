from aoc.lib.util import get_problem_input

problem_input = get_problem_input()
test_input = get_problem_input(test=True)


def solve(problem_input: str) -> int:
    measurements = [int(x) for x in problem_input.split()]
    increases = 0

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increases += 1

    return increases


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))