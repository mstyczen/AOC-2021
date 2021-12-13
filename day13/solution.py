from dataclasses import dataclass
from enum import Enum
import numpy as np

class Axis(Enum):
    Y = 1
    X = 2

@dataclass
class Point:
    x: int
    y: int

    def parse(point_string):
        point_data = point_string.split(',')
        return Point(int(point_data[0]), int(point_data[1]))


    def fold(self, fold):
        if fold.axis == Axis.X:
            if self.x > fold.coordinate:
                return Point(2 * fold.coordinate - self.x, self.y)
        else:
            if self.y > fold.coordinate:
                return Point(self.x, 2 * fold.coordinate - self.y)
        return Point(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

@dataclass
class Fold:
    axis: Axis
    coordinate: int

    def parse(fold_string):
        fold_data = fold_string.split(" ")[-1].split("=")
        axis = Axis.X if fold_data[0] == "x" else Axis.Y
        coordinate = int(fold_data[1])
        return Fold(axis, coordinate)

def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        split = lines.index("")
        points = set(map(lambda x: Point.parse(x), lines[:split]))
        folds = list(map(lambda x: Fold.parse(x), lines[split+1:]))
        return points, folds

def visualize_points(points):
    shape = max([(p.x + 1) for p in points]), max([(p.y + 1) for p in points])
    grid = np.full(shape, False)
    for p in points:
        grid[p.x, p.y] = True

    for i in range(shape[1]):
        for j in range(shape[0]):
            if grid[j,i]: print(u'\u2589', end="")
            else: print(' ', end="")
        print('')

def part1(points, folds):
    points_folded = {p.fold(folds[0]) for p in points}
    return len(points_folded)

def part2(points, folds):
    for fold in folds:
        points = {p.fold(fold) for p in points}
    visualize_points(points)
    

if __name__ == "__main__":
    points, folds = parse_input("full-input.txt")
    print("Part I: ", part1(points, folds))
    print("Part II: ")
    part2(points, folds)