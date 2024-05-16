import random

import pygame
from PIL import Image
from GameElements import Player, RED, WHITE, Enemy

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
pygame.mixer.init()
pygame.mixer.music.load("Sounds/BackgroundMusic.mp3")
pygame.mixer.music.play(-1)

font_timer = pygame.font.Font("Fonts/AldotheApache.ttf", 40)
font = pygame.font.Font("Fonts/AldotheApache.ttf", 24)


background = pygame.image.load("Pics/StarBackground.gif")
background = pygame.transform.scale(background, (1000, 750))
player = pygame.image.load("Pics/Rakete.png")
enemy_1 = pygame.image.load("Pics/Enemy1.png")


player = Player()



game_over = False

clock = pygame.time.Clock()

def timer_before_game_starts():
    countdown = 4
    last_tick = pygame.time.get_ticks()

    while countdown > 0:
        # Berechne vergangene Zeit seit dem letzten Update
        current_tick = pygame.time.get_ticks()
        delta_time = current_tick - last_tick

        # Wenn eine Sekunde vergangen ist, aktualisiere den Countdown
        if delta_time >= 1000:
            countdown -= 1
            last_tick = current_tick

            # Zeichne den Countdown auf das Fenster
            win.fill((0, 0, 0))
            win.blit(background, (0, 0))

            timer_surface = font_timer.render(f"{countdown}", True, (255, 255, 255))
            timer_rect = timer_surface.get_rect(center=(1000 // 2, 800 - 600))
            win.blit(timer_surface, timer_rect)

            #Spielbeschreibung
            description_text_surface = font.render(
                "Press the arrow keys for moving and space for shooting.\n Dont get hit by the enenmys", True,
                (255, 255, 255))
            description_text_rect = description_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))
            win.blit(description_text_surface, description_text_rect)

            pygame.display.update()

            # Verzögere das Programm für eine Sekunde, damit der Benutzer den Countdown sehen kann
            pygame.time.delay(1000)

        # Überprüfe auf Beenden des Spiels

def info_before_game_starts():
    #win.blit(background, (0, 0))
    description_text_surface = font_timer.render("Press the arrow keys for moving and space for shooting.\n Dont get hit by the enenmys", True, (255, 255, 255))
    description_text_rect = description_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 300))
    pygame.display.update()
    pygame.time.delay(3000)




enemys = Enemy()

def redrawGameWindow():
    global game_over
    win.blit(background, (0,0))
    player.draw(win)
    #enemy_creator()
    enemys.draw(win)



    if enemys.enemys == []:
        game_over = True

    """for enemy in enemys.enemys:
        for bullet in player.bullets:
            bullet[1] -= 10
            pygame.draw.rect(win, RED, (bullet[0], bullet[1], player.bullet_width, player.bullet_height))

            if bullet[1] < 0:
                bullet[0] = player.x
                bullet[1] = player.y
                player.bullets.remove(bullet)

            if (enemy[0] - 70 <= bullet[0] <= enemy[0] + 70) and (enemy[1] - 50 <= bullet[1] <= enemy[1] + 50):
                enemys.enemys.remove(enemy)
                player.stroke_enemy = True
                bullet[0] = player.x + 55
                bullet[1] = player.y
                player.bullets.remove(bullet)
                # self.abgefeuert = False
                # self.space = False
                player.stroke_enemy = False"""

    if not player.bullets == []:
        for bullet in player.bullets:
            bullet[1] -= 10
            pygame.draw.rect(win, RED, (bullet[0], bullet[1], player.bullet_width, player.bullet_height))

            for enemy in enemys.enemys:
                if (enemy[0] - 70 <= bullet[0] <= enemy[0] + 70) and (enemy[1] - 50 <= bullet[1] <= enemy[1] + 50):
                    enemys.enemys.remove(enemy)
                    #player.stroke_enemy = True
                    #bullet[0] = player.x + 55
                    #bullet[1] = player.y
                    player.bullets.remove(bullet)
                    # self.abgefeuert = False
                    # self.space = False
                    #player.stroke_enemy = False

                elif bullet[1] < 0:
                    bullet[0] = player.x
                    bullet[1] = player.y
                    player.bullets.remove(bullet)

    for enemy_bullet in enemys.bullets:
        enemy_bullet[1] += 10

        if enemy_bullet[0] - 94 <= player.x <= enemy_bullet[0] + 10 and enemy_bullet[1] - 134 <= player.y + 50 <= enemy_bullet[1] + 20:
            enemys.bullets.remove(enemy_bullet)
            print("Player wurde getroffen")
            game_over = True

        if enemy_bullet[1] >= 800:
            enemys.bullets.remove(enemy_bullet)



        elif len(enemys.bullets) >= 5:
            enemys.bullets.pop(0)


        pygame.draw.rect(win, RED, (enemy_bullet[0], enemy_bullet[1], enemys.bullet_width, enemys.bullet_height))


    frequency_enemy_bullets = random.randint(0,100)

    if frequency_enemy_bullets <= 1:
        print(enemys.bullets)

        random_enemy = random.randint(0, len(enemys.enemys) - 1)
        #enemys.enemys[random_enemy]
        enemys.bullets.append([enemys.enemys[random_enemy][0], enemys.enemys[random_enemy][1]])





        """elif enemy_bullet[0] - 50 <= player.x <= enemy_bullet[0] + 50 and enemy_bullet[1] - 50 <= player.y + 50:
                enemys.bullets.remove(enemy_bullet)"""





    #enemys.shoot(win)



    pygame.display.update()



timer_before_game_starts()

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.space = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        print(f"Player x: {player.x}")
        print(f"Bullet_x : {player.bullet_x}")
        player.left = True
        player.right = False
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x < 1000 - player.width - player.vel:
        print(f"Player x: {player.x}")
        print(f"Bullet_x : {player.bullet_x}")

        player.left = False
        player.right = True
        player.x += player.vel

    elif keys[pygame.K_SPACE]:
        #player.space = True
        pass
    else:
        player.left = False
        player.right = False


    redrawGameWindow()
