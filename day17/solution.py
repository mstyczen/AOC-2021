from dataclasses import dataclass
import math
import re

@dataclass
class Area:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def contains(self, x, y):
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max

def parse_input(file_path):
    with open(file_path, "r") as f:
        line = f.readline().strip()
        x_min, x_max, y_min, y_max = map(int, re.findall('-?\d+', line))
        return Area(x_min, x_max, y_min, y_max)

def solve(area, max_steps):
    y_max = 0
    hits = 0 

    # bruteforce approach with bounded ranges
    for init_dx in range(area.x_max + 1):
        for init_dy in range(area.y_min - 1, -area.y_min + 1):
            x, y, y_max_ = 0, 0, 0
            dx, dy = init_dx, init_dy
            for _ in range(0, max_steps):
                x += dx
                y += dy
                if dx > 0: dx -= 1
                if dx < 0: dx += 1
                dy -= 1

                y_max_ = max(y_max_, y)

                # check for overshooting
                if y < area.y_min or x > area.x_max:
                    break
                
                # if area hit, update max y
                if area.contains(x,y):
                    y_max = max(y_max, y_max_)
                    hits += 1
                    break
                

    return y_max, hits


if __name__ == "__main__":
    area = parse_input("full-input.txt")
    y_max, hits = solve(area, 500)
    print("Part I: ", y_max)
    print("Part II: ", hits )
