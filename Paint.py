import pygame
from pygame.locals import *
import sys

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
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
image.fill(BLACK)
puntos = []

 

# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

def getScaleColorStructure():
    x = 20
    scale.reverse()

    for color in scale:
        punto = pygame.draw.circle(image, color, (x, x), 1)
        x += 5
        puntos.append(punto)

# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("EcoDireccion")

    getScaleColorStructure()

    for circulo in puntos:
        screen.blit(image, circulo)

    pygame.display.update()  
 
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
