from View import View
from Model import Model
from numpy import sin, cos, pi, arange

WIDTH, HEIGHT = 600, 600
EDGE_OFFSET = 20
POINT_RADIUS = 5
HEAT_BOUND = 0.1
POINT_POWER = 50

class Controller:
    def __init__(self, N):
        self.model = Model(N, (WIDTH, HEIGHT), EDGE_OFFSET)
        self.view = View((WIDTH, HEIGHT))
        self.pixels = [[(0,0,0) for i in range(WIDTH)] for j in range(HEIGHT)]
        self.heat_map = [[0 for i in range(WIDTH)] for row in range(HEIGHT)]
        self.point_coords = []

    def run(self):
        self._generate_map()
        self.view.run(self.pixels)

    def _generate_map(self):
        self.model.generate_point_coords()
        self.point_coords = self.model.get_point_coords()

        self._evaluate_heat_map()
        self._adjust_map_with_heat_bound(HEAT_BOUND)

        for point in self.point_coords:
            self._set_point(point[0], point[1])

    def _set_point(self, x, y):
        self.pixels[y][x] = (255,0,0)
        for t in arange(0, pi, 0.05):
            y_diff = int(sin(t) * POINT_RADIUS)
            x_diff = int(cos(t) * POINT_RADIUS)

            for i in range(x_diff):
                for j in range(y_diff):
                    self.pixels[y + i][x + j] = (255,0,0)
                    self.pixels[y + i][x - j] = (255,0,0)
                    self.pixels[y - i][x + j] = (255,0,0)
                    self.pixels[y - i][x - j] = (255,0,0)

    def _evaluate_heat_map(self):
        for point in self.point_coords:
            for t in arange(0, pi, 0.05):
                x1, y1 = point
                y_diff = int(sin(t) * POINT_POWER)
                x_diff = int(cos(t) * POINT_POWER)

                for i in range(x_diff):
                    for j in range(y_diff):
                        for x2, y2 in ((x1 + i, y1 + j), (x1 - i, y1 + j), (x1 + i, y1 - j), (x1 - i, y1 - j)):
                            if x2 >= 0 and x2 < WIDTH and y2 >= 0 and y2 < HEIGHT:
                                distance = self._get_distance(x1, y1, x2, y2)
                                if distance == 0:
                                    self.heat_map[y2][x2] = POINT_POWER
                                else:
                                    self.heat_map[y2][x2] += (3 * POINT_POWER**2) / (distance**4)
    
    def _adjust_map_with_heat_bound(self, heat_bound):
        for i, row in enumerate(self.heat_map):
            for j, value in enumerate(row):
                if value > heat_bound:
                    self.pixels[i][j] = (0,255,0)

    def _get_distance(self, x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5