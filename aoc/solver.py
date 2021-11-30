from typing import Protocol


class Solver(Protocol):
    def run(self) -> str:
        pass

    def test(self) -> str:
        pass
