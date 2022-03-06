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


def addPlanet(imageName, size):
    planets.append([imageName, size])


def addWormhole(imageName, width, height, x, y, rotation, x2, y2,
                rotation2):  # x and y are top left points; rotation should be between 0 and 360
    newWormhole = [imageName, width, height, x, y, rotation]
    newWormhole2 = [imageName, width, height, x2, y2, rotation2]
    newPair = []
    newPair.append(newWormhole)
    newPair.append(newWormhole2)
    wormholePairs.append(newPair)


def teleport(wormholePair, startIndex):
    startWormhole = wormholePair[startIndex]
    otherWormhole = wormholePair[(startIndex + 1) % 2]
    startAngle = math.radians(startWormhole[5])
    otherAngle = math.radians(otherWormhole[5])
    angle = startAngle - otherAngle
    print("success")
    print(babyCoords)

    # teleporting baby accounting for the angled portal
    if (startAngle != 0):  # checking first fail state
        babyCoords[0] = otherWormhole[3] + (babyCoords[0] - startWormhole[3]) * math.sin(otherAngle) / math.sin(
            startAngle)
    else:  # portal is vertical so we can make calculations assuming that
        babyCoords[0] = otherWormhole[3] + (-startWormhole[4] + babyCoords[1]) * math.sin(
            otherAngle)  # check minus in testing
    if (startAngle != math.radians(90) and startAngle != math.radians(270)):  # checking for second fail state
        babyCoords[1] = otherWormhole[4] + (babyCoords[1] - startWormhole[4]) * math.cos(otherAngle) / math.cos(
            startAngle)
    else:  # yet again we can use the problem to our advantage by taking
        babyCoords[1] = otherWormhole[4] + (startWormhole[3] - babyCoords[0]) * math.sin(otherAnge)

    # A = math.radians(180) - math.atan(oldYvelocity/oldXvelocity) - startAngle
    # currentSpeed = math.sqrt(oldXvelocity**2 + oldYvelocity**2)
    # babyCoords[2] = -currentSpeed * math.sin(A+otherWormhole[5])
    # babyCoords[3] = -currentSpeed * math.cos(A + otherWormhole[5])
    # babyCoords[2] = oldDX*math.cos(math.radians(otherWormhole[5]))/math.cos(math.radians(startWormhole[5])) + oldDY*math.sin(math.radians(otherWormhole[5]))/math.sin(math.radians(startWormhole[5]))
    # babyCoords[3] = oldDY*math.sin(math.radians(otherWormhole[5]))/math.sin(math.radians(startWormhole[5])) + oldDX*math.cos(math.radians(otherWormhole[5]))/math.cos(math.radians(startWormhole[5]))

    oldXvelocity = babyCoords[2]
    oldYvelocity = babyCoords[3]

    # setting the velocity
    babyCoords[2] = oldXvelocity * math.cos(angle) - oldYvelocity * math.sin(angle)
    babyCoords[3] = oldXvelocity * math.sin(angle) + oldYvelocity * math.cos(angle)


def drawWormholes():
    for pair in wormholePairs:
        wormholeImg = pygame.image.load(pair[0][0])
        wormholeImg = pygame.transform.scale(wormholeImg, (pair[0][1], pair[0][2]))
        wormholeImg = pygame.transform.rotate(wormholeImg, pair[0][5])
        screen.blit(wormholeImg, (pair[0][3], pair[0][4]))
        wormholeImg = pygame.image.load(pair[1][0])
        wormholeImg = pygame.transform.scale(wormholeImg, (pair[1][1], pair[1][2]))
        wormholeImg = pygame.transform.rotate(wormholeImg, pair[1][5])
        screen.blit(wormholeImg, (pair[1][3], pair[1][4]))


def importPlanets(planetArray):  # planetArray must be a 2d array of planets
    planetLocations = []
    loc = [screenX - 20, screenY - 75]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0] - planet[1], loc[1]])
        loc[0] = loc[0] - 50 - 2 * planet[1]
        print(loc)
    return planetLocations


def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1] * 2, planet[1] * 2))
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


def getPlanetDistance(planet1, planet2):
    return math.sqrt((planet1[2] - planet2[2]) ** 2 + (planet1[3] - planet2[3]) ** 2)


def detectCollision(baby, planet):
    distance = getDistance(baby, planet)
    if distance < planet[1] + 15:
        return True
    else:
        return False


