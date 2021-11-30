from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    """Infinite fibonacci sequence generator"""
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b
