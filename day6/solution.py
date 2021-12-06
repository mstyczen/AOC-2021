def parse_input(file_path):
    with open(file_path, "r") as f:
        fish = f.readline().strip().split(",")
        return list(map(int, fish))

def naive(fish, n_of_days):
    # naive solution, following the logic presented in the task description
    for _ in range(n_of_days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
            
    return len(fish)

def n_of_fish(n_of_days):
    lookups = [1 for _ in range(n_of_days)]
    for depth in range(6, n_of_days):
        lookups[depth] = lookups[max(0, depth - 7)] + lookups[max(0, depth - 9)]
    return lookups[n_of_days - 1]

def dynamic(fish, n_of_days):
    # smarter solution, using a dynamic programming approach
    offsprings = 0
    for fish_ in fish:
        offspring = n_of_fish(n_of_days + (6 - fish_))
        offsprings += offspring
    return offsprings

if __name__ == "__main__":
    fish = parse_input("full-input.txt")
    print("Part I: ", dynamic(fish.copy(), 80))
    print("Part II: ", dynamic(fish.copy(), 256))
    