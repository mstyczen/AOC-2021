import numpy as np

def parse_input(path):
    with open(path, "r") as f:
        # parse first line - numbers
        numbers_str = f.readline().strip().split(",")
        numbers = list(map(int, numbers_str))
        
        # read the grids
        grids = []
        while f.readline():
            grid = []
            for _ in range(5):
                row_str = f.readline().strip().split()
                row = list(map(int, row_str))
                grid.append(row)
            grids.append(np.array(grid))

    return numbers, grids

def mark_number(grid, marker, num):
    # for each position in the grid if it contains the given number, mark it as 1 in the marker
    marker[grid == num] = 1
    return marker

def check_marker(marker):
    # check if a grid has a fully marked row/column
    N = marker.shape[0]
    return max(np.sum(marker, axis=0)) == N or max(np.sum(marker, axis=1)) == N

def masked_sum(grid, marker):
    grid[marker == 1] = 0
    return np.sum(grid)

def part1(numbers, grids):
    markers = [np.zeros_like(grid) for grid in grids]

    # iterate over the given numbers list
    for num in numbers:
        # mark the number in each grid
        for grid, marker in zip(grids, markers):
            marker = mark_number(grid, marker, num)
             # if grid has a fully marked row/column, return the sum of unmarked elements multiplied by the current number
            if check_marker(marker):
                return num * masked_sum(grid, marker)

    # in case not found
    return -1

def part2(numbers, grids):
    markers = [np.zeros_like(grid) for grid in grids]
    wins = np.zeros(len(grids))

    # iterate over the given numbers
    for num in numbers:
        # mark the number in each grid
        for i, (grid, marker) in enumerate(zip(grids, markers)):
            # if grid already won, don't check further
            if wins[i] == 1: 
                continue

            # mark the found numbers
            marker = mark_number(grid, marker, num)

            # if grid has a fully marked row/column, mark the grid as "won"
            if check_marker(marker):
                wins[i] = 1
                # if all of grids won, return the masked sum of the last one to win
                if np.sum(wins) == len(grids):
                    return num * masked_sum(grids[i], markers[i])

    # in case not found
    return -1


if __name__ == "__main__":
    numbers, grids = parse_input("full-input.txt")
    print("Part I: ", part1(numbers, grids))
    print("Part II: ", part2(numbers, grids))