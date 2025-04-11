import pygame
pygame.init()
c_up = pygame.image.load("././assets/character_up.png")
bg = pygame.image.load("././assets/menu_poster.png")
bg = pygame.transform.scale(bg, (1200, 600))
font = pygame.font.Font("././assets/Mojang.ttf", 50)
menu = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Traporia")
pygame.display.set_icon(c_up)
def run():
    done = False
    while not done:
        menu.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import lvl1
        pygame.display.update()
        pygame.time.Clock().tick(60)