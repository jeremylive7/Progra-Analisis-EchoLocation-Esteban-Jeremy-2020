import numpy as np 
import pygame
import random
from PIL import Image
from Point import *
import math
import threading
from math import atan,sin,cos,asin,acos,pi
def getAngulo(p1:Point,p2:Point):
    if p1.x==p2.x:
        if p1.y<p2.y:
            return pi/2
        elif p1.y>p2.y:
            return 3*pi/2
        else:
            return None
    elif p1.y==p2.y:
        if p1.x<p2.x:
            return 0
        elif p1.x>p2.x:
            return pi
    else:
        return atan((p2.y-p1.y)/(p2.x-p1.x))
class Rayo:
    def __init__(self,direccion,origen,energia=255):
        self.direccion=direccion
        self.origen=origen
        self.energia=energia
class Sonar:
    def __init__(self,posicion:Point,izq:float,der:float):
        self.pos=posicion
        self.izq=izq
        self.der=der
    def ejecutar(self):
        while True:
            direccion=random.uniform(izq,der)
            resultados=enviarSonido(direccion)
            for resultado in resultados:
                px[resultado.posicion.x][resultado.posicion.y]=(resultado.intensidad,resultado.intensidad,resultado.intensidad)
    def obtenerAnguloDeReflexion(self,s,r):
        return s+pi-(s-r)
    def obtenerDireccion(self,anguloDeReflejo,energia,segmento):
        a=atan((segmento[1].y-segmento[0].y)/(segmento[1].x-segmento[0].x))
        b=random.uniform(a,a+pi)
        energia-=b*k/anguloDeReflejo
        return b,energia
    def enviarSonido(self,direccion,origen=self.pos,energia=1,cantRecursividades=0,resultados=[]):
        if cantRecursividades>=2:
            return resultados
        puntoQueChoca,segmentoConQueChoca=buscarPorTodosLosSegmentosParaVerConCualChoca(direccion,origen)
        energia=restarEnergia(energia,origen,puntoQueChoca)
        anguloDeIncidencia=obtenerAnguloDeReflexion(segmentoConQueChoca,direccion)
        for _ in range(CANT_RAYOS_MONTECARLO):
            nuevaDireccion,nuevaEnergia=obtenerDireccion(anguloDeIncidencia,energia,segmentoConQueChoca)

            resultados+=enviarSonido(nuevaDireccion,puntoQueChoca,nuevaEnergia,cantRecursividades+1)
        return resultados

# COLORS
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

#pygame stuff
h,w=550,550
border=50
pygame.init()
screen = pygame.display.set_mode((w+(2*border), h+(2*border)))
screen.fill(black)
px=pygame.PixelArray(screen)
pygame.display.set_caption("2D Raytracing")
clock = pygame.time.Clock()

#init random
random.seed()

# posición del sonar
posicionDelSonar=Point(50,50)

#warning, point order affects intersection test!!
segments = [
            ([Point(180, 135), Point(215, 135)]), 
            ([Point(285, 135), Point(320, 135)]),
            ([Point(320, 135), Point(320, 280)]),
            ([Point(320, 320), Point(320, 355)]),
            ([Point(320, 355), Point(215, 355)]),
            ([Point(180, 390), Point(180, 286)]),
            ([Point(180, 286), Point(140, 286)]),
            ([Point(320, 320), Point(360, 320)]),
            ([Point(180, 250), Point(180, 135)]),
            ]

for i in segments:
    pygame.draw.line(screen, blue, (i[0].x,i[0].y), (i[1].x,i[1].y), 1)

#thread setup
t = threading.Thread(target = sonar) # f being the function that tells how the ball should move
t.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t.start()

#main loop
done=False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        pygame.display.update()
        clock.tick(60)
pygame.quit()