import math


def divisors(n: int) -> list[int]:
    """Get the proper divisors of a number n"""

    limit = int(math.sqrt(n)) + 1
    proper_divisors = {1}

    for i in range(2, limit):
        if n % i == 0:
            proper_divisors.add(n // i)
            proper_divisors.add(i)

    return list(proper_divisors)


def number_of_digits(n: int) -> int:
    """Return the number of digits of number n"""

    return math.floor(math.log10(n)) + 1
