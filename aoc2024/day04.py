from typing import Generator

INCREMENTS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def search_on(puzzle: list[str], i: int, j: int) -> int:
    total = 0
    for i_offset, j_offset in INCREMENTS:
        for index, letter in enumerate("MAS", start=1):
            try:
                assert letter == puzzle[i + (i_offset * index)][j + (j_offset * index)]
            except (IndexError, AssertionError):
                break
        else:
            print("-")
            print(i, j, (i_offset, j_offset))
            for index, letter in enumerate("MAS", start=1):
                print(letter, puzzle[i + (i_offset * index)][j + (j_offset * index)])
            total += 1

    return total


def solve(puzzle_input: str) -> Generator[int, None, None]:
    puzzle = puzzle_input.splitlines()

    total = 0
    for i, row in enumerate(puzzle_input.splitlines()):
        for j, letter in enumerate(row):
            if letter != "X":
                continue
            total += search_on(puzzle, i, j)

    yield total
