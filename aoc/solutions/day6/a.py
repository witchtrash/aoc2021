from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    fishes: dict[int, int] = {i: 0 for i in range(9)}

    for x in problem_input.csv():
        fishes[int(x)] += 1

    for _ in range(80):
        spawn = fishes[0]
        fishes[0] = 0

        for i in range(1, 9):
            fishes[i - 1] = fishes[i]

        fishes[8] = spawn
        fishes[6] += spawn

    total = 0
    for _, v in fishes.items():
        total += v

    return total


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
