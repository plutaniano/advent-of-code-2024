from typing import Generator


def is_increasing(levels: list[int]) -> bool:
    return all(left < right for left, right in zip(levels, levels[1:]))


def is_decreasing(levels: list[int]) -> bool:
    return all(left > right for left, right in zip(levels, levels[1:]))


def is_safe(levels: list[int]) -> bool:
    return all(1 <= abs(a - b) <= 3 for a, b in zip(levels, levels[1:])) and (
        is_decreasing(levels) or is_increasing(levels)
    )


def is_safe2(levels: list[int]) -> bool:
    for i, _ in enumerate(levels):
        new = levels[:i] + levels[i + 1 :]
        if all(1 <= abs(a - b) <= 3 for a, b in zip(new, new[1:])) and (
            is_decreasing(new) or is_increasing(new)
        ):
            return True
    return False


def solve(puzzle_input: str) -> Generator[int, None, None]:
    reports = [[int(i) for i in line.split()] for line in puzzle_input.splitlines()]

    yield sum(is_safe(levels) for levels in reports)
    yield sum(is_safe2(levels) for levels in reports)
