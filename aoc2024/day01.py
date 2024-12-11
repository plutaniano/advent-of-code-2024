from collections import Counter
from functools import reduce
from typing import Generator


def solve(puzzle_input: str) -> Generator[int, None, None]:
    left: list[int] = []
    right: list[int] = []

    for line in puzzle_input.splitlines():
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    yield reduce(lambda cumsum, i: abs(i[0] - i[1]) + cumsum, zip(left, right), 0)

    counter = Counter(right)

    yield reduce(lambda cumsum, i: counter.get(i, 0) * i + cumsum, left, 0)
