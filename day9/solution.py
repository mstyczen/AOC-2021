import numpy as np

def parse_input(file_path):
    with open(file_path, "r") as f:
        numbers = [[int(c) for c in line.strip()] for line in f.readlines()]
        return np.array(numbers)

def is_out_of_bounds(matrix, point):
    i,j = point
    return i >= 0 and i < matrix.shape[0] and j >= 0 and j < matrix.shape[1]

def get_neighbors(matrix, i, j):
    neighbor_indices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    neighbor_indices = list(filter(lambda point: is_out_of_bounds(matrix, point), neighbor_indices))
    neighbor_values = [matrix[x,y] for (x,y) in neighbor_indices]

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
    basin_sizes = [len(find_basin(matrix, {minimum})) for minimum in minimas]

    return np.prod(sorted(basin_sizes, reverse=True)[:3])

if __name__ == "__main__":
    matrix = parse_input("full-input.txt")
    print("Part I: ", part1(matrix))
    print("Part II: ", part2(matrix))