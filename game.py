#cRona Invaders game made using Pygame module of Python
#Latest additons: added laser class and started working on collision function
#To do on own: add title screen w/ button functionallity and add music, sound effects
#Big thanks to Tech With Tim for the tutorials!
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
background_image = pygame.transform.scale(pygame.image.load(os.path.join("Images", "backg.png")), (WIDTH, HEIGHT))
player_image = pygame.image.load(os.path.join("Images", "playerVirus.png"))
enemy_image = pygame.image.load(os.path.join("Images", "enemyVirus.png"))
laser_blue_image = pygame.image.load(os.path.join("Images", "pixel_laser_blue.png"))
laser_green_image = pygame.image.load(os.path.join("Images", "pixel_laser_green.png"))
laser_red_image = pygame.image.load(os.path.join("Images", "pixel_laser_red.png"))
laser_yellow_image = pygame.image.load(os.path.join("Images", "pixel_laser_yellow.png"))


class Laser:
    def __init__ (self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.vlit(self.img, (self.x, self.y))
    def move(self, vel):
        self.y += vel
    def offTheScreen(self, height):
        return not (self.y <= height and self.y >= 0)
        #return obj1.mask.overlap(obj2, (offset_x, offset_y)) != None
    def collision(self, obj):
        return collide(self, obj)

class Virus:
    COOLDOWN = 30

    def __init__ (self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_image = player_image
        self.enemy_image = enemy_image
        self.virus_img = enemy_image
        self.cool_down_counter  = 0
        self.laser_img = laser_red_image
        self.lasers = []

    def draw(self, window):
        window.blit(self.player_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    def move_lasers (self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.offTheScreen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

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
    def move_lasers (self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.offTheScreen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
class Enemy(Virus):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.virus_image = enemy_image
        self.mask = pygame.mask.from_surface(self.virus_image)

    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y))
#Main game loop
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    player_vel = 5
    laser_vel = 4
    level = 0
    lives = 5

    enemy_vel = 1
    enemies = []
    wave_length = 5

    lost = False
    lost_count = 0

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

        if lost:
            lost_label = lost_font.render("Loser!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

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
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        player.move_lasers(laser_vel, enemies)
        #redraw_window()
    pygame.quit()

#Home screen function To do: Add buttons and transition to main()
def home_screen():
    runn = True
    FPS = 60
    clock = pygame.time.Clock()
    mainFont = pygame.font.SysFont("comicsans", 100)

    WIN.blit(background_image, (0, 0))
    #Home screens texts
    start_text = "Start Game"
    instructions_text = "How To Play"
    credits_text = "Credits"
    #Creating home screen labels
    startLabel = mainFont.render(start_text, 1, (0,255,0))
    instructionsLabel = mainFont.render(instructions_text, 1, (0, 255, 0))
    creditsLabel = mainFont.render(credits_text, 1, (0, 255, 0))

    #Bliting to screen
    WIN.blit(startLabel, (WIDTH/2 - startLabel.get_width()/2, HEIGHT/2 - 100))
    WIN.blit(instructionsLabel, (WIDTH/2 - instructionsLabel.get_width()/2, HEIGHT/2))
    WIN.blit(creditsLabel, (WIDTH/2 - creditsLabel.get_width()/2, HEIGHT/2 + 100))

    mouse = pygame.mouse.get_pos()
    while runn:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runn = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[1] <= WIDTH/2:
                    main()
    if runn == False:
        pygame.quit()


if __name__ == '__main__':
    #main()

    home_screen()
