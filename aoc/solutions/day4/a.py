from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


class Bingo:
    def __init__(self, numbers: list[list[int]]) -> None:
        self.board: list[list[int]]
        self.marked: set[int] = set()
        self.unmarked: set[int] = set()
        self.last_number: int = 0

        self.board = numbers
        for row in numbers:
            for n in row:
                self.unmarked.add(n)

    def __repr__(self) -> str:
        s = ""
        for row in self.board:
            s += " | ".join(["{:2}".format(str(s)) for s in row])
            s += "\n"

        return s

    def mark(self, n: int) -> None:
        if n in self.unmarked:
            self.marked.add(n)
            self.unmarked.remove(n)
            self.last_number = n

    def has_win(self) -> bool:
        for row in self.board:
            for n in row:
                if n not in self.marked:
                    break
            else:
                return True

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[j][i] not in self.marked:
                    break
            else:
                return True

        return False

    def get_score(self) -> int:
        print(self.last_number, "*", sum(self.unmarked))
        return self.last_number * sum(self.unmarked)


def solve(problem_input: Input) -> int:
    line_input = problem_input.lines()
    drawing_numbers = [int(x) for x in line_input[0].split(",")]
    bingo_cards: list[Bingo] = []

    for i in range(2, len(line_input), 6):
        card_numbers = [
            [int(n.strip()) for n in x.split()] for x in line_input[i : i + 5]
        ]

        bingo_cards.append(Bingo(card_numbers))

    for d in drawing_numbers:
        for card in bingo_cards:
            card.mark(d)
            if card.has_win():
                return card.get_score()

    return 0


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
