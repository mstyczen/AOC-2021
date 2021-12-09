import numpy as np

def parse_input(file_path):
    with open(file_path, "r") as f:
        numbers = [[int(c) for c in line.strip()] for line in f.readlines()]
        return np.array(numbers)

def get_neighbors(matrix, i, j):
    neighbor_values, neighbor_indices = [], []
    if i > 0:
        neighbor_indices.append((i-1,j))
        neighbor_values.append(matrix[i-1,j])
    if i < matrix.shape[0] - 1:
        neighbor_indices.append((i+1,j))
        neighbor_values.append(matrix[i+1,j])
    if j > 0:
        neighbor_indices.append((i,j-1))
        neighbor_values.append(matrix[i,j-1])
    if j < matrix.shape[1] - 1:
        neighbor_indices.append((i,j+1))
        neighbor_values.append(matrix[i,j+1])
    return neighbor_indices, np.array(neighbor_values)

def get_local_minimas(matrix):
    minimas = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            element = matrix[i,j]
            _, neighbors = get_neighbors(matrix, i, j)
            if (neighbors > element).all():
                minimas.append((i, j))
    return minimas

def part1(matrix):
    minimas = get_local_minimas(matrix)
    return sum([matrix[i,j] + 1 for (i,j) in minimas])

def find_basin(matrix, basin):
    if not basin:
        return {}
    else:
        for (i,j) in basin:
            positions, values = get_neighbors(matrix, i, j)
            basin_points = {position for position, value in zip(positions, values) if position not in basin and value > matrix[i, j] and value != 9}
            basin = basin.union(find_basin(matrix, basin_points))

    return basin

def part2(matrix):
    minimas = get_local_minimas(matrix)
    basin_sizes = []
    for minimum in minimas:
        basin = find_basin(matrix, {minimum})
        basin = sorted(basin)
        basin_size = len(basin)
        basin_sizes.append(basin_size)
    return np.prod(sorted(basin_sizes, reverse=True)[:3])

if __name__ == "__main__":
    matrix = parse_input("full-input.txt")
    print("Part I: ", part1(matrix))
    print("Part II: ", part2(matrix))