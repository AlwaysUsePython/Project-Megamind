import pygame
import time

pygame.init()

screenX = 1200
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, 270)
player = [20, (screenY-150)/2 - 25, 0, 0]

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
    loc = []  # x position of next planet; gets updated after every planet placement
    for planet in planets:
        planetLocations.append([planet[0], planet[1], loc, 500])
        loc = loc + (planet[1] * 2)
    return planetLocations

def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1], planet[1]))
    planetImg = pygame.transform.rotate(planetImg, 270)
    screen.blit(planetImg,(planet[2],planet[3]))


def drawPlanetBarRect():
    planetBarRect = pygame.image.load("planetBar.png")
    planetBarRect = pygame.transform.scale(planetBarRect, (screenX,150))
    screen.blit(planetBarRect,(0,screenY - 150))

def drawPlanetBar(planetArray):
    drawPlanetBarRect()
    for planet in planetArray:
        drawPlanet(planet)


addPlanet("Planet1.png",100)
addPlanet("Planet2.png",50)
addPlanet("Planet3.png",70)
addPlanet("Planet4.png",90)
planets = importPlanets(planets)
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
    drawPlanetBarRect()
    for planet in planets:
        drawPlanet(planet)
    pygame.display.update()
