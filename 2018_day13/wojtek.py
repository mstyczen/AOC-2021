class Cart:
    directions = ['<', '^', '>', 'v']
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersectionCounter = 0

    # Comparing:
    # for sorting - could also be used for overloading
    # __lt__	describes less than operator(<)
    # __le__	descries less than or equal to (<=)
    # __gt__	describes greater than (>)
    # __ge__	describes greater than or equal to (>=)
    # __eq__	describes equality operator(==)
    # __ne__	describes not equal to operator(!=)
    def __lt__(self, other):
        if (self.y < other.y) or (self.y == other.y and self.x < self.y):
            return True
        return False

    def __eq__(self, other):
        if (self.x == other.x and self.y == other.y):
            return True
        return False

    def __gt__(self, other):
        if (self.y > other.y) or (self.y == other.y and self.x > self.y):
            return True
        return False

    def __str__(self):
        return f"Cart at x: {self.x}, y: {self.y}, directed: {self.direction}"

    def turn(self, track):
        directionChangesBackSlash = {'<':'^', '>':'v', '^':'<', 'v':'>'}
        directionChangesForwardSlash = {'<':'v', '>':'^', '^':'>', 'v':'<'}
        if track == '\\':
            self.direction = directionChangesBackSlash[self.direction]
        elif track == '/':
            self.direction = directionChangesForwardSlash[self.direction]

    def turnOnIntersection(self):
        directionIndex = self.directions.index(self.direction)
        match (self.intersectionCounter % 3):
            # left
            case 0:
                self.direction = self.directions[(directionIndex - 1) % 4]
                self.intersectionCounter += 1
                return
            # straight
            case 1:
                self.intersectionCounter += 1
                return
            case 2:
                self.direction = self.directions[(directionIndex + 1) % 4]
                self.intersectionCounter += 1
                return

    def moveForward(self):
        match self.direction:
            case '>':
                self.x += 1
                return
            case '<':
                self.x -= 1
                return
            case '^':
                self.y -= 1
                return
            case 'v':
                self.y += 1
                return

    def move(self, map):
        track = map[self.y][self.x]
        if track == '\\' or track == '/':
            self.turn(track)
        elif track == '+':
            self.turnOnIntersection()
        self.moveForward()

def getCrashLocation(carts):
    for i in range(len(carts)):
        for j in range(i + 1, len(carts)):
            if carts[i] == carts[j]:
                return (carts[i].x, carts[i].y)
    return ()

with open("full-input.txt") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]
    width = max([len(line) for line in lines])
    map = [[c for c in line + (width - len(line))*" "] for line in lines]

    directions = ['<', '>', '^', 'v']
    carts = []
    lineNr = 0
    for line in lines:
        found = [x for x in directions if x in line]
        for element in found:
            index = line.index(element)
            # Add carts found in this line to 'carts' list
            carts.append(Cart(index, lineNr, element))
            # swap those carts in 'map' with tracks underneath them
            if directions.index(element) < 2:
                map[lineNr][index] = '-'
            else:
                map[lineNr][index] = '|'
        lineNr += 1
    # for cart in carts:
    #     print(cart)
    crashed = False
    f = open("wojtek_out.txt", "a")
    while (not crashed):
        # sort - top-down then left-right - since the order matters
        carts = sorted(carts)
        for i, cart in enumerate(carts):
            cart.move(map)
            f.write(f"Moving cart {i} to position: {cart.x},{cart.y}\n")
        crashLocation = getCrashLocation(carts)
        if (len(crashLocation) > 0):
            crashed = True
            print(crashLocation)
    f.close()