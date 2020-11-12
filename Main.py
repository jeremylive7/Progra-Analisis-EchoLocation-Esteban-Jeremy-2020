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

def getDirecciones(xx:int,yy:int):
    direcciones = [1,2,3,4,5]
    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x += 5
            y += num
            puntos.append(punto)

def getDirecciones1(xx:int,yy:int):
    direcciones = [1,2,3,4,5]
    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x -= 5
            y -= num
            puntos.append(punto)

def getDirecciones2(xx:int,yy:int):
    direcciones = [1,2,3,4,5]
    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x -= 5
            y += num
            puntos.append(punto)


def getDirecciones4(xx: int, yy: int):
    direcciones = [1, 2, 3, 4, 5]
    x = xx
    y = yy

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        y -= 5
        puntos.append(punto)
        
    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x += num
            y -= 5
            puntos.append(punto)


def getDirecciones5(xx: int, yy: int):
    direcciones = [1, 2, 3, 4, 5]
    x = xx
    y = yy

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        y += 5
        puntos.append(punto)

    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x += num
            y += 5
            puntos.append(punto)


def getDirecciones6(xx: int, yy: int):
    direcciones = [1, 2, 3, 4, 5]
    x = xx
    y = yy

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x += 5
        puntos.append(punto)

    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x += 5
            y -= num
            puntos.append(punto)

def getDirecciones7(xx: int, yy: int):
    direcciones = [1, 2, 3, 4, 5]
    x = xx
    y = yy

    for color in scale:
        punto = pygame.draw.circle(surface, color, (x, y), 1)
        x -= 5
        puntos.append(punto)

    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x -= num
            y -= 5
            puntos.append(punto)

def getDirecciones8(xx: int, yy: int):
    direcciones = [1, 2, 3, 4, 5]

    for num in direcciones:
        x = xx
        y = yy
        for color in scale:
            punto = pygame.draw.circle(surface, color, (x, y), 1)
            x -= num
            y += 5
            puntos.append(punto)


def putSonar(x:int,y:int):
    getDirecciones(x, y)
    getDirecciones1(x, y)
    getDirecciones2(x, y)
    getDirecciones4(x, y)
    getDirecciones5(x, y)
    getDirecciones6(x, y)
    getDirecciones7(x, y)
    getDirecciones8(x, y)


def putSonarDiferrentesPosiciones():
    putSonar(400,400)
    putSonar(900,500)
    putSonar(200,100)
    putSonar(900,200)
    putSonar(sonar[0], sonar[1])


putSonarDiferrentesPosiciones()
# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

angulos = [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,
2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,
5,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7,7.2,7.4,7.6,7.8]

print(len(angulos))




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


