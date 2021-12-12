import numpy as np

def parse_input(file_path):
    with open(file_path, "r") as f:
        return np.array([[int(c) for c in line.strip()] for line in f.readlines()])

def step(grid):
    flash_count = 0

    grid += 1
    flashed = np.full(grid.shape, False)

    while True:
        flashes = flash(grid, flashed)
        if flashes == 0:
            break
        else:
            flash_count += flashes

    grid[flashed] = 0

    return grid, flash_count

def flash(grid, flashed):
    w, h = grid.shape
    count = 0

    for i in range(w):
        for j in range(h):
            if grid[i,j] > 9 and not flashed[i,j]:
                grid[max(0, i-1):min(w, i+2), max(0,j-1):min(h,j+2)] +=1
                flashed[i,j] = True
                count += 1

    return count     

def part1(grid, steps):
    flash_count = 0
    for i in range(steps):
        grid, flashes = step(grid)
        flash_count += flashes

    return flash_count

def part2(grid):
    iteration = 0
    while True:
        iteration += 1
        grid, _ = step(grid)
        if not grid.any():
            return iteration

if __name__ == "__main__":
    grid = parse_input("full-input.txt")
    print("Part I: ", part1(grid.copy(), 200))
    print("Part II: ", part2(grid.copy()))