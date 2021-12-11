from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def is_opening(c: str) -> bool:
    return c == "{" or c == "[" or c == "<" or c == "("


def match(opening: str, closing: str) -> bool:
    a = ord(opening)
    b = ord(closing)

    if a + 1 == b or a + 2 == b:
        return True

    return False


def solve(problem_input: Input) -> int:
    score = 0
    score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in problem_input.lines():
        stack: list[str] = []
        for character in line:
            if is_opening(character):
                stack.append(character)
            else:
                last_opening = stack.pop()
                if not match(last_opening, character):
                    score += score_map[character]
                    break

    return score


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
