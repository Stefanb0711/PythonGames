import pygame
from PIL import Image
import random
import time

"""win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Space Invaders")
"""
background = pygame.image.load("Pics/StarBackground.gif")
background = pygame.transform.scale(background, (1000, 750))


RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Player:
    def __init__(self):
        self.x = 500
        self.y = 650
        self.width = 40
        self.height = 60
        self.vel = 5
        self.left = False
        self.right = False
        self.space = False
        self.player = pygame.image.load("Pics/Rakete.png")
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_x = self.x + 55
        self.bullet_y = self.y
        self.shoot_once = False
        self.abgefeuert = True
        self.stroke_enemy = False
        self.bullets = []

    def draw(self, win):
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))

        if self.left:
            win.blit(self.player, (self.x, self.y))

        elif self.right:
            win.blit(self.player, (self.x, self.y))

        else:
            win.blit(self.player, (self.x, self.y))

        if self.space:

            #self.shoot(win)
            self.shoot(win)
            self.space = False
        else:
            pass
            """for bullet in self.bullets:

                bullet[1] -= 10
                pygame.draw.rect(win, RED, (bullet[0], bullet[1], self.bullet_width, self.bullet_height))

                if bullet[1] < 0:
                    bullet[0] = self.x
                    bullet[1] = self.y
                    self.bullets.remove(bullet)

                    #self.abgefeuert = False
                    #self.space = False
                    #self.stroke_enemy = False

                elif self.stroke_enemy:
                    bullet[0] = self.x + 55
                    bullet[1] = self.y
                    self.bullets.remove(bullet)
                    #self.abgefeuert = False
                    #self.space = False
                    self.stroke_enemy = False"""



    def shoot(self, win):
        if self.space:

            if not self.abgefeuert:
                self.bullet_x = self.x + 55
                self.bullet_y = self.y
                self.bullets.append([self.bullet_x, self.bullet_y])

                #self.abgefeuert = True
            print(self.bullets)

            """for bullet in self.bullets:

                if bullet[1] < 0:
                    bullet[0] = self.x
                    self.abgefeuert = False
                    self.space = False

                elif self.stroke_enemy:
                    bullet[0] = self.x + 55
                    bullet[1] = self.y
                    self.abgefeuert = False
                    self.space = False
                    self.stroke_enemy = False"""

            self.abgefeuert = False
            self.space = False

    def shoot_more_bullets(self, win):
        if self.space:

            if not self.abgefeuert:
                self.bullet_x = self.x + 55
                self.bullet_y = self.y
                self.bullets.append([self.bullet_x, self.bullet_y])

                #self.abgefeuert = True
            print(self.bullets)

            """for bullet in self.bullets:

                if bullet[1] < 0:
                    bullet[0] = self.x
                    self.abgefeuert = False
                    self.space = False

                elif self.stroke_enemy:
                    bullet[0] = self.x + 55
                    bullet[1] = self.y
                    self.abgefeuert = False
                    self.space = False
                    self.stroke_enemy = False"""

            self.abgefeuert = False
            self.space = False







class Enemy:
    def __init__(self):
        self.x_position_enemys_start = 150
        self.y_position_enemys_start = -70
        self.enemy_pic = pygame.image.load("Pics/Enemy1.png")
        self.enemys = []
        self.steps = 120
        self.direction = 1
        #self.rechter_rand = 0
        self.bullets = []
        self.bullet_width = 10
        self.bullet_height = 20


        x_start = 10
        y_start = -70

        for _ in range(3):
            y_start += 100
            x_position = x_start
            for _ in range(5):
                self.enemys.append([x_position, y_start])
                x_position += 120

        self.rechter_rand = self.enemys[14][0]


    def draw(self, win):


        for enemy_position in self.enemys:
            enemy_position[0] += self.direction * 2
            self.rechter_rand += self.direction * 2
            win.blit(self.enemy_pic, enemy_position)

            if enemy_position[0] >= 900:
                self.direction = -1
                win.blit(self.enemy_pic, enemy_position)

            elif enemy_position[0] <= 0:
                self.direction = 1
                win.blit(self.enemy_pic, enemy_position)


        """if self.rechter_rand >= 900:
            self.direction = -1
            for enemy_position in self.enemys:

                win.blit(self.enemy_pic, enemy_position)
                #enemy_position[0] -= 120


        elif self.enemys[0][0] <= 0:
            self.direction = 1
            for enemy_position in self.enemys:

                win.blit(self.enemy_pic, enemy_position)
                enemy_position[0] += 120"""


        """for _ in range(1,5):
            for enemy_position in self.enemys:

                win.blit(self.enemy_pic, enemy_position)
                enemy_position[0] += 120

        for _ in range(5,1, -1):
            for enemy_position in self.enemys:

                enemy_position[0] -= 120"""

    def shoot(self, win):
        random_enemy = random.randint(0, len(self.enemys)-1)
        print(random_enemy)
        self.enemys[random_enemy]
        #bullet = [random_enemy[0], random_enemy[1]]
        self.bullets.append([self.enemys[random_enemy][0], self.enemys[random_enemy][1]])

        for enemy_bullet in self.bullets:
            enemy_bullet[1] += 10

            if enemy_bullet[1] >= 800:
                self.bullets.remove(enemy_bullet)
            elif enemy_bullet:

                pygame.draw.rect(win, RED, (enemy_bullet[0], enemy_bullet[1],self.bullet_width, self.bullet_height))




"""class StartWindow:
    def __init__(self):
        self.win_start = pygame.display.set_mode((1000,800))
        self.button_width = 200
        self.button_height = 100
        self.start_game = False

        self.background = pygame.image.load("Pics/StarBackground.gif")
        self.background = pygame.transform.scale(background, (1000, 750))

        pygame.display.set_caption("Space Invaders")
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/BackgroundMusic.mp3")
        pygame.mixer.music.play(-1)
        #self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


    def draw(self):
        self.win_start.blit(self.background,(0,0) )
        pygame.draw.rect(self.win_start, RED, (500, 400, self.button_width, self.button_height))
        #self.win_start.blit(self.start_button_rect, (500, 400))

"""



