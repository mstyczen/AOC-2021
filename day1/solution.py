def parse_input(path):
    with open(path, "r") as f:
        input = []
        for line in f.readlines():
            input.append(int(line))
        return input

def part1(input):
    count = 0
    for i in range(len(input) - 1):
        if input[i] < input[i + 1]:
            count += 1
    return count

def part2(input):
    count = 0
    for i in range(len(input) - 3):
        if input[i] < input[i + 3]:
            count += 1
    return count

if __name__ == "__main__":
    input = parse_input("full-input.txt")
    print("Part I:", part1(input))
    print("Part II:", part2(input))
    

