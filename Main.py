import pygame
from pygame.locals import *
import sys
import math

# -----------
# Constantes
# -----------

GREEN = (0,255,0)
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
sonar = [330, 130]
puntos = []

surface2 = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
surface2.fill(BLACK)
rect2 = surface2.get_rect()
rect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

surface3 = pygame.Surface((0, 0), pygame.SRCALPHA)
surface3.fill(BLACK)
rect3 = surface3.get_rect()
rect3.center = (200,200)

surface4 = pygame.Surface((0, 0), pygame.SRCALPHA)
surface4.fill(BLACK)
rect4 = surface4.get_rect()
rect4.center = (300, 300)



# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

def getScaleColorStructure():
    x = sonar[0]
    y = sonar[1]
    scale.reverse()

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x += 5
        y += 5
        puntos.append(punto)

def getScaleColorStructure1():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x += 5
        puntos.append(punto)

def getScaleColorStructure2():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        y += 5
        puntos.append(punto)

def getScaleColorStructure3():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x -= 5
        puntos.append(punto)

def getScaleColorStructure4():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        y -= 5
        puntos.append(punto)

def getScaleColorStructure5():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x -= 5
        y -= 5
        puntos.append(punto)


def getScaleColorStructure6():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x += 5
        y -= 5
        puntos.append(punto)

def getScaleColorStructure7():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x -= 5
        y += 5
        puntos.append(punto)

def getScaleColorStructure8():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x -= 2.5
        y += 3.5
        puntos.append(punto)


def getScaleColorStructure9():
    x = sonar[0]
    y = sonar[1]

    for color in scale:
        punto = pygame.draw.circle(surface2, color, (x, y), 1)
        x -= 5
        y += 5
        puntos.append(punto)

#getScaleColorStructure()
#getScaleColorStructure1()
#getScaleColorStructure2()
#getScaleColorStructure3()
#getScaleColorStructure4()
#getScaleColorStructure5()
#getScaleColorStructure6()
#getScaleColorStructure7()
#getScaleColorStructure8()
#getScaleColorStructure9()


# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("EcoDireccion")
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    #for circulo in puntos:
    #    surface.fill(BLACK)
    #    surface.blit(surface2, circulo)
      
    pixAr = pygame.PixelArray(surface)
    pixAr[10][20]=GREEN
    pixAr[10][40] = GREEN

    circu1 = [10,20]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #surface.fill(BLACK)
            #surface.blit(surface2, rect2)
            #surface.blit(surface3, rect3)
            #surface.blit(surface4, rect4)
        
            rect3.center = pygame.mouse.get_pos()
            pygame.draw.circle(surface2, WHITE, rect3.center, 5)
            pygame.draw.circle(surface2, WHITE, rect4.center, 5)
            pygame.draw.line(surface2, WHITE, (400,400), (400,150))
            
            dist = math.hypot(rect3.x - rect4.x, rect3.y - rect4.y)
            if dist < (5 + 5):
                print('Colisiono.')

            for y in range(150,400):
                dist2 = math.hypot(rect3.x - 400, rect3.y - y)
                if dist2 < (5 + 5):
                    print('Colisiono2.')

            posx, posy = pygame.mouse.get_pos()
            pygame.draw.circle(surface, WHITE, (posx,posy), 5)

            dist3 = math.hypot(posx - circu1[0],  posy - circu1[1])
            if dist3 < (5 + 5):
                print('Colisiono3.')

            pygame.display.update()



if __name__ == "__main__":
    main()

# ------------------------------
# Comentarios
# ------------------------------

#if event.type == pygame.MOUSEBUTTONDOWN:
#if event.type == pygame.MOUSEBUTTONUP:
#    pass

#pygame.display.update() es lo mismo que pygame.display.flip()
#screen.fill(BLACK) es lo mismo que screen.blit(surface2,..)
