def parse_input(path):
    with open(path, "r") as f:
        commands = []
        values = []
        for line in f.readlines():
            vs = line.strip().split(' ')
            commands.append(vs[0])
            values.append(int(vs[1]))
        return commands, values

def part1(commands, values):
    depth = 0
    horizontal = 0

    for c, v in zip(commands, values):
        if c == "down": depth += v
        if c == "up": depth -= v
        if c == "forward": horizontal += v

        # match c:
        #     case "down": depth += v
        #     case "up": depth -= v
        #     case "forward": horizontal += v
        #     case "backward": horizontal -= v

    return depth * horizontal

def part2(commands, values):
    depth = 0
    horizontal = 0
    aim = 0

    for c, v in zip(commands, values):
        if c == "down": aim += v
        if c == "up": aim -= v
        if c == "forward": 
            horizontal += v
            depth += aim * v

    return depth * horizontal

if __name__ == "__main__":
    commands, values = parse_input("full-input.txt")
    print("Part I: ", part1(commands, values))
    print("Part II: ", part2(commands, values))