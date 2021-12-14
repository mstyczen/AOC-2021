from collections import defaultdict

def parse_input(file_path):
    with open(file_path, "r") as f:
        # parse the template
        polymer_template = f.readline().strip()
        # skip the empty line
        f.readline()
        # parse the rules
        rules = [line.strip().split(' -> ') for line in f.readlines()]
        rules = {rule[0]: rule[1] for rule in rules}

        return polymer_template, rules

def solve(template, rules, steps):
    # prepare the initial pairs
    transformations = {k: [k[0] + v, v +k[1]] for k,v in rules.items()}
    pairs = {pair: template.count(pair) for pair in transformations}

    for _ in range(steps):
        pairs = apply_step(pairs, transformations)
    
    # calculate frequencies by iterating through pairs
    frequencies = defaultdict(int)
    for pair, count in pairs.items():
        frequencies[pair[0]] += count
        frequencies[pair[1]] += count

    # each character was counted twice (for its left and right pair)
    # (excluding first and last character)
    frequencies_corrected = {k: (v//2) for k,v in frequencies.items()}
    frequencies_corrected[template[0]] += 1
    frequencies_corrected[template[-1]] += 1

    return max(frequencies_corrected.values()) - min(frequencies_corrected.values())

def apply_step(pairs, transformations):
    # copy the old pairs
    new_pairs = defaultdict(int)

    for pair, count in pairs.items():
        for result in transformations[pair]:
            new_pairs[result] += count

    return new_pairs

if __name__ == "__main__":
    template, rules = parse_input("full-input.txt")
    print("Part I: ", solve(template, rules, 10))
    print("Part II: ", solve(template, rules, 40))