def mainMenu():
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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
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
                player[3] -= (player[1] - planet[3]) * planet[1] / ((getDistance(player, planet) ** 2) * 5)
                player[2] -= (player[0] - planet[2]) * planet[1] / ((getDistance(player, planet) ** 2) * 5)
    player[1] += player[3] * gap * speed
    return player


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
    global wormholePairs
    global teleportTime
    global hasTeleported
    planets = []
    wormholePairs = []
    firstLevel()
    player = [20, (screenY - 150) / 2 - 25, 0, 0]
    addPlanet("Planet1.png", 70)
    addPlanet("Planet2.png", 40)
    addPlanet("Planet3.png", 50)
    addPlanet("Planet4.png", 60)
    addWormhole("wormhole.png", 10, 500, 200, 300, 80, 200, 50, 20)
    print(planets)
    planets = importPlanets(planets)
    print(planets)
    prevTime = 0
    currentTime = time.time()
    speed = 40
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

    hasTeleported = False
    running = True
    starting = True
    while running:

        teleportCount = 0
        teleportTime = time.time_ns()-1000000000
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
                            if ((getPlanetDistance(planets[planetIndex], planets[grabbedPlanet])) <
                                planets[planetIndex][
                                    1] + planets[grabbedPlanet][1]) and planetIndex != grabbedPlanet:
                                overlap = True
                        if not overlap:
                            grabbingPlanet = False
                    elif not fired:
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
                collided = True

        if not collided:
            if fired:
                babyCoords = moveBaby(babyCoords, planets, gap, speed)
                print(babyCoords)
                if babyCoords[0] >= 1200:
                    completed = True
                    quick = False
        else:
            time.sleep(2)
            running = False
        drawWormholes()
        drawBaby(babyCoords[0], babyCoords[1])

        if (fired):

            finalPairIndex = 0
            finalWormholeIndex = 0
            for pairIndex in range(len(wormholePairs)):
                inRange = False
                for wormholeIndex in range(len(wormholePairs[pairIndex])):
                    #newAngle = math.atan(babyCoords[0]/babyCoords[1])
                    #canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                    #if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                    #if (not hasTeleported):
                    #if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
                        babyX = babyCoords[0]
                        babyY = babyCoords[1]
                        topLeftX = wormholePairs[pairIndex][wormholeIndex][3]
                        topLeftY = wormholePairs[pairIndex][wormholeIndex][4]
                        angle = math.radians(wormholePairs[pairIndex][wormholeIndex][5])
                        across = babyX - topLeftX
                        down = babyY - topLeftY
                        height = math.cos(angle) * wormholePairs[pairIndex][wormholeIndex][2]
                        width = math.sin(angle) * wormholePairs[pairIndex][wormholeIndex][2]
                        if width == 0:
                            width = 1
                        if across == 0:
                            across = 1
                        if height == 0:
                            height = 1
                        if down == 0:
                            down = 1
                        print (wormholePairs[pairIndex][wormholeIndex])
                        print(across)
                        print(down)
                        print(height)
                        print(width)
                        # ellipseX = wormholePairs[pairIndex][wormholeIndex][3] + width/2
                        # ellipseY = wormholePairs[pairIndex][wormholeIndex][4] + height/2
                        # if ((((babyX-ellipseX/2)*math.cos(angle)+(babyY-ellipseY/2)*math.sin(angle))**2)/(width**2)+(((babyX-ellipseX/2)*math.sin(angle)-(babyY-ellipseY/2)*math.cos(angle))**2)/(height**2)) < 1:
                        # slope = math.cos(angle)/math.sin(angle)
                        # if (slope*(babyX-topLeftX)+topLeftY + 20*math.sin(angle) > babyY) \
                        # and (slope*(babyX-topLeftX)+topLeftY - 20*math.sin(angle) < babyY) \
                        # and (topLeftY<babyY+15) \
                        # and (topLeftY + height) > babyCoords[1]+15:
                        print((across / width) / (down / height))
                        print(topLeftY)
                        print(babyY)
                        print(topLeftY+height)
                        print((((across / width) / (down / height) > 0.8 and (across / width) / (down / height) < 1.2) \
                            and (topLeftY < babyY + 30) \
                            and (topLeftY + height) > babyY - 30))
                        if ((((across / width) / (down / height) > 0.8 and (across / width) / (down / height) < 1.2) \
                            and (topLeftY < babyY + 30) \
                             and (topLeftX - 10 < babyX) \
                             and (topLeftX + width + 10 > babyX) \
                             and (topLeftY + height) > babyY - 30) \
                                or ((angle == 0) \
                                    and (topLeftX -10 < babyX) \
                                    and (topLeftX + width +10 > babyX))):
                            if ((not hasTeleported)):
                                teleport(wormholePairs[pairIndex], wormholeIndex)
                                hasTeleported = True
                                print(time.time_ns() - teleportTime)
                                teleportTime = time.time_ns()
                                teleportedLastWormhole = True
                                print("key")
                            inRange = True
                print(inRange)
                print("range")
                if not inRange:
                    hasTeleported = False

        #if (time.time() - teleportTime > 10):
            #hasTeleported = False

        lastCursorLoc = pygame.mouse.get_pos()
        pygame.display.update()
        if completed:
            if not quick:
                time.sleep(2)
            running = False