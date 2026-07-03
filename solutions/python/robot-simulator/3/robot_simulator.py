# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"

moviment = {
    "R": {
        "north": "east",
        "east": "south",
        "south": "west",
        "west": "north"
    },
    "L": {
        "north": "west",
        "west": "south",
        "south": "east",
        "east": "north"
    },
    "A": {
        "north": (0, 1),
        "south": (0, -1),
        "east": (1, 0),
        "west": (-1, 0)
    }
}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str):
        for letter in instructions:
            if letter == "A":
                delta_x, delta_y = moviment[letter][self.direction]
                current_x, current_y = self.coordinates
                self.coordinates = (current_x + delta_x, current_y + delta_y,)
            else:
                self.direction = moviment[letter][self.direction]