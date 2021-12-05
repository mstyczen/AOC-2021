from dataclasses import dataclass
import re
import numpy as np

@dataclass
class Point:
    x: int
    y: int

    def get_points_between(self, other):
        xs = self.get_coordinates_between(self.x, other.x)
        ys = self.get_coordinates_between(self.y, other.y)
        return xs, ys

    @staticmethod
    def get_coordinates_between(x1, x2):
        if x1 == x2:
            return [x1]
        if x1 < x2:
            return list(range(x1, x2 + 1))
        else:
            return list(range(x1, x2 - 1, -1))

@dataclass
class Edge:
    start: Point
    end: Point

    def is_vertical_or_horizontal(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def get_points(self):
        xs, ys = self.start.get_points_between(self.end)

        if self.is_vertical_or_horizontal():
            return [Point(x,y) for x in xs for y in ys]
        else:
            return [Point(x,y) for (x,y) in zip(xs,ys)]
        
def parse_input(input_file):
    with open(input_file, "r") as f:
        edges = [parse_edge(line) for line in f.readlines()]
        return edges

def parse_edge(line):
    cooridnates_str = line.strip().replace(' -> ', ',').split(',')
    coordinates = list(map(int, cooridnates_str))
    start = Point(coordinates[0], coordinates[1])
    end = Point(coordinates[2], coordinates[3])
    return Edge(start, end)

def make_grid(edges):
    max_x = max([max(edge.start.x, edge.end.x) for edge in edges])
    max_y = max([max(edge.start.y, edge.end.y) for edge in edges])
    grid = np.zeros((max_x + 1, max_y + 1))
    return grid

def number_of_overlaps(edges, only_horizontal_or_vertical):
    grid = make_grid(edges)

    for edge in edges:
        if not only_horizontal_or_vertical or edge.is_vertical_or_horizontal():
            points = edge.get_points()
            for point in points:
                grid[point.x, point.y] += 1

    return np.sum(grid > 1)

if __name__ == "__main__":
    edges = parse_input("full-input.txt")
    print("Part I: ", number_of_overlaps(edges, only_horizontal_or_vertical=True))
    print("Part II: ", number_of_overlaps(edges, only_horizontal_or_vertical=False))