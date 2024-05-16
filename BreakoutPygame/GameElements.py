import pygame
from PIL import Image
import random
import math


game_over = False

RED = (255, 0, 0)
BLUE = (0, 0 , 255)
WHITE = (255, 255, 255)

background = pygame.image.load("Bilder/Hintergrund.png")
background = pygame.transform.scale(background, (600, 800) )

def calculate_bounce_angle(incoming_angle, surface_angle):
    incoming_angle_rad = math.radians(incoming_angle)
    surface_angle_rad = math.radians(surface_angle)

    surface_normal = (math.cos(surface_angle_rad), math.sin(surface_angle_rad))

    incidence_angle = math.acos(
        surface_normal[0] * math.cos(incoming_angle_rad) + surface_normal[1] * math.sin(incoming_angle_rad))

    # Berechne den reflektierten Winkel basierend auf dem Reflexionsgesetz
    reflected_angle = 2 * surface_angle_rad - incoming_angle_rad + math.pi

    # Konvertiere den Winkel in Grad zurück und stelle sicher, dass er im Bereich [0, 360) liegt
    reflected_angle_deg = math.degrees(reflected_angle) % 360

    return reflected_angle_deg


def abprallwinkel_berechnen(einfallswinkel, wandwinkel):
    einfallswinkel %= 360
    wandwinkel %= 360

    winkeldifferenz = einfallswinkel - wandwinkel
    ausfallwinkel = wandwinkel - winkeldifferenz
    ausfallwinkel = (ausfallwinkel + 360) % 360

    return ausfallwinkel



class Player:
    def __init__(self):
        self.x = 300
        self.y = 750
        self.width = 80
        self.height = 20
        self.border_padding = 5
        self.vel = 5
        self.left = False
        self.right = False



    def draw(self, win):
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))

        pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        """if self.left:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        elif self.right:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

        else:
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))
"""


class Ball:
    def __init__(self):

        self.x = 400
        self.y = 300
        self.start_position = [self.x, self.y]
        self.heading_degrees = random.randrange(20, 160)

        self.vel = 10



        self.heading_rad = math.radians(self.heading_degrees)





        self.radius = 25




    def draw(self, win, player, obstacles):
        global game_over


        velocity_x = self.vel * math.cos(self.heading_rad)
        velocity_y = self.vel * math.sin(self.heading_rad)


        self.x += velocity_x
        self.y += velocity_y


        if self.x >= 600 - self.radius or self.x <= 0 + self.radius:
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 90)

            self.heading_rad = math.radians(self.heading_degrees)

            #self.heading_angle = math.radians(self.heading_angle)



        elif self.y >= 800 :
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 180)
            #self.heading = math.degrees(self.heading_angle)
            self.heading_rad = math.radians(self.heading_degrees)

            game_over = True
            pygame.quit()

        elif self.y <= 0 + self.radius:
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 180)
            # self.heading = math.degrees(self.heading_angle)
            self.heading_rad = math.radians(self.heading_degrees)


        #Abprall an Spieler

        elif (self.x + self.radius - player.x) <= 110 and (self.x + self.radius - player.x > -10) and abs(self.y - player.y) < 30:
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 180)

            self.heading_rad = math.radians(self.heading_degrees)


        elif any((self.x + self.radius - obstacle[0] < 90) and (self.x + self.radius - obstacle[0] > -10) and abs(self.y - obstacle[1]) < 10 for obstacle in obstacles):
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 180)

            self.heading_rad = math.radians(self.heading_degrees)

            for obstacle in obstacles:
                if ((self.x + self.radius - obstacle[0] < 90) and (self.x + self.radius - obstacle[0] > -10) and abs(
                        self.y - obstacle[1]) < 10):
                    obstacles.remove(obstacle)

        elif any(
            (self.x + self.radius >= obstacle[0] and self.x + self.radius <= obstacle[0] + 60) and
            (abs(self.y - obstacle[1]) < 10) for obstacle in obstacles
        ):
            self.heading_degrees = abprallwinkel_berechnen(self.heading_degrees, 90)

            self.heading_rad = math.radians(self.heading_degrees)

            for obstacle in obstacles:
                if ((self.x + self.radius - obstacle[0] < 90) and (self.x + self.radius - obstacle[0] > -10) and abs(
                        self.y - obstacle[1]) < 10):
                    obstacles.remove(obstacle)
            """for obstacle in obstacles:

                obstacle_center_x = obstacle[0] + 30
                obstacle_center_y = obstacle[1] + 10

                distance_x = abs(self.x - obstacle_center_x)
                distance_y = abs(self.y - obstacle_center_y)

                if distance_x < (self.radius + 30) and distance_y < (self.radius + 10):
                    obstacles.remove(obstacle)"""


        pygame.draw.circle(surface=win, color=RED, center=(self.x, self.y), radius=self.radius)




class Obstacles:
    def __init__(self):
        self.number_of_obstacles = 10
        self.obstacles = []

        self.obstacle_width = 60
        self.obstacle_height = 20
        self.create_obstacles()

    def draw(self, win):
        for obstacle in self.obstacles:


            pygame.draw.rect(win, BLUE, (obstacle[0], obstacle[1], self.obstacle_width, self.obstacle_height))


    def create_obstacles(self):
        for obstacle in range(self.number_of_obstacles):
            obstacle_x = random.randrange(20, 580)
            obstacle_y = random.randrange(50, 400)

            """"""
            while any(-100 < abs(obstacle_x - other_obstacle[0]) < 100 and abs(obstacle_y - other_obstacle[1]) < 70 for other_obstacle in self.obstacles):

                obstacle_x = random.randrange(20, 580)
                obstacle_y = random.randrange(50, 400)

            self.obstacles.append([obstacle_x, obstacle_y])


class StartWindow:
    def __init__(self):
        self.win = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Breakout")

        self.start_game = False
        self.clock = pygame.time.Clock()


    def redraw_start_window(self):
        pass




