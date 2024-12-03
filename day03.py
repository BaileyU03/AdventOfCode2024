import re


def part01(text):
    return multiplier(text)


def part02(text):
    text = "do()" + text
    new_line = ""
    dos = list(map(lambda x: x.start(), re.finditer("do\(\)", text)))
    donts = list(map(lambda x: x.start(), re.finditer("don't\(\)", text)))
    while len(dos) > 0 and dos[0] < donts[-1]:
        do = dos[0]
        for dont in donts:
            if dont > do:
                new_line += text[do:dont]
                dos = [do for do in dos if do > dont]
                break
    if dos[-1] > donts[-1]:
        new_line += text[dos[-1]:]
    return multiplier(new_line)


def multiplier(text):
    muls = []
    while "mul" in text:
        mul_pos = text.find("mul")
        try:
            muls.append(text[mul_pos+3:mul_pos+13])
            text = text[0:mul_pos] + text[mul_pos+3:]
        except IndexError:
            muls.append(text[mul_pos:])
            text = text[0:mul_pos]
    total = 0
    for m in muls:
        match = re.search("^\(\d{1,3},\d{1,3}\)", m)
        if match is not None:
            pair = list(map(int, match.group()[1:-1].split(",")))
            total += pair[0] * pair[1]
    return total


def main():
    with open("./files/day03.txt", "r") as f:
        text = ""
        for line in f:
            text += line.split("\n")[0]
        print(part01(text))
        print(part02(text))


main()
