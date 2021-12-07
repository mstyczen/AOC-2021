import numpy as np

def parse_input(file_path):
    with open(file_path, "r") as f:
        return list(map(int, f.readline().strip().split(",")))

def part1(crabs):
    return np.sum(np.abs(np.array(crabs) - np.median(crabs)))

def fuel_consumption(distances):
    n = np.abs(distances)
    return np.sum(n * (n + 1) / 2)

def part2(crabs):
    crabs = np.array(crabs)
    mean_down = int(np.mean(crabs))
    mean_up = mean_down + 1
    return min(fuel_consumption(crabs - mean_down), fuel_consumption(crabs - mean_up))

if __name__ == "__main__":
    crabs = parse_input("full-input.txt")
    print("Part I: ", part1(crabs))
    print("Part II: ", part2(crabs))
