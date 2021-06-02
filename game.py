import pygame
import os
import time
import random
pygame.font.init()
#Screen
WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hoop-Invaders --alpha 1.00")

#Images
background_image = pygame.transform.scale(pygame.image.load(os.path.join("Images", "background.jpg")), (WIDTH, HEIGHT))
hoop_image = pygame.image.load(os.path.join("Images", "hoop.jpg"))
ball_image = pygame.image.load(os.path.join("Images", "ball.jpg"))
player_image = pygame.image.load(os.path.join("Images", "playerVirus.png"))

class Virus:
    def __init__ (self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_image = player_image
        self.ball_img = None
        self.balls = []
        self.coolDownCounter = 0

    def draw(self, window):
        window.blit(self.player_image, (self.x, self.y))

    def get_width(self):
        return self.player_image.get_width()

    def get_height(self):
        return self.player_image.get_height()

class Player(Virus):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.ball_img = ball_image
        self.mask = pygame.mask.from_surface(self.hoop_image)
        self.max_health = health
#Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont("comicsans", 50)
    player_vel = 5
    level = 1
    lives = 5

    player = Virus(300, 650)
    def redraw_window():
        WIN.blit(background_image, (0, 0))
        #Drawing text
        livesLabel = mainFont.render(f"Lives: {lives}", 1, (255,0,0))
        levelLabel = mainFont.render(f"Level: {level}", 1, (0, 255, 0))

        WIN.blit(livesLabel, (10, 10))
        WIN.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0:
             player.x -= player_vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
    pygame.quit()




if __name__ == '__main__':
    main()
