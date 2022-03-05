import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (70, 70))
playerImg = pygame.transform.rotate(playerImg, 270)
player = [20, 1080/2 - 35, 0, 0]


running = True

def drawBackground():
    screen.fill((0, 0, 0))

def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))

prevTime = 0
currentTime = time.time()
speed = 100
while running:

    prevTime = currentTime
    currentTime = time.time()
    gap = currentTime - prevTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_d:
                player[2] = 5
            if event.key == pygame.K_a:
                player[2] = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player[2] = 0

    player[0] += player[2]*gap*speed
    player[1] += player[3]*gap*speed



    drawBackground()
    drawPlayer(player[0], player[1])
    pygame.display.update()

