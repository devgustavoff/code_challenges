# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str):
        for letter in instructions:
            if letter == "R":
                if self.direction == "north":
                    self.direction = EAST
                elif self.direction == "east":
                    self.direction = SOUTH
                elif self.direction == "south":
                    self.direction = WEST
                elif self.direction == "west":
                    self.direction = NORTH
            elif letter == "L":
                if self.direction == "north":
                    self.direction = WEST
                elif self.direction == "west":
                    self.direction = SOUTH
                elif self.direction == "south":
                    self.direction = EAST
                elif self.direction == "east":
                    self.direction = NORTH
            elif letter == "A":
                if self.direction == NORTH:
                    temp = list(self.coordinates)
                    temp[1] += 1
                    self.coordinates = tuple(temp)
                elif self.direction == SOUTH:
                    temp = list(self.coordinates)
                    temp[1] -= 1
                    self.coordinates = tuple(temp)
                elif self.direction == EAST:
                    temp = list(self.coordinates)
                    temp[0] += 1
                    self.coordinates = tuple(temp)
                elif self.direction == WEST:
                    temp = list(self.coordinates)
                    temp[0] -= 1
                    self.coordinates = tuple(temp)

robot = Robot(direction=WEST, x_pos=5, y_pos=5)
robot.move("A")
print(robot.coordinates, robot.direction)