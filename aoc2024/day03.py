import re
from typing import Generator, Literal

Instruction = Literal["do", "dont"] | tuple[int, int]


def parse(puzzle_input: str) -> list[Instruction]:
    matches = re.findall(r"(?:do\(\))|(?:don't\(\))|(?:mul\(\d+,\d+\))", puzzle_input)

    parsed: list[Instruction] = []
    for m in matches:
        match m:
            case "do()":
                parsed.append("do")
            case "don't()":
                parsed.append("dont")
            case other:
                a, b = other[4:-1].split(",")
                parsed.append((int(a), int(b)))

    print(parsed)
    return parsed


def solve(puzzle_input: str) -> Generator[int, None, None]:
    total1 = 0
    total2 = 0
    enabled = True

    for i in parse(puzzle_input):
        match i:
            case "do":
                enabled = True
            case "dont":
                enabled = False
            case a, b:
                total1 += a * b
                total2 += a * b * enabled

    yield total1
    yield total2
