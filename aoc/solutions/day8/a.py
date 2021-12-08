from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    total = 0

    for line in problem_input.lines():
        _signals, output = line.split("|")
        for s in output.split():
            match len(s):
                case 2:
                    total += 1
                case 3:
                    total += 1
                case 4:
                    total += 1
                case 7:
                    total += 1

    return total


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
