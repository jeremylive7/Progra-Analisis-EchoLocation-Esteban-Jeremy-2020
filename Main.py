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

#Sonar
sonar = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

#Rayo
surface3 = pygame.Surface((0, 0), pygame.SRCALPHA)
surface3.fill(BLACK)
rect3 = surface3.get_rect()

# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

# ------------------------------
# Funcion principal del juego
# ------------------------------

def main():
    pygame.init()
    pygame.display.set_caption("EcoDireccion")
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    #esenario
    pygame.draw.line(surface, WHITE, (5, 5), (5, 875))
    pygame.draw.line(surface, WHITE, (5, 5), (1035, 5))
    pygame.draw.line(surface, WHITE, (5, 875), (1035, 875))
    pygame.draw.line(surface, WHITE, (1035, 5), (1035, 875))

    #rayos
    pixAr = pygame.PixelArray(surface)

    #Sonar
    pixAr[sonar[0]][sonar[1]] = WHITE
    
    #Rayos
    #...

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            posx, posy = pygame.mouse.get_pos()
            rect3.center = (posx, posy)
            pygame.draw.circle(surface, WHITE, rect3.center, 1)

            #Colision con sonar
            dist = math.hypot(posx - sonar[0],  posy - sonar[1])
            if dist < (1 + 1):
                print('Llego al sonar.')

            #Colision con pared
            for y in range(5,875):
                dist2 = math.hypot(rect3.x - 5, rect3.y - y)
                if dist2 < (1 + 1):
                    print('Colision con pared.')
            
            for h in range(5, 1035):
                dist3 = math.hypot(rect3.x - h, rect3.y - 5)
                if dist3 < (1 + 1):
                    print('Colision con pared.')

            for p in range(5, 1035):
                dist4 = math.hypot(rect3.x - p, rect3.y - 875)
                if dist4 < (1 + 1):
                    print('Colision con pared.')

            for k in range(5, 875):
                dist5 = math.hypot(rect3.x - 1035, rect3.y - k)
                if dist5 < (1 + 1):
                    print('Colision con pared.')
           
            ##Update
            pygame.display.update()



if __name__ == "__main__":
    main()

           #Prueba
    #print("x:")
    #print(posx)
    #print("y:")
    #print(posy)
