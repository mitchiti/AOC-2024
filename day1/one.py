import re

from word2number import w2n



def part_one(filename: str) -> list[list[int]]:
    with open(filename, encoding="utf-8") as f:
        calibration = f.read().split("\n")
    result = []
    for c in calibration:
        d = re.findall('\d', c)
        if len(d) == 1:
            result.append(int(('{}{}').format(d[0], d[0])))
        elif len(d) > 1:
            result.append(int(('{}{}').format(d[0], d[-1])))
    return sum(result)


def part_two(filename: str) -> list[list[int]]:

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    with open(filename, encoding="utf-8") as f:
        calibration = f.read().split("\n")
    result = []
    for c in calibration:
        d = ""
        for i, _ in enumerate(c):
            if c[i].isdigit():
                d += c[i]
            for n in numbers:
                if len(c) >= i + len(n):
                    if c[i:].startswith(n):
                        d += str(w2n.word_to_num(n))
        if len(d) == 0:
            print(c)
        if len(d) == 1:
            result.append(int(('{}{}').format(d[0], d[0])))
        elif len(d) > 1:
            result.append(int(('{}{}').format(d[0], d[-1])))
    return sum(result)


if __name__ == "__main__":
    input_path = "./day1/input"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
    