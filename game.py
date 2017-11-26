'''in case that nested pygame with tkinter would sometimes create the error that terminating with uncaught exception of type NSException. '''

'''I split the tkinter part from the pygame part, but you could find the tkinter part in the background file'''
import Reference
import ImageWriter
import sys,time
import pygame
import random, copy, math
from boat import Boat
from Player import Player
from Utils import Utils
from gameSprit import GameSprite

class Struct(object): pass
BLACK = (0, 0, 0)

def init(data):
    data.speed=24
    pglst = ["pg1.jpg",
             "pg2.jpg",
             "pg3.jpg",
             "pg4.jpg",
             "pg5.jpg", "pg6.jpg"]
    data.newpglst = []  # the surfaces list
    for i in pglst:
        b = pygame.image.load(i).convert()
        data.newpglst.append(b)
    data.timelst = [0]
    timelap = 0
    for j in data.newpglst:
        width = ImageWriter.getWidth(j)
        timelap += 1.0 * width / data.speed
        data.timelst.append(timelap)

    # game objects
    data.boatSprites1 = pygame.sprite.Group()
    data.boatSprites2 = pygame.sprite.Group()
    data.boatSprites3 = pygame.sprite.Group()
    data.boatSprites4 = pygame.sprite.Group()
    data.boatSprites5 = pygame.sprite.Group()

    data.playerSprite = pygame.sprite.GroupSingle()

    boat1lst = [("pg1-1.png"), ("pg1-2.png"), ("pg1-3.png"), ("pg1-4.png"), ("pg1-5.png"), ("pg1-6.png"),
                ("pg1-7.png"), ("pg1-8.png")]
    boat2lst = [("pg2-1.png"), ("pg2-2.png"), ("pg2-3.png"), ("pg2-4.png")]
    boat3lst = [("pg3-1.png"), ("pg3-2.png"), ("pg3-3.png"), ("pg3-4.png"), ("pg3-5.png")]
    boat4lst = [("pg4-1.png"), ("pg4-2.png"), ("pg4-3.png"), ("pg4-4.png")]
    boat5lst = [("pg5-1.png"), ("pg5-2.png"), ("pg5-3.png")]

    #set object and initial location
    time_passed = time.time() - start
    #boat11 = Boat(data, 1009, 596, boat1lst[0], 1)
    boat12 = Boat(data, 1600, 453, boat1lst[1], time_passed, 1)
    boat13 = Boat(data, 1545, 418, boat1lst[2], time_passed,1)
    boat14 = Boat(data, 2132, 445, boat1lst[3], time_passed,1)
    boat15 = Boat(data, 2581, 461, boat1lst[4], time_passed,1)
    boat16 = Boat(data, 2675, 466, boat1lst[5], time_passed,1)
    boat17 = Boat(data, 2793, 558, boat1lst[6], time_passed,1)
    boat18 = Boat(data, 2869, 434, boat1lst[7], time_passed,1)

    boat21 = Boat(data, 180, 620, boat2lst[0], time_passed,2)
    boat22 = Boat(data, 302, 560, boat2lst[1], time_passed,2)
    boat23 = Boat(data, 580, 598, boat2lst[2], time_passed,2)
    boat24 = Boat(data, 1224, 580, boat2lst[3], time_passed,2)

    boat31 = Boat(data, 987, 637, boat3lst[0],time_passed, 3)
    boat32 = Boat(data, 1691, 400, boat3lst[1],time_passed, 3)
    boat33 = Boat(data, 1736, 397, boat3lst[2],time_passed, 3)
    boat34 = Boat(data, 2865, 606, boat3lst[3],time_passed, 3)
    boat35 = Boat(data, 2900, 588, boat3lst[4],time_passed, 3)

    boat41 = Boat(data, 755, 600, boat4lst[0],time_passed, 4)
    boat42 = Boat(data, 2335, 419, boat4lst[1],time_passed, 4)
    boat43 = Boat(data, 2370, 407, boat4lst[2],time_passed, 4)
    boat44 = Boat(data, 2419, 370, boat4lst[3],time_passed,4)


    boat51 = Boat(data, 1060, 526, boat5lst[0], time_passed,5)
    boat52 = Boat(data, 1440, 419, boat5lst[1], time_passed,5)
    boat53 = Boat(data, 1562, 384, boat5lst[2], time_passed,5)

    data.mouseHeld=False

    # game objects
    data.boatSprites1 = pygame.sprite.Group()
    data.boatSprites2 = pygame.sprite.Group()
    data.boatSprites3 = pygame.sprite.Group()
    data.boatSprites4 = pygame.sprite.Group()
    data.boatSprites5 = pygame.sprite.Group()
    data.playerSprite = pygame.sprite.GroupSingle()

    data.boatSprites1.add(boat12, boat13, boat14, boat15, boat16, boat17, boat18)
    data.boatSprites2.add(boat21, boat22, boat23, boat24)
    data.boatSprites3.add(boat31, boat32, boat33, boat34,boat35)
    data.boatSprites4.add(boat41, boat42, boat43, boat44)
    data.boatSprites5.add(boat51, boat52, boat53)

    #default player
    defaultplayer=Player(data, 1009, 596, boat1lst[0], time_passed, 1)
    data.player=defaultplayer
    data.playerSprite.add(data.player)


    data.gameSpriteGroups = [data.boatSprites1,
                         data.boatSprites2,
                         data.boatSprites3,
                         data.boatSprites4,
                         data.boatSprites5,
                         data.playerSprite]

