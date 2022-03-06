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

#asteroid object is [x, y, xDimension, yDimension] ALL BY TOP LEFT
astImg = pygame.image.load("Asteroids.png")

def drawAsteroid(asteroid):
    asteroidImg = pygame.transform.scale(astImg, (asteroid[2], asteroid[3]))
    screen.blit(asteroidImg, (asteroid[0], asteroid[1]))



originalBabyImg = pygame.image.load("Baby.png")
babyImg = pygame.transform.scale(originalBabyImg, (30, 30))
bigBabyImg = pygame.transform.scale(originalBabyImg, (200, 200))


explainScreen = pygame.image.load("Explanation.png")
explainScreen = pygame.transform.scale(explainScreen, (1000, 500))

def drawBaby(x, y):
    screen.blit(babyImg, (x - 15, y - 15))

def drawExplainScreen():
    screen.blit(explainScreen, (100, 50))

def drawBigBaby(x, y):
    screen.blit(bigBabyImg, (x - 100, y - 100))


def drawBackground():
    screen.fill((0, 0, 0))


def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))


def addPlanet(imageName, size):
    planets.append([imageName, size])


def importPlanets(planetArray):  # planetArray must be a 2d array of planets
    planetLocations = []
    loc = [1065, 525]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0] - planet[1], loc[1]])
        if loc == [1065, 525]:
            loc[0] = loc[0] - 280
        elif loc == [1065-280, 525]:
            loc[0] = loc[0] - 280
        elif loc == [1065 - 280 - 280, 525]:
            loc[0] -= 240
    return planetLocations


def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1] * 2, planet[1] * 2))
    if planet[0] != "Earth.png":
        planetImg = pygame.transform.rotate(planetImg, 90)
        planetImg = pygame.transform.rotate(planetImg, 90)
    screen.blit(planetImg, (planet[2] - planet[1], planet[3] - planet[1]))


def drawBigPlanet(x, y):
    bigPlanet = pygame.image.load("Planet1.png")
    bigPlanet = pygame.transform.scale(bigPlanet, (400, 400))
    screen.blit(bigPlanet, (x - 200, y - 200))


def drawPlanetBarRect():
    planetBarRect = pygame.image.load("planetBar.png")
    planetBarRect = pygame.transform.scale(planetBarRect, (screenX, 150))
    screen.blit(planetBarRect, (0, screenY - 150))


def getDistance(baby, planet):
    return math.sqrt((babyCoords[0] - planet[2]) ** 2 + (babyCoords[1] - planet[3]) ** 2)


def detectCollision(baby, planet):
    distance = getDistance(baby, planet)
    if distance < planet[1] + 15:
        return True
    else:
        return False


def mainMenu():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Project Megamind", True, (100, 100, 150))
    text2 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu = False
                finished = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    finished = True
                if event.key == pygame.K_SPACE:
                    inMenu = False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigBaby(600, 300)
        pygame.display.update()


def moveBaby(player, planets, gap, speed):
    player[0] += player[2] * gap * speed
    # player[3] = 0
    for planet in planets:
        if planet[3] < 450:
            if getDistance(player, planet) < 2500:
                player[3] -= (player[1] - planet[3]) * planet[1]*(gap*speed)**2 / ((getDistance(player, planet) ** 2) * 8)
                player[2] -= (player[0] - planet[2]) * planet[1]*(gap*speed)**2 / ((getDistance(player, planet) ** 2) * 8)
    player[1] += player[3] * gap * speed
    return player

def drawExplanation0():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Get the baby to planet Earth!", True, (255, 255, 255))
    text1 = font.render("Use the spacebar to launch the baby", True, (255, 255, 255))
    text2 = font.render("W and S move the ship on the y axis", True, (255, 255, 255))
    text3 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 350)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 500)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)


def drawExplanation1():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Avoid the asteroids!!", True, (255, 255, 255))
    text1 = font.render("Planets have gravitational pull.", True, (255, 255, 255))
    text2 = font.render("Use that to your advantage!", True, (255, 255, 255))
    text4 = font.render("Drag the planets onto the screen with your mouse", True, (255, 255, 255))
    text3 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 350)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 500)
    textRect4 = text4.get_rect()
    textRect4.center = (600, 450)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)


def drawExplanation2():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("This one's a bit harder!", True, (255, 255, 255))
    text1 = font.render("You may need to place a few more planets.", True, (255, 255, 255))
    text2 = font.render("Larger planets have larger gravitational pulls!", True, (255, 255, 255))
    text3 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 350)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 500)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)


