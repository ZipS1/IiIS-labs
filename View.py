from PIL import Image


class View:
    def __init__(self, screen_size):
        self.img = Image.new('RGB', screen_size)

    def run(self, pixels):
        for i, row in enumerate(pixels):
            for j, pixel in enumerate(row):
                self.img.putpixel((i, j), pixel)
                
        self.img.show()
