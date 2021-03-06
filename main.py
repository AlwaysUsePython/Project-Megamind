import pygame
import time
import math
from pygame import mixer
import random

endImg = pygame.image.load("End.png")
endImg = pygame.transform.scale(endImg, (1200, 600))

pygame.init()
wormholePairs = []

explosionSound = mixer.Sound("ShipExplosion.wav")
victory = mixer.Sound("VictoryChime.wav")

noDrums = mixer.music.load("ThemeNoDrums.wav")
mixer.music.play(2)
mixer.music.queue("MainTheme.wav", "main",  -1)

screenX = 1200
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

planets = []
levels = []
level = [1, "First Launch"]
levels.append(level)
level = [2, "Asteroid"]
levels.append(level)
level = [3, "Serpens"]
levels.append(level)
level = [4, "Thread the Needle"]
levels.append(level)
level = [5, "Black Hole"]
levels.append(level)
level = [6, "Roundabout"]
levels.append(level)
level = [7, "Portals"]
levels.append(level)
level = [8, "Vertical Jump"]
levels.append(level)
level = [9, "Astral Slide"]
levels.append(level)
level = [10, "Tug-o-War"]
levels.append(level)
level = [11, "Boomerang"]
levels.append(level)
level = [12, "Twist"]
levels.append(level)

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, 270)
planets = []

holeImg = pygame.image.load("BlackHole.png")
holeImg = pygame.transform.scale(holeImg, (40, 40))

def drawHole(x, y):
    screen.blit(holeImg, (x-20, y-20))

#asteroid object is [x, y, xDimension, yDimension] ALL BY TOP LEFT
astImg = pygame.image.load("Asteroids.png")

def drawAsteroid(asteroid):
    asteroidImg = pygame.transform.scale(astImg, (asteroid[2], asteroid[3]))
    screen.blit(asteroidImg, (asteroid[0], asteroid[1]))

exp1 = pygame.image.load("Explosion1.png")
exp2 = pygame.image.load("Explosion2.png")
exp3 = pygame.image.load("Explosion3.png")
exp1 = pygame.transform.scale(exp1, (50, 50))
exp2 = pygame.transform.scale(exp2, (50, 50))
exp3 = pygame.transform.scale(exp3, (50, 50))

def drawExplosion(x, y, num):
    if num == 1:
        img = exp1
    elif num == 2:
        img = exp2
    else:
        img = exp3
    screen.blit(img, (x-15, y -15))


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


backgroundImg = pygame.image.load("Background.png")
backgroundImg = pygame.transform.scale(backgroundImg, (1200, 600))

def drawBackground():
    screen.blit(backgroundImg, (0, 0))

def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))


def addPlanet(imageName, size):
    planets.append([imageName, size])


def startScreen():
    wait=True
    while wait:
        drawBackground()
        box = pygame.image.load("box.png")
        width = 1000
        height = 500
        box = pygame.transform.scale(box, (width, height))
        screen.blit(box, ((1200 - width) / 2, (600 - height) / 2))
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("Your home planet has been destroyed!",True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (600,200)
        screen.blit(text,textRect)
        text2 = font.render("One baby is your species' only shot at survival", True, (0,0,0))
        textRect2 = text2.get_rect()
        textRect2.center=(600,275)
        screen.blit(text2,textRect2)
        text3 = font.render("Get the baby to Earth", True, (0,0,0))
        textRect3 = text3.get_rect()
        textRect3.center = (600,350)
        screen.blit(text3,textRect3)
        text4 = font.render("Press Space to continue", True, (0,0,0))
        textRect4 = text4.get_rect()
        textRect4.center = (600, 425)
        screen.blit(text4,textRect4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    wait = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    wait = False
        pygame.display.update()





def importPlanets(planetArray):  # planetArray must be a 2d array of planets
    planetLocations = []
    loc = [1200-150, 525]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0] - planet[1], loc[1]])
        loc[0] -= 300
    return planetLocations


def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1] * 2, planet[1] * 2))
    screen.blit(planetImg, (planet[2] - planet[1], planet[3] - planet[1]))


def drawBigPlanet(x, y, planetNum):
    if planetNum == 1:
        bigPlanet = pygame.image.load("Planet1.png")
    if planetNum == 2:
        bigPlanet = pygame.image.load("Planet2.png")
    if planetNum == 3:
        bigPlanet = pygame.image.load("Planet3.png")
    if planetNum == 4:
        bigPlanet = pygame.image.load("Planet4.png")
    if planetNum == 5:
        bigPlanet = pygame.image.load("BlackHole.png")
    bigPlanet = pygame.transform.scale(bigPlanet, (300, 300))
    screen.blit(bigPlanet, (x - 150, y - 150))


