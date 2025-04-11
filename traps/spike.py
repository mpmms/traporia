from .trap import Trap
import pygame
class Spike(Trap):
    def __init__(self, display, x, y):
        super().__init__(display, x, y, type="spike")
        self.image = pygame.image.load("././assets/spike.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.width = 32
        self.height = 32
