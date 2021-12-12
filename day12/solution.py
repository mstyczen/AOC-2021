import networkx as nx

def parse_input(file_path):
    with open(file_path, "r") as f:
        edge_list = [tuple(line.strip().split("-")) for line in f.readlines()]
        g = nx.Graph()
        g.add_edges_from(edge_list)
        return g

def part1(g):
    return number_of_paths(g, ["start"], False)

def part2(g):
    return number_of_paths(g, ["start"], True)

def number_of_paths(g, path, double_visit):
    current = path[-1]

    # if you are already at the end, there is one path to the end (meaning staying where you are)
    if current == "end":
        return 1
    
    n_of_paths = 0
    # iterate through neighbors
    for neighbor in g[current]:
        # first visit case only consider uppercase nodes or the ones that were not visited yet
        if not neighbor in path or neighbor.isupper():
            n_of_paths += number_of_paths(g, path + [neighbor], double_visit)
        # second visit case - allow for a single double visit
        elif double_visit and path.count(neighbor) == 1 and neighbor != "start":
            n_of_paths += number_of_paths(g, path + [neighbor], False)

    return n_of_paths

if __name__ == "__main__":
    graph = parse_input("full-input.txt")
    print("Part I: ", part1(graph))
    print("Part II: ", part2(graph))