from View import View
from Model import Model
import numpy as np

WIDTH, HEIGHT = 600, 600
EDGE_OFFSET = 20
POINT_RADIUS = 5
HEAT_BOUND = 0.1
POINT_POWER = 50
DEBUG_SHOW_TOWER_RADIUS = True  # TODO


class Controller:
    def __init__(self, N):
        self.model = Model(N, (WIDTH, HEIGHT), EDGE_OFFSET)
        self.view = View((WIDTH, HEIGHT))
        self.pixels = [[(0, 0, 0) for i in range(WIDTH)] for j in range(HEIGHT)]
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

        if DEBUG_SHOW_TOWER_RADIUS:
            self._show_tower_radius()

        for point in self.point_coords:
            self._set_point(point[0], point[1])

    def _set_point(self, x, y):
        self.pixels[y][x] = (255, 0, 0)
        for t in np.arange(0, np.pi, 0.05):
            y_diff = int(np.sin(t) * POINT_RADIUS)
            x_diff = int(np.cos(t) * POINT_RADIUS)

            for i in range(x_diff):
                for j in range(y_diff):
                    self.pixels[y + i][x + j] = (255, 0, 0)
                    self.pixels[y + i][x - j] = (255, 0, 0)
                    self.pixels[y - i][x + j] = (255, 0, 0)
                    self.pixels[y - i][x - j] = (255, 0, 0)

    def _evaluate_heat_map(self):
        for point in self.point_coords:
            for t in np.arange(0, np.pi, 0.05):
                x1, y1 = point
                y_diff = int(np.sin(t) * POINT_POWER)
                x_diff = int(np.cos(t) * POINT_POWER)

                for i in range(x_diff):
                    for j in range(y_diff):
                        for x2, y2 in (
                            (x1 + i, y1 + j),
                            (x1 - i, y1 + j),
                            (x1 + i, y1 - j),
                            (x1 - i, y1 - j),
                        ):
                            if x2 >= 0 and x2 < WIDTH and y2 >= 0 and y2 < HEIGHT:
                                distance = self._get_distance(x1, y1, x2, y2)
                                value = self.heat_map[y2][x2]
                                if distance == 0:
                                    value = 1
                                elif value < 1:
                                    value += 1 - distance / POINT_POWER
                                    if value > 1:
                                        value = 1

                                self.heat_map[y2][x2] = value

    def _adjust_map_with_heat_bound(self, heat_bound):
        for i, row in enumerate(self.heat_map):
            for j, value in enumerate(row):
                if value > heat_bound:
                    self.pixels[i][j] = (0, 255, 0)

    def _get_distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    def _show_tower_radius(self):
        for point in self.point_coords:
            x, y = point
            for t in np.arange(- np.pi, np.pi / 2, 0.05):
                y_diff = int(np.sin(t) * POINT_POWER)
                x_diff = int(np.cos(t) * POINT_POWER)
                is_x_negative_in = (x - x_diff) >= 0
                is_x_positive_in = (x + x_diff) < WIDTH
                is_y_negative_in = (y - y_diff) >= 0
                is_y_positive_in = (y + y_diff) < HEIGHT

                if is_y_positive_in and is_x_positive_in:
                    self.pixels[y + y_diff][x + x_diff] = (255, 255, 255)
                if is_y_negative_in and is_x_positive_in and y_diff > 0:
                    self.pixels[y - y_diff][x + x_diff] = (255, 255, 255)
                if is_y_positive_in and is_x_negative_in and x_diff > 0:
                    self.pixels[y + y_diff][x - x_diff] = (255, 255, 255)
                if is_y_negative_in and is_x_positive_in and y_diff > 0:
                    self.pixels[y - y_diff][x + x_diff] = (255, 255, 255)