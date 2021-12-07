from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    crabs = [int(x) for x in problem_input.csv()]
    start = min(crabs)
    stop = max(crabs)

    crab_positions = {i: 0 for i in range(start, stop + 1)}

    for crab in crabs:
        for i in range(start, stop + 1):
            distance = abs(i - crab)
            cost = (distance * (distance + 1)) // 2

            crab_positions[i] += cost

    return min(crab_positions.items(), key=lambda x: x[1])[1]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
