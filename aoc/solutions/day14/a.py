from typing import Counter

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    template = problem_input.lines()[0]
    frequency = Counter(template)
    pairs: Counter[str] = Counter()
    rules: dict[str, str] = {}

    for i in range(0, len(template) - 1):
        pairs[template[i : i + 2]] += 1

    for line in problem_input.lines()[2:]:
        k, v = line.split(" -> ")
        rules[k] = v

    for i in range(10):
        working_copy = pairs.copy()

        for rule, insert in zip(rules.keys(), rules.values()):
            if pairs[rule] > 0:
                n = pairs[rule]
                first, second = rule[0] + insert, insert + rule[1]

                working_copy[first] += n
                working_copy[second] += n
                working_copy[rule] -= n
                frequency[insert] += n

        pairs = working_copy

    return frequency.most_common()[0][1] - frequency.most_common()[-1][1]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