blackRect = pygame.image.load("BlackRect.png")
blackRect = pygame.transform.scale(blackRect, (1200, 150))

def drawPlanetBarRect():
    screen.blit(blackRect, (0, 450))
    planetBarRect = pygame.image.load("box.png")
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

startImg = pygame.image.load("Opening.png")
startImg = pygame.transform.scale(startImg, (1200, 600))

def mainMenu():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text2 = font.render("Press Space to Begin", True, (255, 255, 255))
    text3 = font.render("Press Enter for Level Select", True, (255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.center = (1000, 450)
    textRect3 = text3.get_rect()
    textRect3.center = (950, 500)
    inMenu = True
    levelSelectBoolean = False
    while inMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inMenu = False
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
                    return 1
                if event.key == pygame.K_RETURN:
                    inMenu = False
                    levelSelectBoolean = True


        screen.blit(startImg, (0, 0))
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        pygame.display.update()
        if levelSelectBoolean:
            return levelSelect()


def levelSelect():
    global first
    first = True
    inLevelSelect = True
    while inLevelSelect:
        drawBackground()
        for row in range(1,4,1):
            for column in range(4):
                drawBox(24 + 24*column + 270*column,24+24*row+120*row,row*4 - 5 + column+1)

        font = pygame.font.Font("freesansbold.ttf", 50)
        text = font.render("Level Select!", True, (255, 50, 50))
        textRect = text.get_rect()
        textRect.center = ((600, 100))
        screen.blit(text, textRect)

        pygame.display.update()
        mainMenuBoolean = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inLevelSelect = False
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inLevelSelect = False
                    mainMenuBoolean = True
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for row in range(1, 4, 1):
                    for column in range(4):
                        if (pos[0] > 24 + 24*column + 270*column and pos[0] < 24 + 270 + 24*column + 270*column) \
                                    and (pos[1]>24+24*row+120*row and pos[1] < 24 + 120 + 24*row+120*row):
                            return row*4 - 5 + column + 2
                            inLevelSelect = False

        if(mainMenuBoolean):
            mainMenu()

def drawEndScreen():
    wait = True
    while wait:
        box = pygame.image.load("box.png")
        width = 660
        height = 250
        box = pygame.transform.scale(box,(width,height))
        screen.blit(box,((1200-width)/2,(600-height)/2-20))
        font = pygame.font.Font("freesansbold.ttf", 50)
        text = font.render("You saved the baby!", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = ((600, 225))
        screen.blit(text,textRect)
        font2 = pygame.font.Font("freesansbold.ttf", 32)
        text2 = font2.render("Press Space to play the next level", True, (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = ((600, 300))
        screen.blit(text2,textRect2)
        font3 = pygame.font.Font("freesansbold.ttf", 32)
        text3 = font3.render("Press Enter for level select", True, (0, 0, 0))
        textRect3 = text3.get_rect()
        textRect3.center = ((600, 350))
        screen.blit(text3,textRect3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    wait = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    wait = False
                    return -1
                if event.key == pygame.K_RETURN:
                    return levelSelect()
                    wait = False


def drawBox(x,y,levelNum):##270 x 120
    box = pygame.image.load("box.png")
    screen.blit(box,(x,y))
    font = pygame.font.Font("freesansbold.ttf", 20)
    levels[levelNum]
    content = "" + str(levels[levelNum][0]) + ": " + levels[levelNum][1]
    text = font.render(content, True, (0, 0, 0))
    textRect = text.get_rect()
    xCenter = x + 135
    yCenter = y + 60
    textRect.center=((xCenter,yCenter))
    screen.blit(text,textRect)

def moveBaby(player, planets, gap, speed):
    # player[3] = 0
    for planet in planets:
        if planet[3] < 450:
            if getDistance(player, planet) < 2500:
                if planet[0] == "BlackHole.png":
                    player[3] -= (player[1] - planet[3]) * 120 * (gap*speed) / ((getDistance(player, planet) ** 2)*8)
                    player[2] -= (player[0] - planet[2]) * 120 * (gap*speed) / ((getDistance(player, planet) ** 2)*8)
                else:
                    player[3] -= (player[1] - planet[3]) * planet[1] * (gap * speed) / ((getDistance(player, planet) ** 2) * 8)
                    player[2] -= (player[0] - planet[2]) * planet[1] * (gap * speed) / ((getDistance(player, planet) ** 2) * 8)

    player[1] += player[3] * gap * speed
    player[0] += player[2] * gap * speed
    return player


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
    babyCoords[2] = 0.8*(oldXvelocity * math.cos(angle) - oldYvelocity * math.sin(angle))
    babyCoords[3] = 0.8*(oldXvelocity * math.sin(angle) + oldYvelocity * math.cos(angle))


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


def drawExplanation1():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Get the baby to planet Earth in ONE SHOT!", True, (255, 255, 255))
    text1 = font.render("Use the spacebar to launch the baby", True, (255, 255, 255))
    text2 = font.render("W and S move the ship on the y axis", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 290)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)


def drawExplanation2():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("You need to curve your one shot around the", True, (255, 255, 255))
    text1 = font.render(" asteroids! Planets have gravitational pull.", True, (255, 255, 255))
    text2 = font.render("Use that to your advantage!", True, (255, 255, 255))
    text3 = font.render("Drag the planets onto the screen with your mouse", True, (255, 255, 255))
    text4 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 290)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 330)
    textRect4 = text4.get_rect()
    textRect4.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)


def drawExplanation3():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("This one's a bit harder!", True, (255, 255, 255))
    text1 = font.render("You may need to place a few more planets.", True, (255, 255, 255))
    text2 = font.render("Larger planets have larger", True, (255, 255, 255))
    text3 = font.render("gravitational pulls!", True, (255, 255, 255))
    text4 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 290)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 330)
    textRect4 = text4.get_rect()
    textRect4.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)


