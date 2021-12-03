def parse_input(path):
    with open(path, "r") as f:
        input = []
        k = None
        for line in f.readlines():

            # in the first iteration note down the length of the bitstring
            if not k:
                k = len(line)

            input.append(int(line, 2))

        return k, input

def get_most_common_bits(input):
    mask = 1 << k - 1
    N = len(input)
    most_common_bits = 0

    for _ in range(k - 1):
        mask >>= 1
        mapped_input = map(lambda bitstring: bitstring & mask, input)
        occurrences = sum(mapped_input) // mask
        if occurrences >= N / 2:
            most_common_bits += mask
    
    return most_common_bits

def part1(k, input):
    gamma = get_most_common_bits(input)
    epsilon = 2 ** (k - 1) - 1 - gamma
    return gamma * epsilon

def part2(k, input):
    oxygen_ratings, co2_ratings = input.copy(), input.copy()
    mask = 1 << k - 1

    for _ in range(k):
        
        if len(co2_ratings) == 1 and len(oxygen_ratings) == 1:
            break

        mask >>= 1

        if len(oxygen_ratings) > 1:
            oxygen_mask = get_most_common_bits(oxygen_ratings) & mask
            oxygen_ratings = list(filter(lambda x: x & mask == oxygen_mask, oxygen_ratings))

        if len(co2_ratings) > 1:
            co2_mask = get_most_common_bits(co2_ratings) & mask
            co2_ratings = list(filter(lambda x: x & mask != co2_mask, co2_ratings))
        
        
    return oxygen_ratings[0] * co2_ratings[0]

if __name__ == "__main__":
    k, input = parse_input("full-input.txt")
    print("Part I: ", part1(k, input))
    print("Part II: ", part2(k, input))