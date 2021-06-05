import pygame
import os
import time
import random
pygame.font.init()
#Screen
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cRona-Invaders --alpha 1.00")

#Images
background_image = pygame.transform.scale(pygame.image.load(os.path.join("Images", "background.jpg")), (WIDTH, HEIGHT))
player_image = pygame.image.load(os.path.join("Images", "playerVirus.png"))
enemy_image = pygame.image.load(os.path.join("Images", "enemyVirus.png"))

class Virus:
    def __init__ (self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_image = player_image
        self.enemy_image = enemy_image
        self.virus_img = enemy_image
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
        self.player_image = player_image
        self.mask = pygame.mask.from_surface(self.player_image)
        self.max_health = health
class Enemy(Virus):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.virus_image = enemy_image
        self.mask = pygame.mask.from_surface(self.virus_image)

    def move(self, vel):
        self.y += vel
#Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont("comicsans", 50)
    player_vel = 5
    level = 0
    lives = 5

    enemy_vel = 1
    enemies = []
    wave_length = 5

    player = Virus(300, 650)
    def redraw_window():
        WIN.blit(background_image, (0, 0))
        #Drawing text
        livesLabel = mainFont.render(f"Lives: {lives}", 1, (255,0,0))
        levelLabel = mainFont.render(f"Level: {level}", 1, (0, 255, 0))

        WIN.blit(livesLabel, (10, 10))
        WIN.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100))
                enemies.append(enemy)

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

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        redraw_window()
    pygame.quit()




if __name__ == '__main__':
    main()
