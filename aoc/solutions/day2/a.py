from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input()


def solve(problem_input: Input) -> int:
    commands = [(x.split()[0], int(x.split()[1])) for x in problem_input.lines()]
    horizontal = 0
    vertical = 0

    for (direction, value) in commands:
        match direction:
            case 'forward':
                horizontal += value
            case 'down':
                vertical += value
            case 'up':
                vertical -= value
    return horizontal * vertical


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
