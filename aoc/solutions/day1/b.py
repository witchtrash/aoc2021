from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    measurements = problem_input.ints()
    increases = 0

    for i in range(1, len(measurements) - 2):
        window_a = sum(measurements[i - 1 : i + 2])
        window_b = sum(measurements[i : i + 3])

        if window_b > window_a:
            increases += 1

    return increases


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
