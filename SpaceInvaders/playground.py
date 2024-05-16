import pygame
import sys

pygame.init()

win = pygame.display.set_mode((1000, 800))

font = pygame.font.Font("Fonts/AldotheApache.ttf", 24)

clock = pygame.time.Clock()

def timer_before_game_starts():
    countdown = 3
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

            timer_surface = font.render(f"{countdown}", True, (255, 255, 255))
            timer_rect = timer_surface.get_rect(center=(1000 // 2, 800 - 300))
            win.blit(timer_surface, timer_rect)
            pygame.display.update()

            # Verzögere das Programm für eine Sekunde, damit der Benutzer den Countdown sehen kann
            pygame.time.delay(1000)

        # Überprüfe auf Beenden des Spiels


while True:
    timer()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