def drawExplanation4():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Now you have to make some tight turns!", True, (255, 255, 255))
    text1 = font.render("Use the circular shape of the planets'", True, (255, 255, 255))
    text2 = font.render(" orbits to navigate around the bends!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 290)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

def drawExplanation5():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Black holes have disproportionately large", True, (255, 255, 255))
    text1 = font.render("gravitational pulls", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text3, textRect3)

def drawExplanation6():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Similar challenge, but now", True, (255, 255, 255))
    text1 = font.render("with a few asteroids!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect1 = text1.get_rect()
    textRect1.center = (600, 250)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text3, textRect3)


def drawExplanation7():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Portals allow you to teleport!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text3, textRect3)

def drawExplanation8():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("The angle you go into a portal is the", True, (255, 255, 255))
    text2 = font.render("angle you emerge at on the other side!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 300)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

def drawExplanation9():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("This black hole is really close to the ship.", True, (255, 255, 255))
    text2 = font.render("Harness its power to make it across!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 300)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

def drawExplanation10():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Make sure you balance the pull of the black holes", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text3, textRect3)

def drawExplanation11():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Your escape pod will swerve out of control", True, (255, 255, 255))
    text2 = font.render("It will require a lot of mass to correct it.", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 300)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)

def drawExplanation12():
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("This level is deviously difficult.", True, (255, 255, 255))
    text2 = font.render("Pay attention to portal direction! Good luck!", True, (255, 255, 255))
    text3 = font.render("Press Space to Continue", True, (200, 200, 200))
    textRect = text.get_rect()
    textRect.center = (600, 210)
    textRect2 = text2.get_rect()
    textRect2.center = (600, 300)
    textRect3 = text3.get_rect()
    textRect3.center = (600, 390)
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)


def firstLevel():
    global finished
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 1)
        pygame.display.update()



def secondLevel():
    global finished
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 2)
        pygame.display.update()



def thirdLevel():
    global finished
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 3)
        pygame.display.update()

def fourthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 4", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 4)
        pygame.display.update()

def fifthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 5", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 5)
        pygame.display.update()


def sixthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 6", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 1)
        pygame.display.update()

def seventhLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 7", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 2)
        pygame.display.update()


def eighthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 8", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 3)
        pygame.display.update()

def ninthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 9", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 4)
        pygame.display.update()

def tenthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 10", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 4)
        pygame.display.update()

def eleventhLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 11", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 5)
        pygame.display.update()


def twelfthLevel():
    global finished
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Level 12", True, (255, 255, 255))
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
                pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    inMenu = False
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        drawBigPlanet(600, 300, 5)
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

running = True


# LEVEL 1
def start1(earthX, earthY, first):
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
    if first:
        firstLevel()
        planets = []
        player = [20, 400, 0, 0]
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

# LEVEL 2
def start2(earthX, earthY, first):
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
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        secondLevel()
        planets = []
        addPlanet("Planet1.png", 60)
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

# LEVEL 2
def start3(earthX, earthY, first):
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
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        thirdLevel()
        planets = []
        addPlanet("Planet1.png", 60)
        addPlanet("Planet2.png", 40)
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

