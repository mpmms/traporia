from .trap import Trap
import pygame
class MSpike(Trap):
    def __init__(self, display, x, y, coor):
        super().__init__(display, x, y, type="mspike")
        self.image = pygame.image.load("././assets/spike.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.width = 32
        self.height = 32
        self.coor = coor
    def check(self, player):
        return True if player[0] >= self.coor[0] and player[1] <= self.coor[1] else False
