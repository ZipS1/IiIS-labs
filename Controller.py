from View import View
from Model import Model
from numpy import sin, cos, pi, arange

WIDTH, HEIGHT = 600, 600
EDGE_OFFSET = 20
POINT_RADIUS = 5


class Controller:
    def __init__(self, N):
        self.model = Model(N, (WIDTH, HEIGHT), EDGE_OFFSET)
        self.view = View((WIDTH, HEIGHT))
        self.pixels = [[(0,0,0) for i in range(WIDTH)] for j in range(HEIGHT)]
        self.pixels_map = [[0 for i in range(WIDTH)] for row in range(HEIGHT)]

    def run(self):
        self._generate_map()
        self.view.run(self.pixels)

    def _generate_map(self):
        self.model.generate_point_coords()
        point_coords = self.model.get_point_coords()
        for point in point_coords:
            self._set_point(point[0], point[1])

    def _set_point(self, x, y):
        self.pixels[y][x] = "red"
        for t in arange(0, pi, 0.05):
            y_diff = int(sin(t) * POINT_RADIUS)
            x_diff = int(cos(t) * POINT_RADIUS)

            for i in range(x_diff):
                for j in range(y_diff):
                    self.pixels[y + j][x + i] = (255,0,0)
                    self.pixels[y + j][x - i] = (255,0,0)
                    self.pixels[y - j][x + i] = (255,0,0)
                    self.pixels[y - j][x - i] = (255,0,0)
