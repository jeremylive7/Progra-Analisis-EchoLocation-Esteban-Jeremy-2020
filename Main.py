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


#Coordenadainicial del sonar
sonar = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

#Rutas de las direcciones al rededor del sonar izq,der,up,down,derSup,derInf,izqSup,izqInf
posicion = [1,2,3,4,5,6,7,8]

#Direccion del sonar, aleatorio monte carlo #1
direccionSonar = random.randint(0,8)

#Posicion inicial del rayo
pos_rayo_x = sonar[0]
pos_rayo_y = sonar[1]

#Conjunto de puntos que forman un rayo
puntos_rayo_primario = []

#Matriz de pixeles
matriz_pixeles = pygame.PixelArray(surface)
matriz_pixeles[sonar[0]][sonar[1]] = WHITE

#Rayo primario
#Supongo que el random dio 2, direccion derecha inferior
for num in range(0, ((SCREEN_WIDTH // 2) // 5) - 16):
    rayo.x = pos_rayo_x
    rayo.y = pos_rayo_y
    punto = pygame.draw.circle(surface, WHITE, (rayo.x, rayo.y), 1)
    puntos_rayo_primario.append(punto)
    pos_rayo_x += 5
    pos_rayo_y += 5


# ------------------------------
# Clases y Funciones utilizadass
# ------------------------------

#Metodos de obtencion de rayo reflector

#Metodo de formula de reflexion difusa

#Metodo de definir cuantas llamadas recursivas son


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
            
            #Evento de mouse, se mueve circulo
            posx, posy = pygame.mouse.get_pos()
            #rayo.center = (posx, posy)
            #pygame.draw.circle(surface, WHITE, rayo.center, 1)


            #Colision con sonar
            dist = math.hypot(posx - sonar[0],  posy - sonar[1])
            if dist < (1 + 1):
                print('Llego al sonar.')

            #Colision con pared de la izquierda
            for y in range(5,875):
                dist2 = math.hypot(rayo.x - 5, rayo.y - y)
                if dist2 < (1 + 1):
                    print('Colision con pared de la izquierda')
            
            #Colision con pared de arriba
            for h in range(5, 1035):
                dist3 = math.hypot(rayo.x - h, rayo.y - 5)
                if dist3 < (1 + 1):
                    print('Colision con pared de arriba.')

            #Colision con pared de abajo
            for p in range(5, 1035):
                dist4 = math.hypot(rayo.x - p, rayo.y - 875)
                if dist4 < (1 + 1):
                    print('Colision con pared de abajo.')
                    print('rayo.x')
                    print(rayo.x)
                    print('rayo.y')
                    print(rayo.y)

            #Colision con pared de la derecha
            for k in range(5, 875):
                dist5 = math.hypot(rayo.x - 1035, rayo.y - k)
                if dist5 < (1 + 1):
                    print('Colision con pared de la derecha.')
           
            #distacia
            #mess='La distancia es de {}'.format( str(int(dist2)))

            ##Update
            pygame.display.update()



if __name__ == "__main__":
    main()


