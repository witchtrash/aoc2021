from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    numbers = [[int(b) for b in x] for x in problem_input.lines()]
    total: list[int]

    bits = len(numbers[0])

    oxygen_numbers = numbers.copy()
    co2_numbers = numbers.copy()

    i = 0
    while len(oxygen_numbers) > 1:
        total = [0] * bits

        for n in oxygen_numbers:
            for nx, x in enumerate(n):
                total[nx] += x

        truth_table = list(map(lambda num: num * 2 >= len(oxygen_numbers), total))

        oxygen_numbers = list(
            filter(
                lambda number: number[i] == int(truth_table[i]),
                oxygen_numbers,
            )
        )
        i += 1

    i = 0
    while len(co2_numbers) > 1:
        total = [0] * bits

        for n in co2_numbers:
            for nx, x in enumerate(n):
                total[nx] += x

        truth_table = list(map(lambda num: num * 2 < len(co2_numbers), total))

        co2_numbers = list(
            filter(
                lambda number: number[i] == int(truth_table[i]),
                co2_numbers,
            )
        )
        i += 1

    oxygen = "".join([str(x) for x in oxygen_numbers[0]])
    co2 = "".join([str(x) for x in co2_numbers[0]])

    return int(oxygen, 2) * int(co2, 2)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
