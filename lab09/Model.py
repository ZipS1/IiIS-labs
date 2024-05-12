from random import randint


class Model:
    def __init__(self, number_of_points, screen_size, edge_offset):
        self.number_of_points = number_of_points
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.point_coords = set()
        self.EDGE_OFFSET = edge_offset

    def generate_point_coords(self):
        while len(self.point_coords) < self.number_of_points:
            x = randint(self.EDGE_OFFSET, self.width - self.EDGE_OFFSET)
            y = randint(self.EDGE_OFFSET, self.height - self.EDGE_OFFSET)
            self.point_coords.add((x, y))

    def get_point_coords(self):
        return self.point_coords
