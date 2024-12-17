from pathlib import Path


def get(day: int, part: int | None = None) -> str:
    suffix = "" if part is None else f"-{part}"
    return Path(f"tests/data/day{day:02}{suffix}.txt").read_text()


def test_day01() -> None:
    from aoc2024.day01 import solve

    gen = solve(get(1))

    assert next(gen) == 2580760
    assert next(gen) == 25358365


def test_day02() -> None:
    from aoc2024.day02 import solve

    gen = solve(get(2))

    assert next(gen) == 306
    assert next(gen) == 366


def test_example_day03() -> None:
    from aoc2024.day03 import solve

    gen = solve(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )

    assert next(gen) == 161
    assert next(gen) == 48


def test_real_day03() -> None:
    from aoc2024.day03 import solve

    gen = solve(get(3))

    assert next(gen) == 173731097
    assert next(gen) == 93729253


def test_example_day04() -> None:
    from aoc2024.day04 import solve

    gen = solve(
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX"
    )

    assert next(gen) == 18
    assert next(gen) == 9


def test_real_day04() -> None:
    from aoc2024.day04 import solve

    gen = solve(get(4))

    assert next(gen) == 2685
    assert next(gen) == 2048
