import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