def checkboundary(data):
    for group in data.gameSpriteGroups:
        for sprit in group:
           if Reference.isColliding(sprit.x, sprit.y,sprit)==True:
                if sprit.operationofsprit==True:
                    #in this situation, boat would stop, which need player change mousepos and adapt to new direction
                     sprit.v = 0
                elif sprit.operationofsprit==False:
                    #boat which in random move would adapt by itself
                     sprit.turn()



def findgroup(sprite,data):
    #helps in changemode
    #to include the new sprites in courterpart groups(make checkboudary goes well for every one)
        if sprite.school==1:
            data.boatSprite1.add(sprite)
        elif sprite.school==2:
            data.boatSprite2.add(sprite)
        elif sprite.school==3:
            data.boatSprite3.add(sprite)
        elif sprite.school==4:
            data.boatSprite4.add(sprite)
        elif sprite.school==5:
            data.boatSprite5.add(sprite)



def changemode(sprite,data):
    #two situations
    #clear the initial one(boat/player) and create the new one(player/boat) with same basic traits
    if sprite.operationofsprit==True:
        x0=sprite.rect.x
        y0=sprite.rect.x
        school=sprite.school
        img=sprite.image
        sprite.kill()
        newsprite=Player(data, x0, y0,img, school)
        findgroup(newsprite,data)
        newsprite.draw(data)
        data.player=newsprite

    elif sprite.operationofsprit==False:
        x0 = sprite.rect.x
        y0 = sprite.rect.x
        school = sprite.school
        img = sprite.image
        sprite.kill()
        newsprite = Boat(data, x0, y0, img, school)
        findgroup(newsprite,data)
        newsprite.draw(data)
        data.player = None

def updateSpritesScreenPos(data):
    for group in data.gameSpriteGroups:
        for sprit in group:
            sprit.updateScreenCoords()

start = time.time()
def run():
    data=Struct()
    pygame.init()
    surf = pygame.display.set_mode((1440, 663))
    pygame.display.set_caption('A Panorama of Rivers and Mountains')
    surf.fill(BLACK)

    def move(i, time_passed, data):
        time = time_passed - data.timelst[i]
        width = ImageWriter.getWidth(data.newpglst[i])
        if (time >= 0) and (time * data.speed <= 1440 + width):
            data.distance = 1440 - time * data.speed
            surf.blit(data.newpglst[i], (1440 - time * data.speed, 0))

    def done(time_passed,data):
        move(0, time_passed,data)
        move(1, time_passed,data)
        move(2, time_passed,data)
        move(3, time_passed,data)
        move(4, time_passed,data)
        move(5, time_passed,data)

    def draw(data,surf):
        for group in data.gameSpriteGroups:
            for boat in group:
                boat.drawself(surf)


    while True:
        init(data)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                data.speed = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                data.speed = 12
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for group in data.gameSpriteGroups:
                    for s in group:
                        if s.rect.collidepoint(pos):
                            activated_sprite=s
                            activated_sprite.operationofsprit = True
                            if activated_sprite != data.player:
                                changemode(activated_sprite,data)
                            if activated_sprite ==data.player:
                                activated_sprite.operationofsprit = False
                                changemode(activated_sprite,data)
                    if event.button == 1:
                        data.mouseHeld = True
                        data.player.doMove(data)
            elif event.type == pygame.MOUSEBUTTONUP:
                data.mouseHeld = False

        time_passed = time.time() - start
        done(time_passed,data)
        updateSpritesScreenPos(data)
        draw(data,surf)
        checkboundary(data)
        pygame.display.flip()
        pygame.display.update()
run()

