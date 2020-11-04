import pygame
from pygame.locals import *
import sys
import time

# -----------
# Constantes
# -----------

BLACK = (0, 0, 0)
scale = [(0,0,0),
(8,8,8),
(16,16,16),
(24,24,24),
(32,32,32),
(40,40,40),
(48,48,48),
(56,56,56),
(64,64,64),
(72,72,72),
(80,80,80),
(88,88,88),
(96,96,96),
(104,104,104),
(112,112,112),
(120,120,120),
(128,128,128),
(136,136,136),
(144,144,144),
(152,152,152),
(160,160,160),
(168,168,168),
(176,176,176),
(184,184,184),
(192,192,192),
(200,200,200),
(208,208,208),
(216,216,216),
(224,224,224),
(232,232,232),
(240,240,240),
(248,248,248),
(255,255,255)]
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 880
image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
image.fill(BLACK)
puntos = []
sonar = [180,130]


 

# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

def getScaleColorStructure():
    x = sonar[0]+1
    y = sonar[1]+1
    scale.reverse()

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x += 5
        y += 5
        puntos.append(punto)

def getScaleColorStructure1():
    x = sonar[0]+1
    y = sonar[1]+1

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x += 5
        puntos.append(punto)

def getScaleColorStructure2():
    x = sonar[0]+1
    y = sonar[1]+1

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        y += 5
        puntos.append(punto)

def getScaleColorStructure3():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x -= 5
        puntos.append(punto)

def getScaleColorStructure4():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        y -= 5
        puntos.append(punto)

def getScaleColorStructure5():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x -= 5
        y -= 5
        puntos.append(punto)


def getScaleColorStructure6():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x += 5
        y -= 5
        puntos.append(punto)

def getScaleColorStructure7():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, y), 1)
        x -= 5
        y += 5
        puntos.append(punto)

getScaleColorStructure()
#getScaleColorStructure1()
#getScaleColorStructure2()
#getScaleColorStructure3()
#getScaleColorStructure4()
#getScaleColorStructure5()
#getScaleColorStructure6()
#getScaleColorStructure7()

# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #screen.fill(BLACK)
    pygame.display.set_caption("EcoDireccion")

    for circulo in puntos:
        screen.fill(BLACK)
        screen.blit(image, circulo)
        time.sleep(0.5)
     
    pygame.display.flip()
    #pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()

# ------------------------------
# Comentarios
# ------------------------------

#pygame.display.update() es lo mismo que pygame.display.flip()
#screen.fill(BLACK) es lo mismo que screen.blit(image,..)
