import pygame


class Bar:

    factor = 1

    @staticmethod
    def set_factor(factor):
        Bar.factor = factor

    def __init__(self, x, y, width, value):

        self.x = x
        self.y = y

        self.width = width
        self.height = None

        self.value = value
        self.pos = 0

        self.color = (50, 50, 50)

        self.points = ()

    def set_points(self):
        self.height = self.value * Bar.factor

        self.points = ((self.x, self.y),
                       (self.x + self.width, self.y),
                       (self.x + self.width, self.y - self.height),
                       (self.x, self.y - self.height))

    def set_x(self, x):
        self.x = x

    def set_value(self, value):
        self.value = value

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def update_x(self, space, width, side_buffer):
        self.x = ((space - width) / 2 + side_buffer + self.pos * space)
        self.set_points()

    def update_x(self, pos, space, width, side_buffer):
        self.x = ((space - width) / 2 + side_buffer + pos * space)
        self.set_points()

    def set_color(self, color):
        self.color = color

    def get_value(self):
        return self.value

    def draw(self, win):
        pygame.draw.polygon(win, self.color, self.points)


