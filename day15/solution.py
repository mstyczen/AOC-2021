import networkx as nx
import numpy as np

def parse_input(file_path):
    with open(file_path, "r") as f:
        return np.array([[int(x) for x in line.strip()] for line in f.readlines()])

def get_neighbors(i, j, h, w):
    neighbors = [(i - 1, j), (i + 1, j), (i, j -1), (i, j + 1)]
    neighbors = [(i,j) for (i,j) in neighbors if i >= 0 and i < h and j >= 0 and j < w]
    return neighbors

def shortest_path(grid):
    edge_list = []
    h, w = grid.shape
    
    for i in range(h):
        for j in range(w):
            neighbors = get_neighbors(i, j, h, w)
            for (i_, j_) in neighbors:
                edge_list.append(((i,j), (i_, j_), grid[i_,j_]))

    g = nx.DiGraph()
    g.add_weighted_edges_from(edge_list)
    return nx.shortest_path_length(g,source=(0,0),target=(h-1,w-1), weight='weight')

def grow_grid(grid, times):
    h,w = grid.shape
    grids = [grid]

    for _ in range(times*w - 1):
        grids.append(np.mod(grids[-1], 9) + 1)

    new_grid = np.zeros((times*h, times*w))

    for i in range(times):
        for j in range(times):
            new_grid[i*h:(i+1)*h,j*w:(j+1)*w] = grids[i + j]

    return new_grid

if __name__ == "__main__":
    grid = parse_input("full-input.txt")
    print("Part I: ", shortest_path(grid))
    bigger_grid = grow_grid(grid, 5)
    print("Part II: ", shortest_path(bigger_grid))

