import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (70, 70))
playerImg = pygame.transform.rotate(playerImg, 270)
player = [20, 1080/2 - 35, 0, 0]
planets = []

running = True

def drawBackground():
    screen.fill((0, 0, 0))

def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))

def addPlanet(imageName,size):
    planets.append([imageName,size])

def importPlanets(planetArray): #planetArray must be a 2d array of planets
    planetLocations = []
    loc = 0  # x position of next planet; gets updated after every planet placement
    for planet in planets:
        planetLocations.append([planet[0], planet[1], loc, 500])
        loc = loc + (planet[1] * 2)
    return planetLocations

def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1], planet[1]))
    planetImg = pygame.transform.rotate(planetImg, 270)
    screen.blit(planetImg,(planet[2],planet[3]))


def setup(locatedPlanets):
    for planet in locatedPlanets:
        drawPlanet(planet)



        




prevTime = 0
currentTime = time.time()
speed = 10
print("starting")
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

    print("working")

    drawBackground()
    print("working")
    drawPlayer(player[0], player[1])
    addPlanet("planet.png",100)
    addPlanet("planet.png",50)
    setup(importPlanets(planets))
    print("skipped")
    pygame.display.update()