def firstLevel():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 1", True, (255, 255, 255))
    text2 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                if event.key == pygame.K_SPACE:
                    inMenu = False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300)
        pygame.display.update()



def secondLevel():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 2", True, (255, 255, 255))
    text2 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                if event.key == pygame.K_SPACE:
                    inMenu = False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300)
        pygame.display.update()



def thirdLevel():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 3", True, (255, 255, 255))
    text2 = font.render("Press Space to Begin", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 100)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 500)
    inMenu = True
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                if event.key == pygame.K_SPACE:
                    inMenu = False
        drawBackground()
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300)
        pygame.display.update()

def detectAsteroidCollision(baby, asteroid):
    for i in range(asteroid[2]):
        if math.sqrt((baby[0] - asteroid[0]-i)**2 + (baby[1] - asteroid[1])**2) < 15:
            return True
        if math.sqrt((baby[0] - asteroid[0]-i)**2 + (baby[1] - asteroid[1]-asteroid[3])**2) < 15:
            return True
    for i in range(asteroid[3]):
        if math.sqrt((baby[0] - asteroid[0]-asteroid[2])**2 + (baby[1] - asteroid[1]-i)**2) < 15:
            return True
        if math.sqrt((baby[0] - asteroid[0])**2 + (baby[1] - asteroid[1]-i)**2) < 15:
            return True
    return False


# LEVEL 1
def start0(earthX, earthY):
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
    global asteroids
    asteroids = []
    planets = []
    firstLevel()
    player = [20, (screenY - 150) / 2 - 25, 0, 0]
    addPlanet("Planet1.png", 70)
    addPlanet("Planet2.png", 40)
    addPlanet("Planet3.png", 50)
    addPlanet("Planet4.png", 60)
    addPlanet("Earth.png", 100)
    planets = importPlanets(planets)
    planets[len(planets) - 1][2] = earthX
    planets[len(planets) - 1][3] = earthY
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

finished = False

mainMenu()
completed = False
while not completed and not finished:
    explained = False
    running = True
    starting = True
    while running:
        if starting:
            start0(1200, 225)

        if not collided:
            prevTime = currentTime
            currentTime = time.time()
            gap = currentTime - prevTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    completed = True
                    finished = True
                    quick = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        completed = True
                        quick = True
                        finished = True

                    if event.key == pygame.K_s:
                        player[3] = 5
                    if event.key == pygame.K_w:
                        player[3] = -5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player[3] = 0
                    if event.key == pygame.K_SPACE:
                        if not explained:
                            explained = True
                        elif not fired:
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
                            grabbingPlanet = False
                    else:
                        for planetIndex in range(len(planets)):
                            if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                    planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                  planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                  planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                1]:
                                grabbedPlanet = planetIndex
                                grabbingPlanet = True;

                if event.type == pygame.MOUSEBUTTONUP:
                    mousePressed = False

            move = player[1] + player[3] * speed * gap
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
                if planet[0] == "Earth.png":
                    completed = True
                    quick = False
                collided = True

        for asteroid in asteroids:
            if detectAsteroidCollision(babyCoords, asteroid):
                quick = False
                collided = True

        if not collided:
            if fired:
                move = moveBaby(babyCoords, planets, gap, speed)
                if (move[1] < 430 and move[1] > 0):
                    babyCoords = move
                else:
                    babyCoords = move
                    collided = True
                print(babyCoords)
                if babyCoords[0] >= 1200:
                    collided = True
                    quick = False
        else:
            time.sleep(2)
            running = False
        drawBaby(babyCoords[0], babyCoords[1])
        lastCursorLoc = pygame.mouse.get_pos()
        for asteroid in asteroids:
            drawAsteroid(asteroid)

        if not explained:
            drawExplainScreen()
            drawExplanation0()

        pygame.display.update()
        if completed:
            if not quick:
                time.sleep(2)
            running = False

# LEVEL 1
def start1(earthX, earthY):
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
    global asteroids
    asteroids = []
    asteroids.append([580, 100, 40, 250])
    planets = []
    secondLevel()
    player = [20, (screenY - 150) / 2 - 25, 0, 0]
    addPlanet("Planet1.png", 70)
    addPlanet("Planet2.png", 40)
    addPlanet("Planet3.png", 50)
    addPlanet("Planet4.png", 60)
    addPlanet("Earth.png", 100)
    planets = importPlanets(planets)
    planets[len(planets) - 1][2] = earthX
    planets[len(planets) - 1][3] = earthY
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

finished = False

