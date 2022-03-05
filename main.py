import pygame
import time
import math

pygame.init()

screenX = 1200
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, 270)
planets = []

originalBabyImg = pygame.image.load("Baby.png")
babyImg = pygame.transform.scale(originalBabyImg, (30, 30))
bigBabyImg = pygame.transform.scale(originalBabyImg, (200, 200))

def drawBaby(x, y):
    screen.blit(babyImg, (x - 15, y - 15))

def drawBigBaby(x, y):
    screen.blit(bigBabyImg, (x - 100, y - 100))
running = True

def drawBackground():
    screen.fill((0, 0, 0))

def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))

def addPlanet(imageName,size):
    planets.append([imageName,size])

def importPlanets(planetArray): #planetArray must be a 2d array of planets
    planetLocations = []
    loc = [screenX - 20, screenY -75]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0]-planet[1], loc[1]])
        loc[0] = loc[0] - 50 - 2 * planet[1]
        print(loc)
    return planetLocations

def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1]*2, planet[1]*2))
    planetImg = pygame.transform.rotate(planetImg, 90)
    planetImg = pygame.transform.rotate(planetImg, 90)
    screen.blit(planetImg,(planet[2]-planet[1], planet[3]-planet[1]))


def drawBigPlanet(x, y):
    bigPlanet = pygame.image.load("Planet1.png")
    bigPlanet = pygame.transform.scale(bigPlanet, (400, 400))
    screen.blit(bigPlanet, (x-200, y-200))

def drawPlanetBarRect():
    planetBarRect = pygame.image.load("planetBar.png")
    planetBarRect = pygame.transform.scale(planetBarRect, (screenX,150))
    screen.blit(planetBarRect,(0,screenY - 150))

def getDistance(baby, planet):
    return math.sqrt((babyCoords[0]-planet[2])**2 + (babyCoords[1] - planet[3])**2)

def detectCollision(baby, planet):
    distance = getDistance(baby, planet)
    if distance < planet[1] + 15:
        return True
    else:
        return False

def mainMenu():
    font = pygame.font.Font("freesansbold.ttf",32)
    text = font.render("Project Megamind", True,(100,100,150))
    text2 = font.render("Press Space to Begin", True, (200,200,200))
    textRect = text.get_rect()
    textRect.center = (600,100)
    textRect2 = text2.get_rect()
    textRect2.center = (600,500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu=False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu=False
                if event.key == pygame.K_SPACE:
                    inMenu=False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigBaby(600, 300)
        pygame.display.update()


def moveBaby(player, planets, gap, speed):

    player[0] += player[2]*gap*speed
    #player[3] = 0
    for planet in planets:
        if planet[3] < 450:
            if getDistance(player, planet) < 2500:
                player[3] -= (player[1] - planet[3])*planet[1]/((getDistance(player, planet)**2)*5)
                player[2] -= (player[0] - planet[2])*planet[1]/((getDistance(player, planet)**2)*5)
    player[1] += player[3]*gap*speed
    return player

def firstLevel():
    font = pygame.font.Font("freesansbold.ttf",32)
    text = font.render("Level 1", True,(255,255,255))
    text2 = font.render("Press Space to Begin", True, (200,200,200))
    textRect = text.get_rect()
    textRect.center = (600,100)
    textRect2 = text2.get_rect()
    textRect2.center = (600,500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu=False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu=False
                if event.key == pygame.K_SPACE:
                    inMenu=False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300)
        pygame.display.update()



def start1():
    global planets
    global player
    global prevTime
    global currentTime
    global speed
    global fired
    global babyCoords
    global mousePressed
    global grabbedPlanet
    global grabbingPlanet
    global lastCursorLoc
    global collided
    planets = []
    firstLevel()
    player = [20, (screenY - 150) / 2 - 25, 0, 0]
    addPlanet("Planet1.png",70)
    addPlanet("Planet2.png",40)
    addPlanet("Planet3.png",50)
    addPlanet("Planet4.png",60)
    print(planets)
    planets = importPlanets(planets)
    print(planets)
    prevTime = 0
    currentTime = time.time()
    speed = 100
    babyCoords = [-200, -200, 0, 0]
    fired = False
    mousePressed = False
    grabbedPlanet = 0
    grabbingPlanet = False
    lastCursorLoc = pygame.mouse.get_pos()
    collided = False
    global starting
    starting = False

mainMenu()
completed = False
while not completed:
    running = True
    starting = True
    while running:
        if starting:
            start1()

        if not collided:
            prevTime = currentTime
            currentTime = time.time()
            gap = currentTime - prevTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    completed = True
                    quick = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        completed = True
                        quick = True

                    if event.key == pygame.K_s:
                        player[3] = 5
                    if event.key == pygame.K_w:
                        player[3] = -5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player[3] = 0
                    if event.key == pygame.K_SPACE:
                        if not fired:
                            fired = True
                            babyCoords = []
                            for coord in player:
                                babyCoords.append(coord)
                            babyCoords[0] += 75
                            babyCoords[1] += 25
                            babyCoords[2] = 5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePressed = True
                    if grabbingPlanet == True:
                        overlap = False
                        for planetIndex in (0, len(planets) - 1, 1):
                            if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                    planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                  planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                  planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                1] and planetIndex != grabbedPlanet:
                                overlap = True
                        if not overlap:
                            grabbingPlanet = False
                    else:
                        for planetIndex in range(len(planets)):
                            if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                    planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                  planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                  planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][1]:
                                grabbedPlanet = planetIndex
                                grabbingPlanet = True;

                if event.type == pygame.MOUSEBUTTONUP:
                    mousePressed = False

            move = player[1] + player[3]*speed*gap
            if move < 400 and move > 0:
                player[1] = move

        drawBackground()
        drawPlanetBarRect()
        drawPlayer(player[0], player[1])
        if grabbingPlanet:
            planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (pygame.mouse.get_pos()[0] - lastCursorLoc[0])
            planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (pygame.mouse.get_pos()[1] - lastCursorLoc[1])
        for planet in planets:
            drawPlanet(planet)
            if detectCollision(babyCoords, planet):
                collided = True

        if not collided:
            if fired:
                babyCoords = moveBaby(babyCoords, planets, gap, speed)
                print(babyCoords)
                if babyCoords[0] >=1200:
                    completed = True
                    quick = False
        else:
            time.sleep(2)
            running = False
        drawBaby(babyCoords[0], babyCoords[1])
        lastCursorLoc = pygame.mouse.get_pos()
        pygame.display.update()
        if completed:
            if not quick:
                time.sleep(2)
            running = False
