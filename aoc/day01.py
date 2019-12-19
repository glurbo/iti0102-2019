numbers = []
with open("day01.txt", "r") as f:
    for line in f:
        numbers.append(int(line))


def part_one():
    total = 0
    for num in numbers:
        total += num // 3 - 2
    return total


def part_two():
    total = 0
    for num in numbers:
        while num // 3 - 2 >= 0:
            new_num = num // 3 - 2
            num = new_num
            total += num
    return total


if __name__ == '__main__':
    print(part_one())
    print(part_two())
