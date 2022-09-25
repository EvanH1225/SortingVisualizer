import pygame

pygame.init()

class Button:

    font = pygame.font.Font('freesansbold.ttf', 12)

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        r, g, b = color

        self.color = (r, g, b)
        self.highlighted_color = (min(r + 40, 255), min(g + 40, 255), min(b + 40, 255))

        self.highlighted = False

        self.text = ""
        self.textRect = None

    def set_text(self, text):
        self.text = Button.font.render(text, True, (255, 255, 255), None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x + self.width / 2, self.y + self.height / 2)

    def check_hover(self, mouse_pos):
        x, y = mouse_pos

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True

        return False

    def set_highlight(self, mouse_pos):
        if self.check_hover(mouse_pos):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, win):
        if self.highlighted:
            pygame.draw.rect(win, self.highlighted_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        win.blit(self.text, self.textRect)
