from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    numbers = [[int(b) for b in x] for x in problem_input.lines()]

    count = len(numbers)
    bits = len(numbers[0])

    total: list[int] = [0] * bits

    for n in numbers:
        for i, x in enumerate(n):
            total[i] += x

    gamma = 0
    mask = int("1" * bits, 2)

    for t in total:
        bits -= 1
        if t * 2 >= count:
            gamma += 1 << bits

    return gamma * (gamma ^ mask)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
