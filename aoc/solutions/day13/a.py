from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)

Point = tuple[int, int]


def solve(problem_input: Input) -> int:
    split = problem_input.lines().index("")
    points: list[Point] = []
    paper: list[list[str]]
    width = 0
    height = 0
    dots = 0

    for point_line in problem_input.lines()[:split]:
        x, y = map(int, point_line.split(","))
        width = max(width, x + 1)
        height = max(height, y + 1)
        points.append((x, y))

    paper = [["." for _x in range(width)] for _y in range(height)]

    for point in points:
        x, y = point
        paper[y][x] = "#"

    for fold_line in problem_input.lines()[split + 1 :]:
        direction, value = fold_line.split(" ")[2].split("=")
        fold = int(value)

        new_paper: list[list[str]] = []
        paper_row: list[str] = []

        if direction == "x":
            # Reflect horizontal right
            right_fold = [
                [paper[y][x] for x in range(fold + 1, width)][::-1]
                for y in range(height)
            ]

            for right_y, row in enumerate(right_fold):
                paper_row = []
                for right_x, right_value in enumerate(row):
                    left_value = paper[right_y][right_x]

                    value = "#" if left_value == "#" or right_value == "#" else "."

                    paper_row.append(value)
                new_paper.append(paper_row)
            width //= 2

        else:
            # Reflect vertical up
            bottom = paper[fold:][::-1]

            for bottom_y, row in enumerate(bottom):
                paper_row = []
                for bottom_x, bottom_value in enumerate(row):
                    top_value = paper[bottom_y][bottom_x]

                    value = "#" if bottom_value == "#" or top_value == "#" else "."

                    paper_row.append(value)
                new_paper.append(paper_row)
            height //= 2

        paper = new_paper
        dots = sum([p.count("#") for p in paper])

        break

    return dots


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
