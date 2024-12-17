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


def search_xmas_on(puzzle: list[str], i: int, j: int) -> int:
    total = 0
    for i_step, j_step in INCREMENTS:
        for index, letter in enumerate("MAS", start=1):
            i_offset = i + (i_step * index)
            j_offset = j + (j_step * index)
            try:
                assert i_offset >= 0 and j_offset >= 0
                assert letter == puzzle[i_offset][j_offset]
            except (IndexError, AssertionError):
                break
        else:
            total += 1

    return total


def search_x_mas_on(puzzle: list[str], i: int, j: int) -> int:
    try:
        assert i - 1 >= 0 and j - 1 >= 0
        letters = "".join(
            [
                puzzle[i - 1][j - 1],
                puzzle[i - 1][j + 1],
                puzzle[i + 1][j - 1],
                puzzle[i + 1][j + 1],
            ]
        )
        return letters in ["MSMS", "MMSS", "SSMM", "SMSM"]
    except (IndexError, AssertionError):
        return 0


def solve(puzzle_input: str) -> Generator[int, None, None]:
    puzzle = puzzle_input.splitlines()

    total1 = 0
    total2 = 0
    for i, row in enumerate(puzzle_input.splitlines()):
        for j, letter in enumerate(row):
            if letter == "X":
                total1 += search_xmas_on(puzzle, i, j)
            elif letter == "A":
                total2 += search_x_mas_on(puzzle, i, j)

    yield total1
    yield total2