def start4(earthX, earthY, first):
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
    asteroids.append([280, 0, 50, 160])
    asteroids.append([280, 290, 50, 160])
    asteroids.append([575, 185, 50, 60])
    asteroids.append([850, 0, 50, 160])
    asteroids.append([850, 290, 50, 160])
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        fourthLevel()
        planets = []
        addPlanet("Planet1.png", 60)
        addPlanet("Planet3.png", 50)
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

def start5(earthX, earthY, first):
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
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        fifthLevel()
        planets = []
        addPlanet("Planet4.png", 60)
        addPlanet("BlackHole.png", 20)
        addPlanet("Earth.png", 100)
        planets = importPlanets(planets)
        planets[len(planets) - 1][2] = earthX
        planets[len(planets) - 1][3] = earthY
        planets[len(planets) - 2][2] = 600
        planets[len(planets) - 2][3] = 225
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

def start6(earthX, earthY, first):
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
    asteroids.append([400, 250, 50, 200])
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        sixthLevel()
        planets = []
        addPlanet("Planet3.png", 60)
        addPlanet("Planet4.png", 50)
        addPlanet("BlackHole.png", 20)
        addPlanet("Earth.png", 75)
        planets = importPlanets(planets)
        planets[len(planets) - 1][2] = earthX
        planets[len(planets) - 1][3] = earthY
        planets[len(planets) - 2][2] = 300
        planets[len(planets)-2][3] = 225
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

def start7(earthX, earthY, first):
    global wormholePairs
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
    asteroids.append([500, 225, 50, 225])
    asteroids.append([500, 0, 50, 225])
    #imageName, width, height, x, y, rotation, x2, y2, rotation2
    wormholePairs = []
    addWormhole("Portal.png", 40, 70, 400, 20, 0, 800, 350, 0)
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        seventhLevel()
        planets = []
        addPlanet("Planet1.png", 40)
        addPlanet("Planet2.png", 50)
        addPlanet("Planet3.png", 60)
        addPlanet("Planet4.png", 50)
        addPlanet("Earth.png", 75)

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

def start8(earthX, earthY, first):
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
    global wormholePairs
    asteroids = []
    asteroids.append([500, 225, 50, 225])
    asteroids.append([500, 0, 50, 225])
    #imageName, width, height, x, y, rotation, x2, y2, rotation2
    wormholePairs = []
    addWormhole("Portal.png", 50, 90, 400, 20, 45, 1000, 350, 91)
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        eighthLevel()
        planets = []
        addPlanet("Planet1.png", 40)
        addPlanet("Planet2.png", 50)
        addPlanet("Planet3.png", 60)
        addPlanet("Planet4.png", 50)
        addPlanet("Earth.png", 50)

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

def start9(earthX, earthY, first):
    global wormholePairs
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
    asteroids.append([900, 250, 300, 200])
    asteroids.append([200, 0, 50, 200])
    # imageName, width, height, x, y, rotation, x2, y2, rotation2
    wormholePairs = []
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        ninthLevel()
        planets = []
        addPlanet("Planet1.png", 40)
        addPlanet("Planet2.png", 50)
        addPlanet("Planet3.png", 60)
        addPlanet("Planet4.png", 50)
        addPlanet("BlackHole.png", 20)
        addPlanet("Earth.png", 75)

        planets = importPlanets(planets)
        planets[len(planets)-2][2] = 370

        planets[len(planets)-2][3] = 290
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


def start10(earthX, earthY, first):
    global wormholePairs
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
    asteroids.append([300, 150, 50, 50])
    asteroids.append([350, 100, 200, 50])
    asteroids.append([500, 250 ,50,50])
    asteroids.append([300, 300, 200, 50])
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        tenthLevel()
        planets = []
        addPlanet("Planet1.png", 40)
        addPlanet("Planet2.png", 50)
        addPlanet("Planet3.png", 60)
        addPlanet("Planet4.png", 50)
        addPlanet("BlackHole.png", 20)
        addPlanet("BlackHole.png", 20)
        addPlanet("Earth.png", 80)
        planets = importPlanets(planets)
        planets[len(planets) - 3][2] = 600
        planets[len(planets) - 3][3] = 365
        planets[len(planets) - 2][2] = 700
        planets[len(planets) - 2][3] = 50
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


