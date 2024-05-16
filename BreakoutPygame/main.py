import pygame
from GameElements import Player, game_over, Ball, Obstacles
import time
import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

pygame.init()

start_win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start_game = False

font_timer = pygame.font.Font("Fonts/AldotheApache.ttf", 40)
font = pygame.font.Font("Fonts/AldotheApache.ttf", 24)

background = pygame.image.load("Bilder/Hintergrund.png")
start_button = pygame.image.load("Bilder/HolzSchildStart.png")

start_button_width = 1920 / 8
start_button_height = 960 / 8

start_button_rect = start_button.get_rect(center=(start_button_width,start_button_height))

#Font


start_button = pygame.transform.scale(start_button, (start_button_width, start_button_height))
background = pygame.transform.scale(background, (600, 800))

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
            timer_rect = timer_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 500))
            win.blit(timer_surface, timer_rect)

            #Spielbeschreibung
            description_text_surface = font.render(
                "Press the arrow keys to catch the ball", True,
                (255, 255, 255))
            description_text_rect = description_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 400))
            win.blit(description_text_surface, description_text_rect)

            pygame.display.update()

            # Verzögere das Programm für eine Sekunde, damit der Benutzer den Countdown sehen kann
            pygame.time.delay(1000)

        # Überprüfe auf Beenden des Spiels

def redraw_start_window():
    start_win.fill((0,0,0))
    start_win.blit(background, (0, 0))
    start_win.blit(start_button, (300 - start_button_width / 2, 300))


    pygame.display.update()


while not start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #start_game = True
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                start_game = True

                break



    redraw_start_window()





win = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()




player = Player()
ball = Ball()
obstacle_manager = Obstacles()



def redrawGameWindow():

    player.draw(win=win)
    ball.draw(win=win, player=player, obstacles=obstacle_manager.obstacles)
    obstacle_manager.draw(win=win)


    pygame.display.update()

if start_game:
    timer_before_game_starts()
    #count_down_before_game_starts()
    while not game_over:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > player.border_padding:
            player.left = True
            player.right = False
            player.x -= player.vel

        elif keys[pygame.K_RIGHT] and player.x < 600 - player.width - player.border_padding:
            player.right = True
            player.left = False
            player.x += player.vel

        else:
            player.left = False
            player.right = False

        redrawGameWindow()


