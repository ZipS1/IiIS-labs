import tkinter as tk


class View:
    def __init__(self, screen_size, point_radius):
        self.window = tk.Tk()
        self.window.title("Tower Coverage Map")
        self.canvas = tk.Canvas(
            self.window, width=screen_size[0], height=screen_size[1]
        )
        self.canvas.pack()
        self.point_radius = point_radius

    def run(self, point_coords):
        for point in point_coords:
            self.canvas.create_oval(
                point[0],
                point[1],
                point[0] + self.point_radius,
                point[1] + self.point_radius,
                fill="red",
            )
        self.window.mainloop()