def start11(earthX, earthY, first):
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
    global wormholes
    global wormholePairs
    asteroids = []
    asteroids.append([300, 0, 50, 150])
    wormholePairs = []
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        eleventhLevel()
        planets = []
        addPlanet("Planet1.png", 60)
        addPlanet("Planet2.png", 60)
        addPlanet("Planet3.png", 50)
        addPlanet("Planet4.png", 40)
        addPlanet("BlackHole.png", 20)
        addPlanet("Blackhole.png", 20)
        addPlanet("Earth.png", 50)
        planets = importPlanets(planets)
        planets[len(planets) - 1][2] = earthX
        planets[len(planets) - 1][3] = earthY
        planets[len(planets) - 2][2] = 290
        planets[len(planets) - 2][3] = 315
        planets[len(planets) - 3][2] = 490
        planets[len(planets) - 3][3] = 240


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

def start12(earthX, earthY, first):
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
    global wormholes
    global wormholePairs
    asteroids = []
    asteroids.append([1000, 0, 50, 450])
    wormholePairs = []
    addWormhole("Portal.png", 40, 70, 500, 20, 45, 1100, 200, 90)
    if first:
        player = [20, (screenY - 150) / 2 - 25, 0, 0]
        twelfthLevel()
        planets = []
        addPlanet("Planet1.png", 100)
        addPlanet("Planet2.png", 75)
        addPlanet("Planet3.png", 75)
        addPlanet("Planet4.png", 75)
        addPlanet("BlackHole.png", 20)
        addPlanet("Blackhole.png", 20)
        addPlanet("Earth.png", 50)
        planets = importPlanets(planets)
        planets[len(planets) - 1][2] = earthX
        planets[len(planets) - 1][3] = earthY
        planets[len(planets) - 2][2] = 600
        planets[len(planets) - 2][3] = 225
        planets[len(planets) - 3][2] = 200
        planets[len(planets) - 3][3] = 330


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
first = True
startScreen()
levelIndex = mainMenu()
while not finished:
    #ready = input()
    if levelIndex == 1:
        while not completed and levelIndex == 1:
            explained = False
            running = True
            starting = True
            while running:
                if starting:
                    start1(1200, 110, first)
                    initial = 0
                    if first:
                        first = False

                if not collided:
                    prevTime = currentTime
                    currentTime = time.time()
                    gap = currentTime - prevTime

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            completed = True
                            finished = True
                            pygame.quit()
                            quick = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            if planet[0] != "Earth.png":
                                pygame.mixer.Sound.play(explosionSound)

                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()


                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                if not completed:
                                    pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                        drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)

                if not explained:
                    drawExplainScreen()
                    drawExplanation1()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 2:
        finished = False
        first = True
        completed = False
        while not completed and not finished and levelIndex == 2:
            explained = False
            running = True
            starting = True
            while running:
                if starting:
                    start2(1200, 225, first)
                    if first:
                        first = False

                if not collided:
                    prevTime = currentTime
                    currentTime = time.time()
                    gap = currentTime - prevTime

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            completed = True
                            finished = True
                            pygame.quit()
                            quick = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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

                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)

                if not explained:
                    drawExplainScreen()
                    drawExplanation2()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 3:
        completed = False
        first = True
        while not completed and not finished and levelIndex == 3:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start3(1200, 140, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False


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

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                        1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation3()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 4:
        completed = False
        first = True
        while not completed and not finished and levelIndex == 4:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start4(1200, 225, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                        1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation4()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 5:
        completed = False
        first = True
        while not completed and not finished and levelIndex == 5:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start5(1200, 225, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                        1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation5()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

        running = True

    if levelIndex == 6:
        finished = False
        completed = False
        first = True
        while not completed and not finished and levelIndex == 6:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start6(1000, 300, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                        1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation6()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 7:
        finished = False
        completed = False
        first = True
        while not completed and not finished and levelIndex == 7:
            teleportCount = 0
            teleportTime = time.time_ns() - 1000000000
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start7(1000, 350, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
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

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < planets[planetIndex][
                                        1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][0] != "BlackHole.png":
                                            grabbingPlanet = True

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
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                drawWormholes()
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
                                if (babyX +10> topLeftX) and (babyY +10> topLeftY) and (babyX < topLeftX+width+10) and (babyY < topLeftY+height+10):
                                    if ((not hasTeleported)):
                                        teleport(wormholePairs[pairIndex], wormholeIndex)
                                        hasTeleported = True
                                        teleportTime = time.time_ns()
                                        teleportedLastWormhole = True
                                    inRange = True
                        if not inRange:
                            hasTeleported = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation7()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 9:
        finished = False
        completed = False
        first = True
        while not completed and not finished and levelIndex == 9:
            teleportCount = 0
            teleportTime = time.time_ns() - 1000000000
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start9(1000, 100, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousePressed = True
                            if grabbingPlanet == True:
                                overlap = False
                                for planetIndex in (0, len(planets) - 1, 1):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1] and planetIndex != grabbedPlanet:
                                        overlap = True

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][
                                            0] != "BlackHole.png":
                                            grabbingPlanet = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            mousePressed = False

                    move = player[1] + player[3] * speed * gap
                    if move < 400 and move > 0:
                        player[1] = move

                drawBackground()
                drawPlanetBarRect()
                drawPlayer(player[0], player[1])
                if grabbingPlanet:
                    if grabbedPlanet < len(planets) - 2:
                        planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (
                                pygame.mouse.get_pos()[0] - lastCursorLoc[0])
                        planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (
                                pygame.mouse.get_pos()[1] - lastCursorLoc[1])
                for planet in planets:
                    drawPlanet(planet)
                    if detectCollision(babyCoords, planet):
                        if planet[0] == "Earth.png":
                            completed = True
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                drawWormholes()
                if (fired):

                    finalPairIndex = 0
                    finalWormholeIndex = 0
                    for pairIndex in range(len(wormholePairs)):
                        inRange = False
                        for wormholeIndex in range(len(wormholePairs[pairIndex])):
                            # newAngle = math.atan(babyCoords[0]/babyCoords[1])
                            # canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                            # if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                            # if (not hasTeleported):
                            # if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
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
                            if (babyX +10> topLeftX) and (babyY +10> topLeftY) and (babyX < topLeftX+width+10) and (babyY < topLeftY+height+10):
                                if ((not hasTeleported)):
                                    teleport(wormholePairs[pairIndex], wormholeIndex)
                                    hasTeleported = True
                                    teleportTime = time.time_ns()
                                    teleportedLastWormhole = True
                                inRange = True
                        if not inRange:
                            hasTeleported = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation9()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    if levelIndex == 8:
        finished = False
        completed = False
        first = True
        while not completed and not finished and levelIndex == 8:
            teleportCount = 0
            teleportTime = time.time_ns() - 1000000000
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start8(800, 100, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousePressed = True
                            if grabbingPlanet == True:
                                overlap = False
                                for planetIndex in (0, len(planets) - 1, 1):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1] and planetIndex != grabbedPlanet:
                                        overlap = True

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][
                                            0] != "BlackHole.png":
                                            grabbingPlanet = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            mousePressed = False

                    move = player[1] + player[3] * speed * gap
                    if move < 400 and move > 0:
                        player[1] = move

                drawBackground()
                drawPlanetBarRect()
                drawPlayer(player[0], player[1])
                if grabbingPlanet:
                    planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (
                            pygame.mouse.get_pos()[0] - lastCursorLoc[0])
                    planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (
                            pygame.mouse.get_pos()[1] - lastCursorLoc[1])
                for planet in planets:
                    drawPlanet(planet)
                    if detectCollision(babyCoords, planet):
                        if planet[0] == "Earth.png":
                            completed = True
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                drawWormholes()
                if (fired):

                    finalPairIndex = 0
                    finalWormholeIndex = 0
                    for pairIndex in range(len(wormholePairs)):
                        inRange = False
                        for wormholeIndex in range(len(wormholePairs[pairIndex])):
                            # newAngle = math.atan(babyCoords[0]/babyCoords[1])
                            # canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                            # if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                            # if (not hasTeleported):
                            # if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
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
                            if ((((across / width) / (down / height) > 0.8 and (across / width) / (down / height) < 1.2) \
                                 and (topLeftY < babyY + 30) \
                                 and (topLeftX - 10 < babyX) \
                                 and (topLeftX + width + 10 > babyX) \
                                 and (topLeftY + height) > babyY - 30) \
                                    or ((angle == 0) \
                                        and (topLeftX - 10 < babyX) \
                                        and (topLeftX + width + 10 > babyX))):
                                if ((not hasTeleported)):
                                    teleport(wormholePairs[pairIndex], wormholeIndex)
                                    hasTeleported = True
                                    teleportTime = time.time_ns()
                                    teleportedLastWormhole = True
                                inRange = True
                        if not inRange:
                            hasTeleported = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation8()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False


    if levelIndex == 11:
        completed = False
        first = True
        while not completed and not finished and levelIndex == 11:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start11(1000, 300, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousePressed = True
                            if grabbingPlanet == True:
                                overlap = False
                                for planetIndex in (0, len(planets) - 1, 1):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1] and planetIndex != grabbedPlanet:
                                        overlap = True

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1]:
                                        grabbedPlanet = planetIndex
                                        if planetIndex < len(planets) - 3:
                                            grabbingPlanet = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            mousePressed = False

                    move = player[1] + player[3] * speed * gap
                    if move < 400 and move > 0:
                        player[1] = move

                drawBackground()
                drawPlanetBarRect()
                drawWormholes()
                drawPlayer(player[0], player[1])

                if grabbingPlanet:
                    if grabbedPlanet < len(planets) - 3:
                        planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (
                                pygame.mouse.get_pos()[0] - lastCursorLoc[0])
                        planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (
                                pygame.mouse.get_pos()[1] - lastCursorLoc[1])
                for planet in planets:
                    drawPlanet(planet)
                    if detectCollision(babyCoords, planet):
                        if planet[0] == "Earth.png":
                            mixer.Sound.play(victory)
                            completed = True
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                        finalPairIndex = 0
                        finalWormholeIndex = 0
                        for pairIndex in range(len(wormholePairs)):
                            inRange = False
                            for wormholeIndex in range(len(wormholePairs[pairIndex])):
                                # newAngle = math.atan(babyCoords[0]/babyCoords[1])
                                # canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                                # if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                                # if (not hasTeleported):
                                # if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
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
                                if ((babyX + 15 > topLeftX) and (babyY + 15 > topLeftY) and (
                                        babyX < topLeftX + width + 15) and (babyY < topLeftY + height + 15)):
                                    if ((not hasTeleported)):
                                        teleport(wormholePairs[pairIndex], wormholeIndex)
                                        hasTeleported = True
                                    inRange = True
                            if not inRange:
                                hasTeleported = False
                    drawBaby(babyCoords[0], babyCoords[1])



                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation11()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

        running = True
        finished = False

    if levelIndex == 12:
        completed = False
        first = True
        while not completed and not finished and levelIndex == 12:
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start12(1125, 340, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousePressed = True
                            if grabbingPlanet == True:
                                overlap = False
                                for planetIndex in (0, len(planets) - 1, 1):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1] and planetIndex != grabbedPlanet:
                                        overlap = True

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1]:
                                        grabbedPlanet = planetIndex
                                        if planetIndex < len(planets) - 3:
                                            grabbingPlanet = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            mousePressed = False

                    move = player[1] + player[3] * speed * gap
                    if move < 400 and move > 0:
                        player[1] = move

                drawBackground()
                drawPlanetBarRect()
                drawWormholes()
                drawPlayer(player[0], player[1])

                if grabbingPlanet:
                    if grabbedPlanet < len(planets) -3:
                        planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (
                                    pygame.mouse.get_pos()[0] - lastCursorLoc[0])
                        planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (
                                    pygame.mouse.get_pos()[1] - lastCursorLoc[1])
                for planet in planets:
                    drawPlanet(planet)
                    if detectCollision(babyCoords, planet):
                        if planet[0] == "Earth.png":
                            completed = True
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                        finalPairIndex = 0
                        finalWormholeIndex = 0
                        for pairIndex in range(len(wormholePairs)):
                            inRange = False
                            for wormholeIndex in range(len(wormholePairs[pairIndex])):
                                # newAngle = math.atan(babyCoords[0]/babyCoords[1])
                                # canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                                # if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                                # if (not hasTeleported):
                                # if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
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
                                if ((babyX + 15 > topLeftX) and (babyY + 15 > topLeftY) and (
                                        babyX < topLeftX + width + 15) and (babyY < topLeftY + height + 15)):
                                    if ((not hasTeleported)):
                                        teleport(wormholePairs[pairIndex], wormholeIndex)
                                        hasTeleported = True
                                    inRange = True
                            if not inRange:
                                hasTeleported = False
                    drawBaby(babyCoords[0], babyCoords[1])



                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False

                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation12()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

        running = True

    if levelIndex == 10:
        finished = False
        completed = False
        first = True
        while not completed and not finished and levelIndex == 10:
            teleportCount = 0
            teleportTime = time.time_ns() - 1000000000
            running = True
            starting = True
            explained = False
            while running:
                if starting:
                    start10(1000, 360, first)
                    if first:
                        first = False

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
                            pygame.quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                completed = True
                                quick = True
                                finished = True
                                pygame.quit()

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
                            if event.key == pygame.K_RETURN:
                                levelIndex = levelSelect()
                                running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mousePressed = True
                            if grabbingPlanet == True:
                                overlap = False
                                for planetIndex in (0, len(planets) - 1, 1):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1] and planetIndex != grabbedPlanet:
                                        overlap = True

                                grabbingPlanet = False
                            else:
                                for planetIndex in range(len(planets)):
                                    if (math.sqrt((planets[planetIndex][2] - lastCursorLoc[0]) * (
                                            planets[planetIndex][2] - lastCursorLoc[0]) + (
                                                          planets[planetIndex][3] - lastCursorLoc[1]) * (
                                                          planets[planetIndex][3] - lastCursorLoc[1]))) < \
                                            planets[planetIndex][
                                                1]:
                                        grabbedPlanet = planetIndex
                                        if planets[planetIndex][0] != "Earth.png" and planets[planetIndex][
                                            0] != "BlackHole.png":
                                            grabbingPlanet = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            mousePressed = False

                    move = player[1] + player[3] * speed * gap
                    if move < 400 and move > 0:
                        player[1] = move

                drawBackground()
                drawPlanetBarRect()
                drawPlayer(player[0], player[1])
                if grabbingPlanet:
                    if grabbedPlanet < len(planets) - 3:
                        planets[grabbedPlanet][2] = planets[grabbedPlanet][2] + (
                                pygame.mouse.get_pos()[0] - lastCursorLoc[0])
                        planets[grabbedPlanet][3] = planets[grabbedPlanet][3] + (
                                pygame.mouse.get_pos()[1] - lastCursorLoc[1])
                for planet in planets:
                    drawPlanet(planet)
                    if detectCollision(babyCoords, planet):
                        if planet[0] == "Earth.png":
                            completed = True
                            pygame.mixer.Sound.play(victory)
                            quick = False
                        if not collided:
                            collided = True
                            if not completed:
                                pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                for asteroid in asteroids:
                    if detectAsteroidCollision(babyCoords, asteroid):
                        quick = False
                        if not collided:
                            collided = True
                            pygame.mixer.Sound.play(explosionSound)
                            initial = time.time()

                if not collided:
                    if fired:
                        move = moveBaby(babyCoords, planets, gap, speed)
                        if (move[1] < 430 and move[1] > 0):
                            babyCoords = move
                        else:
                            babyCoords = move
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                        if babyCoords[0] >= 1200:
                            if not collided:
                                collided = True
                                pygame.mixer.Sound.play(explosionSound)
                                initial = time.time()
                            quick = False
                    drawBaby(babyCoords[0], babyCoords[1])
                else:
                    current = time.time()
                    if current - initial < 0.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 1)
                    elif current - initial < 1:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 2)

                    elif current - initial < 1.5:
                        if completed:
                            drawBaby(babyCoords[0], babyCoords[1])
                        else:
                            drawExplosion(babyCoords[0], babyCoords[1], 3)

                    else:
                        running = False
                drawWormholes()
                if (fired):

                    finalPairIndex = 0
                    finalWormholeIndex = 0
                    for pairIndex in range(len(wormholePairs)):
                        inRange = False
                        for wormholeIndex in range(len(wormholePairs[pairIndex])):
                            # newAngle = math.atan(babyCoords[0]/babyCoords[1])
                            # canTeleport = (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle)
                            # if ((time.time_ns()-teleportTime>100000000)) and not teleportedLastWormhole:
                            # if (not hasTeleported):
                            # if (wormholePairs[pairIndex][wormholeIndex][5] + 90 > newAngle) and (wormholePairs[pairIndex][wormholeIndex][5] - 90 < newAngle):
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
                            if (babyX + 10 > topLeftX) and (babyY + 10 > topLeftY) and (
                                    babyX < topLeftX + width + 10) and (babyY < topLeftY + height + 10):
                                if ((not hasTeleported)):
                                    teleport(wormholePairs[pairIndex], wormholeIndex)
                                    hasTeleported = True
                                    teleportTime = time.time_ns()
                                    teleportedLastWormhole = True
                                inRange = True
                        if not inRange:
                            hasTeleported = False
                lastCursorLoc = pygame.mouse.get_pos()
                for asteroid in asteroids:
                    drawAsteroid(asteroid)
                if not explained:
                    drawExplainScreen()
                    drawExplanation10()

                pygame.display.update()
                if completed:
                    if not quick:
                        time.sleep(1)
                    newIndex = drawEndScreen()
                    if (newIndex == -1):
                        levelIndex = levelIndex + 1
                    else:
                        levelIndex = newIndex
                    running = False

    while levelIndex > 12:
        ending = True
        while ending:
            font = pygame.font.Font("freesansbold.ttf", 32)
            endText = font.render("Hit enter for level select", True, (0, 0, 0))
            endTextRect = endText.get_rect()
            endTextRect.center = (300, 500)
            screen.blit(endImg, (0, 0))
            screen.blit(endText, endTextRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_RETURN:
                        ending = False

        levelIndex = levelSelect()
        running = True
        completed = False
