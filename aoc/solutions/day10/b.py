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
    scores = []
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in problem_input.lines():
        stack: list[str] = []

        for character in line:
            if is_opening(character):
                stack.append(character)
            else:
                last_opening = stack.pop()
                if not match(last_opening, character):
                    break
        else:
            score = 0
            while len(stack) > 0:
                c = stack.pop()
                if c == "(":
                    c = ")"
                else:
                    c = chr(ord(c) + 2)
                score = score * 5 + score_map[c]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
