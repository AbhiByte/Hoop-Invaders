import pygame

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hoop-Invaders --alpha 1.00")
background = pygame.image.load("background.jpg")
FPS = 60
def draw_bg():
    WIN.blit(background, (0, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    draw_bg()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()




if __name__ == '__main__':
    main()
