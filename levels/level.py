import pygame
from thepalette import Color
pygame.init()
class Level:
    def __init__(self, display, end_command, color):
        self.display = pygame.display.set_mode(display)
        self.gravity = 0.6
        self.y_v = 0
        c_down = pygame.image.load("././assets/character_down.png")
        c_up = pygame.image.load("././assets/character_up.png")
        bg_1 = pygame.image.load("././assets/bg_1.png")
        door = pygame.image.load("././assets/door.png")
        self.font = pygame.font.Font("././assets/Mojang.ttf", 50)
        self.jump_effect = pygame.mixer.Sound("././assets/jump.mp3")
        self.end_efffect = pygame.mixer.Sound("././assets/end.mp3")
        bg_1 = pygame.transform.scale(bg_1, (1200, 600))
        c_up = pygame.transform.scale(c_up, (150, 150))
        c_down = pygame.transform.scale(c_down, (150, 150))
        self.door = pygame.transform.scale(door, (150, 150))
        self.assets = [c_down, c_up, bg_1]
        self.character = self.assets[1]
        self.traps = []
        self.color = color
        self.end_command = end_command
    def run(self):
        done = False
        speed = 4
        c_type = "up"
        c_loc = [200, 297]
        is_left = False
        is_right = False
        is_jumping = False
        on_ground = True
        y_v = 0
        dr_y = 297
        is_end = False
        lines = [417] * 12
        while not done:
            self.display.fill(self.color.get_rgb())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        c_type = "down"
                        speed = 2
                    if event.key == pygame.K_LEFT:
                        is_left = True
                    if event.key == pygame.K_RIGHT:
                        is_right = True
                    if event.key == pygame.K_SPACE and on_ground:
                        self.jump_effect.play()
                        is_jumping = True
                        on_ground = False
                        y_v = -12
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        c_type = "up"
                        speed = 4
                    if event.key == pygame.K_LEFT:
                        is_left = False
                    if event.key == pygame.K_RIGHT:
                        is_right = False
            
            if is_left:
                c_loc = [c_loc[0] - speed, c_loc[1]]
            if is_right:
                c_loc = [c_loc[0] + speed, c_loc[1]]
            
            if -57 > c_loc[0]:
                c_loc = [-57, c_loc[1]]
            if 1110 < c_loc[0]:
                c_loc = [1110, c_loc[1]]
            if c_loc[0] >= 1000:
                dr_y += 4
                is_end = True
            if dr_y >= 600:
                self.end_efffect.play()
                self.end_command()
            if is_jumping:
                c_loc = [c_loc[0], c_loc[1] + y_v]
                y_v += self.gravity
                
                if c_loc[1] >= 297:
                    c_loc = [c_loc[0], 297]
                    is_jumping = False
                    y_v = 0
                    on_ground = True
            if c_loc[1] >= 600:
                done = True
            for i in range(12):
                lines[i] = lines[i] + 5 if lines[i] > 417 else lines[i]
            for i in range(12):
                pygame.draw.line(self.display, (0, 0, 0), (i * 100, lines[i]), ((i + 1) * 100, lines[i]),10)
            character = self.assets[1] if c_type == "up" else self.assets[0]
            self.display.blit(self.door, (1000, dr_y))
            if not is_end:
                self.display.blit(character, c_loc if c_type == "up" else [c_loc[0], c_loc[1] + 15])
            for trap in self.traps:
                margin_x = 60
                if trap.type == "void":
                    if trap.check((c_loc[0], c_loc[1])):
                        lines[trap.num - 1] += 1
                    if lines[trap.num - 1] > 417:
                        x, y = c_loc
                        if (trap.num - 1) * 100 - 65 <= x <= (trap.num - 1) * 100 + 25 and y >= 297:
                            c_loc[1] += 10
                        elif (trap.num - 1) * 100 - 65 > x > (trap.num - 1) * 100 + 25:
                            c_loc[1] = 297
                elif trap.type == "mspike":
                    if trap.check((c_loc[0], c_loc[1])):
                        if (trap.x <= c_loc[0] + 150 - margin_x and 
                        trap.x + trap.width >= c_loc[0] + margin_x and 
                        trap.y <= c_loc[1] + 110 and 
                        trap.y + trap.height >= c_loc[1] + 40):
                            done = True
                        self.display.blit(trap.image, (trap.x, trap.y))

                else:
                    if (trap.x <= c_loc[0] + 150 - margin_x and 
                        trap.x + trap.width >= c_loc[0] + margin_x and 
                        trap.y <= c_loc[1] + 110 and 
                        trap.y + trap.height >= c_loc[1] + 40):
                            done = True
                    self.display.blit(trap.image, (trap.x, trap.y))
            pygame.display.update()
            pygame.time.Clock().tick(60)
        quit()