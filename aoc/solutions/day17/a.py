import dataclasses
import re

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)

Point = tuple[int, int]


@dataclasses.dataclass
class BoundingBox:
    a: Point
    b: Point

    def intersects(self, point: Point) -> bool:
        px, py = point
        ax, ay = self.a
        bx, by = self.b

        return ax <= px <= bx and ay <= py <= by

    def passed(self, point: Point) -> bool:
        # Check if the point is past the box in the x or y axis
        px, py = point
        min_y = min(self.a[1], self.b[1])
        bx, _ = self.b

        return px > bx or py < min_y


def simulate(x_velocity: int, y_velocity: int, box: BoundingBox) -> tuple[Point, int]:
    point: Point = (0, 0)
    max_y = 0
    while not box.intersects(point) and not box.passed(point):
        point = (point[0] + x_velocity, point[1] + y_velocity)
        max_y = max(point[1], max_y)
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1

    return (point, max_y)


def solve(problem_input: Input) -> int:
    s = problem_input.raw(strip=True).split(",")
    sx = re.search(r"=((?:-)?\d+)\.\.((?:-)?\d+)", s[0])
    sy = re.search(r"=((?:-)?\d+)\.\.((?:-)?\d+)", s[1])
    max_y = 0

    assert sx is not None and sy is not None

    box = BoundingBox(
        a=(int(sx.group(1)), int(sy.group(1))),
        b=(int(sx.group(2)), int(sy.group(2))),
    )

    for x in range(0, 500):
        for y in range(-250, 250):
            point, y_pos = simulate(x, y, box)

            if box.intersects(point):
                max_y = max(max_y, y_pos)

    return max_y


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