completed = False
while not completed and not finished:
    explained = False
    running = True
    starting = True
    while running:
        if starting:
            start1(1200, 225)

        if not collided:
            prevTime = currentTime
            currentTime = time.time()
            gap = currentTime - prevTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    completed = True
                    finished = True
                    quick = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        completed = True
                        quick = True
                        finished = True

                    if event.key == pygame.K_s:
                        player[3] = 5
                    if event.key == pygame.K_w:
                        player[3] = -5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player[3] = 0
                    if event.key == pygame.K_SPACE:
                        if not explained:
                            explained = True
                        elif not fired:
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
                            grabbingPlanet = False
                    else:
                        for planetIndex in range(len(planets)):
                            if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                    planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                  planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                  planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                1]:
                                grabbedPlanet = planetIndex
                                grabbingPlanet = True;

                if event.type == pygame.MOUSEBUTTONUP:
                    mousePressed = False

            move = player[1] + player[3] * speed * gap
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
                if planet[0] == "Earth.png":
                    completed = True
                    quick = False
                collided = True

        for asteroid in asteroids:
            if detectAsteroidCollision(babyCoords, asteroid):
                quick = False
                collided = True

        if not collided:
            if fired:
                move = moveBaby(babyCoords, planets, gap, speed)
                if (move[1] < 430 and move[1] > 0):
                    babyCoords = move
                else:
                    babyCoords = move
                    collided = True
                print(babyCoords)
                if babyCoords[0] >= 1200:
                    collided = True
                    quick = False
        else:
            time.sleep(2)
            running = False
        drawBaby(babyCoords[0], babyCoords[1])
        lastCursorLoc = pygame.mouse.get_pos()
        for asteroid in asteroids:
            drawAsteroid(asteroid)

        if not explained:
            drawExplainScreen()
            drawExplanation1()

        pygame.display.update()
        if completed:
            if not quick:
                time.sleep(2)
            running = False




# LEVEL 2
def start2(earthX, earthY):
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
    global asteroids
    asteroids = []
    asteroids.append([680, 200, 40, 250])
    asteroids.append([200, 0, 40, 250])
    planets = []
    thirdLevel()
    player = [20, (screenY - 150) / 2 - 25, 0, 0]
    addPlanet("Planet1.png", 70)
    addPlanet("Planet2.png", 40)
    addPlanet("Planet3.png", 50)
    addPlanet("Planet4.png", 60)
    addPlanet("Earth.png", 50)
    print(planets)
    planets = importPlanets(planets)
    planets[len(planets) - 1][2] = earthX
    planets[len(planets) - 1][3] = earthY
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

completed = False
while not completed and not finished:
    running = True
    starting = True
    explained = False
    while running:
        if starting:
            start2(1000, 390)

        if not collided:
            prevTime = currentTime
            currentTime = time.time()
            gap = currentTime - prevTime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    completed = True
                    quick = True
                    finished = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        completed = True
                        quick = True
                        finished = True

                    if event.key == pygame.K_s:
                        player[3] = 5
                    if event.key == pygame.K_w:
                        player[3] = -5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player[3] = 0
                    if event.key == pygame.K_SPACE:
                        if explained and not fired:
                            fired = True
                            babyCoords = []
                            for coord in player:
                                babyCoords.append(coord)
                            babyCoords[0] += 75
                            babyCoords[1] += 25
                            babyCoords[2] = 5
                        if not explained:
                            explained = True
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
                                                  planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                1]:
                                grabbedPlanet = planetIndex
                                grabbingPlanet = True;

                if event.type == pygame.MOUSEBUTTONUP:
                    mousePressed = False

            move = player[1] + player[3] * speed * gap
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
                if planet[0] == "Earth.png":
                    completed = True
                    quick = False
                collided = True

        for asteroid in asteroids:
            if detectAsteroidCollision(babyCoords, asteroid):
                quick = False
                collided = True

        if not collided:
            if fired:
                move = moveBaby(babyCoords, planets, gap, speed)
                if (move[1] < 430 and move[1] > 0):
                    babyCoords = move
                else:
                    babyCoords = move
                    collided = True
                print(babyCoords)
                if babyCoords[0] >= 1200:
                    collided = True
                    quick = False
        else:
            time.sleep(2)
            running = False
        drawBaby(babyCoords[0], babyCoords[1])
        lastCursorLoc = pygame.mouse.get_pos()
        for asteroid in asteroids:
            drawAsteroid(asteroid)
        if not explained:
            drawExplainScreen()
            drawExplanation2()

        pygame.display.update()
        if completed:
            if not quick:
                time.sleep(2)
            running = False

