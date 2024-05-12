from View import View
from Model import Model

WIDTH, HEIGHT = 600, 600
EDGE_OFFSET = 20
POINT_RADIUS = 5


class Controller:
    def __init__(self, N):
        self.model = Model(N, (WIDTH, HEIGHT), EDGE_OFFSET)
        self.view = View((WIDTH, HEIGHT), POINT_RADIUS)
        self.pixels = []

    def run(self):
        self.model.generate_point_coords()
        self.view.run(self.model.get_point_coords())
