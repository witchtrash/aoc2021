from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    return problem_input.raw()


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
