import pygame
from pygame.locals import *
import sys
import math
import random

# -----------
# Constantes
# -----------

#Colores disponibles
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

#Colores de blanco a negro
scale.reverse()

#Dimensiones de la pantalla
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 880

#Pantalla
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Superficie de la figura circulo que irá haciendo camino, siendo el rayo
surface3 = pygame.Surface((0, 0), pygame.SRCALPHA)
rayo = surface3.get_rect()

#esenario
pygame.draw.line(surface, WHITE, (5, 5), (5, 875))
pygame.draw.line(surface, WHITE, (5, 5), (1035, 5))
pygame.draw.line(surface, WHITE, (5, 875), (1035, 875))
pygame.draw.line(surface, WHITE, (1035, 5), (1035, 875))

#Coordenada inicial del sonar
sonar = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
pos_rayo_x = sonar[0]
pos_rayo_y = sonar[1]

#Matriz de pixeles
matriz_pixeles = pygame.PixelArray(surface)
matriz_pixeles[sonar[0]][sonar[1]] = WHITE


#Rutas de las direcciones al rededor del sonar izq,der,up,down,derSup,derInf,izqSup,izqInf
posicion = [1,2,3,4,5,6,7,8]

#Direccion del sonar, aleatorio monte carlo #1
direccionSonar = random.randint(0,8)

#Conjunto de puntos que forman un rayo
puntos_rayo_primario = []

#
puntos = []

def getScaleColorStructure():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y += 5
        puntos.append(punto)

def getScaleColorStructure01():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y += 4
        puntos.append(punto)

def getScaleColorStructure02():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y += 3
        puntos.append(punto)


def getScaleColorStructure03():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y += 2
        puntos.append(punto)


def getScaleColorStructure04():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y += 0
        puntos.append(punto)

def getScaleColorStructure1():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        puntos.append(punto)


def getScaleColorStructure2():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        y += 5
        puntos.append(punto)


def getScaleColorStructure3():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x -= 5
        puntos.append(punto)


def getScaleColorStructure4():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        y -= 5
        puntos.append(punto)


def getScaleColorStructure5():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x -= 5
        y -= 5
        puntos.append(punto)


def getScaleColorStructure6():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        y -= 5
        puntos.append(punto)


def getScaleColorStructure7():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x -= 5
        y += 5
        puntos.append(punto)


def getScaleColorStructure8():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x -= 5
        y += 3.5
        puntos.append(punto)




getScaleColorStructure()
getScaleColorStructure1()
getScaleColorStructure2()
getScaleColorStructure3()
getScaleColorStructure4()
getScaleColorStructure5()
getScaleColorStructure6()
getScaleColorStructure7()
getScaleColorStructure8()
getScaleColorStructure01()
getScaleColorStructure02()
getScaleColorStructure03()
getScaleColorStructure04()

# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    #Inicializo la sincronia con el juego
    pygame.init()
    pygame.display.set_caption("EcoDireccion")
    
    #Ciclo de recursion
    while True:

        #Eventos del juego, teclado no se usa, solo el mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Update
            pygame.display.update()


if __name__ == "__main__":
    main()


