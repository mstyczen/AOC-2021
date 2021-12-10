def parse_input(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def part1(lines, brackets):
    costs = {')':3, ']': 57, '}': 1197, '>': 25137}
    cost = 0

    for line in lines:
        stack = []
        for c in line:
            if c in brackets.keys():
                stack.append(c)
            else:
                opening_bracket = stack.pop()
                if c != brackets[opening_bracket]:
                    cost += costs[c]
                    break

    return cost

def part2(lines, brackets):
    missing_costs = {')':1, ']': 2, '}': 3, '>': 4}
    costs = []
    
    for line in lines:
        invalid = False
        stack = []

        for c in line:
            if c in brackets.keys():
                stack.append(c)
            elif stack:
                opening_bracket = stack.pop()
                if c != brackets[opening_bracket]:
                    invalid = True
                    break
            else:
                break

        if not invalid:
            missing_brackets = reversed([brackets[opening_bracket] for opening_bracket in stack])

            cost = 0
            for missing_bracket in missing_brackets:
                cost = cost * 5 + missing_costs[missing_bracket]

            costs.append(cost)

    return sorted(costs)[len(costs) // 2]

if __name__ == "__main__":
    brackets = {'(':')', '[': ']', '{':'}', '<':'>'}
    lines = parse_input("full-input.txt")

    print("Part I: ", part1(lines, brackets))
    print("Part II: ", part2(lines, brackets))

    

    