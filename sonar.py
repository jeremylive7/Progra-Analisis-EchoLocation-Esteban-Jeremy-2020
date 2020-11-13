import numpy as np 
import pygame
import random
from PIL import Image
from Point import *
import math
import threading
from math import atan,sin,cos,asin,acos,pi
def ccw(A, B, C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
def getAngulo(p1:Point,p2:Point):
    if p1.x==p2.x:
        if p1.y<p2.y:
            return pi/2
        elif p1.y>p2.y:
            return -pi/2
        else:
            return None
    elif p1.y==p2.y:
        return 0
    else:
        return atan((p2.y-p1.y)/(p2.x-p1.x))
class Resultado:
    def __init__(self,rayo):
        self.posicion=4
class Rayo:
    def __init__(self,direccion,origen,distancia=0,energia=255):
        self.direccion=direccion
        self.origen=origen
        self.energia=energia
        self.distanciaRecorrida=distancia
    def getVectorDireccion(self):
        return Point(sin(direccion),cos(direccion))
    def parseResultado(self):
        return Resultado(self)
class Sonar:
    def __init__(self,posicion:Point,low:float,high:float):
        self.pos=posicion
        while abs(high-low)>pi:
            low+=(1-2*(high<low))*2*pi
        if high<low:
            x=high
            high=low
            low=x
        self.low=low
        self.high=high
    def ejecutar(self):
         for _ in range(50):
            direccion=random.uniform(self.low,self.high)
            finalLinea=(self.pos.x+300*cos(direccion),self.pos.y+300*sin(direccion))
            conjunto_rayos.append(
            	([Point(self.pos.x, self.pos.y), Point(finalLinea[0], finalLinea[1])]))
            #pygame.draw.line(screen, grisamarillento, (self.pos.x,self.pos.y), finalLinea, 1)
            #resultados=enviarSonido(direccion)
            #for resultado in resultados:
                #px[resultado.posicion.x][resultado.posicion.y]=(resultado.intensidad,resultado.intensidad,resultado.intensidad)
    def anguloPrincipal(self,angulo):
        while angulo<-pi or angulo>pi:
            angulo+=2*pi*(1-2*(angulo>pi))
        return angulo
    def obtenerAnguloDeReflexion(self,s,r):
        return pi-(r-s)+s
    def compararAngulos(self,cita,cita0):
        return pow(cos(cita-cita0),2)
    
    def obtenerDireccion(self,anguloDeReflejo,energia,segmento):
        b=useMonteCarloInAngle()
        energia-=K*compararAngulos(b,anguloDeReflejo)
        return b,energia
    def enviarSonido(self,direccion,origen=None,energia=1,cantRecursividades=0,resultados=[]):
        if origen==None:
            origen=self.pos
        if cantRecursividades>=2:
            return resultados
        puntoQueChoca,segmentoConQueChoca=buscarPuntoDeImpacto(direccion,origen)#Considerando la oreja del sonar
        
        if self.loEscucha(puntoQueChoca): pass

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
grisamarillento=(149, 150, 80)
conjunto_rayos = []

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

# posición de los angulos
angulos_direcciones = [0, pi*5/6, pi*3/4, pi*2/3, pi/2, pi/3, pi/4, pi/6, pi, -pi/6, -pi/4, -pi/3, -pi/2, -pi*2/3, -pi*3/4, -pi*5/6]
largo_angulos_posibles = len(angulos_direcciones)-1
sonar_inicial_random = random.randint(0, largo_angulos_posibles)
sonar_inicial = angulos_direcciones[sonar_inicial_random]
angulo_limite_izquierda = sonar_inicial_random-1
angulo_limite_derecha = sonar_inicial_random+1
if angulo_limite_derecha > largo_angulos_posibles:
    angulo_limite_derecha = 0
if angulo_limite_izquierda < 0:
    angulo_limite_izquierda = largo_angulos_posibles

# Primera recursibidad
sonar = Sonar(Point(200, 370), angulo_limite_izquierda, angulo_limite_derecha)

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
    pygame.draw.line(screen, blue, (i[0].x,i[0].y), (i[1].x,i[1].y), 2)

#thread setup
t = threading.Thread(target = sonar.ejecutar)
t.setDaemon(True) 
t.start()

#for i in conjunto_rayos:
#    pygame.draw.line(screen, grisamarillento, (i[0].x, i[0].y), (i[1].x, i[1].y), 2)

conjunto_aleatorio = []
total_rayos_aleatorios = random.randint(10, 20)
for num in range(0,total_rayos_aleatorios):
    rayo_aleatorio = random.randint(0,len(conjunto_rayos)-1)
    rayo = conjunto_rayos.pop(rayo_aleatorio)
    conjunto_aleatorio.append(rayo)
for i in conjunto_aleatorio:
    pygame.draw.line(screen, grisamarillento, (i[0].x, i[0].y), (i[1].x, i[1].y), 1)
print("Total de rayos %s" % len(conjunto_aleatorio))

grupo_choque = []
for imp1 in conjunto_aleatorio:
    for imp2 in segments:
        if intersect(imp1[0],imp1[1],imp2[0],imp2[1]):
            grupo_choque.append(
            	([Point(imp1[0].x, imp1[0].y), Point(imp1[1].x, imp1[1].y), Point(imp2[0].x, imp2[0].y), Point(imp2[1].x, imp2[1].y)]))
for list in grupo_choque:
    print("Choque del rayo con la pared: RayoInicio: (%s,%s). RayoFinal: (%s,%s). ParedInicio: (%s,%s). ParedFinal: (%s,%s)" % (
    	list[0].x, list[0].y, list[1].x, list[1].y, list[2].x, list[2].y, list[3].x, list[3].y))



#main loop
done=False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        pygame.display.update()
        clock.tick(60)
pygame.quit()
quit()
