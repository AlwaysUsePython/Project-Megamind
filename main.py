import pygame
import time
import math

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
<<<<<<< Updated upstream
    loc = 200  # x position of next planet; gets updated after every planet placement
    for planet in planets:
        planetLocations.append([planet[0], planet[1], loc, 500])
        loc = loc + (planet[1] * 2)
=======
    loc = [screenX - 20, screenY -75]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0]-planet[1], loc[1]])
        loc[0] = loc[0] - 50 - 2 * planet[1]
        print(loc)
>>>>>>> Stashed changes
    return planetLocations

def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1]*2, planet[1]*2))
    planetImg = pygame.transform.rotate(planetImg, 270)
    planetImg = pygame.transform.rotate(planetImg, 270)
    screen.blit(planetImg,(planet[2]-planet[1], planet[3]-planet[1]))


<<<<<<< Updated upstream
def setup(locatedPlanets):
    for planet in locatedPlanets:
        drawPlanet(planet)



        




prevTime = 0
currentTime = time.time()
speed = 10
print("starting")
addPlanet("planet.png",100)
addPlanet("planet.png",50)
addPlanet("planet.png",100)
addPlanet("planet.png",50)
=======
def drawPlanetBarRect():
    planetBarRect = pygame.image.load("planetBar.png")
    planetBarRect = pygame.transform.scale(planetBarRect, (screenX,150))
    screen.blit(planetBarRect,(0,screenY - 150))


addPlanet("Planet1.png",30)
addPlanet("Planet2.png",30)
addPlanet("Planet3.png",30)
addPlanet("Planet4.png",30)
addPlanet("Planet1.png",30)
addPlanet("Planet1.png",30)
addPlanet("Planet1.png",30)
addPlanet("Planet1.png",30)
planets = importPlanets(planets)
prevTime = 0
currentTime = time.time()
speed = 100
mousePressed = False
grabbedPlanet = 0
grabbingPlanet = False;
lastCursorLoc = pygame.mouse.get_pos()

>>>>>>> Stashed changes
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True
            if grabbingPlanet == True:
                overlap = False
                for planetIndex in (0, len(planets) - 1, 1):
                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (planets[planetIndex][2] - lastCursorLoc[0]) + (planets[planetIndex][3] - lastCursorLoc[1]) * (planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][1] and planetIndex != grabbedPlanet:
                        overlap = True
                if not overlap:
                    grabbingPlanet = False
            else:
                for planetIndex in range(len(planets)):
                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0])*(planets[planetIndex][2] - lastCursorLoc[0]) + (planets[planetIndex][3] - lastCursorLoc[1])*(planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][1]:
                        grabbedPlanet = planetIndex
                        grabbingPlanet = True;


        if event.type == pygame.MOUSEBUTTONUP:
            mousePressed = False;



    player[0] += player[2]*gap*speed
    player[1] += player[3]*gap*speed

    print("working")

    drawBackground()
<<<<<<< Updated upstream
    print("working")
    drawPlayer(player[0], player[1])

    setup(importPlanets(planets))
    print("skipped")
    pygame.display.update()
=======
    drawPlanetBarRect()
    drawPlayer(player[0], player[1])
    if grabbingPlanet:
        planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (pygame.mouse.get_pos()[0] - lastCursorLoc[0])
        planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (pygame.mouse.get_pos()[1] - lastCursorLoc[1])
    for planet in planets:
        drawPlanet(planet)
    pygame.display.update()
    lastCursorLoc = pygame.mouse.get_pos()
<<<<<<< Updated upstream
>>>>>>> Stashed changes

=======
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
                        if (not fired) and (not grabbingPlanet):
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
                            if (math.sqrt((planets[planetIndex][2] - planets[grabbedPlanet][2]) * (
                                    planets[planetIndex][2] - planets[grabbedPlanet][2]) + (
                                                  planets[planetIndex][3] - planets[grabbedPlanet][3]) * (
                                                  planets[planetIndex][3] - planets[grabbedPlanet][3]))) < planets[planetIndex][
                                1] + planets[grabbedPlanet][1] and planetIndex != grabbedPlanet:
                                overlap = True
                        if not overlap:
                            grabbingPlanet = False
                    elif not fired:
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
>>>>>>> Stashed changes
