from aoc.lib.util import get_problem_input

problem_input = get_problem_input()
test_input = get_problem_input(test=True)


def solve(x: str) -> str:
    return x


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
