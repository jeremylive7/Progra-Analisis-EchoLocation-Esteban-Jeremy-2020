import numpy as np 
import pygame
import random
from PIL import Image
from Point import *
import rt
import math
import threading
from math import atan,sin,cos,asin,acos,pi,tan
#out = []
def getRoute(start: Point, end: Point, totalSteps: int):
    out = []
    for i in range(0, totalSteps):
        tempX = start.x+(end.x-start.x)*i/totalSteps
        tempY = start.y+(end.y-start.y)*i/totalSteps
        out.append(Point(tempX, tempY))
    return out
    
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
            finalLinea=(self.pos.x+150*cos(direccion),self.pos.y+150*sin(direccion))
            conjunto_rayos.append(([Point(self.pos.x, self.pos.y), Point(finalLinea[0], finalLinea[1]), direccion]))
            
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


def obtenerAnguloDeReflexion2(s, r):
    return pi-(r-s)+s

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

# Posición de los angulos
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

# Posicion del Sonar aleatorio
x_limite_sonar_izq = int(round((w+(2*border))/4))
x_limite_sonar_der = int(round(((w+(2*border))/(1/8)/10)))
y_limite_sonar_izq = int(round((h+(2*border))/4))
y_limite_sonar_der = int(round(((h+(2*border))/(1/8)/10)))
aleatorio_posicion_sonar_x = random.randint(x_limite_sonar_izq, x_limite_sonar_der)
aleatorio_posicion_sonar_y = random.randint(y_limite_sonar_izq, y_limite_sonar_der)

# Primera recursibidad
sonar = Sonar(Point(aleatorio_posicion_sonar_x, aleatorio_posicion_sonar_y),
              angulo_limite_izquierda, angulo_limite_derecha)

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
    pygame.draw.line(screen, blue, (i[0].x, i[0].y), (i[1].x, i[1].y), 2)

#thread setup
t = threading.Thread(target = sonar.ejecutar)
t.setDaemon(True) 
t.start()

# Rayos
conjunto_aleatorio = []
total_rayos_aleatorios = random.randint(10, 20)
for num in range(0,total_rayos_aleatorios):
    rayo_aleatorio = random.randint(0,len(conjunto_rayos)-1)
    rayo = conjunto_rayos.pop(rayo_aleatorio)
    conjunto_aleatorio.append(rayo)
#for i in conjunto_aleatorio:
 #   pygame.draw.line(screen, grisamarillento, (i[0].x, i[0].y), (i[1].x, i[1].y), 1)
print("Total de rayos %s" % len(conjunto_aleatorio))

# Intersección
grupo_choque = []
for imp1 in conjunto_aleatorio:
    cont = 0
    for imp2 in segments:
        if intersect(imp1[0],imp1[1],imp2[0],imp2[1]) and cont == 0:
            grupo_choque.append(([Point(imp1[0].x, imp1[0].y), Point(imp1[1].x, imp1[1].y), imp1[2]]))
            cont = 1

# Matriz de pixeles, Rayo reflejado
matriz_pixeles = pygame.PixelArray(screen)
choque = []
rayos_ecos = []
for hp in grupo_choque:
    hp1x = int(round(hp[1].x))
    hp1y = int(round(hp[1].y))
    #print("Inicio-> x:%s. y:%s. Final-> x:%s. y:%s." % (hp[0].x, hp[0].y, hp1x, hp1y))
    cont = 0
    rayo_eco = []
    trayectoria_rayo = getRoute(hp[0], Point(hp1x, hp1y), (300))
    for h in trayectoria_rayo:
        x = int(round(h.x))
        y = int(round(h.y))
        #print("trayectoria del rayo x:%s, y:%s" % (x, y))
        if cont == 0:
            rayo_eco.append(Point(x, y))
        if matriz_pixeles[x][y] == screen.map_rgb(blue) and cont == 0:
            choque.append(Point(x,y))
            anguloReflejoHipot = obtenerAnguloDeReflexion2(pi, hp[2])
            finalRayoHipot = (x+150*cos(anguloReflejoHipot),
                              y+150*sin(anguloReflejoHipot))
            pygame.draw.line(screen, (0, 105, 77), (x, y), finalRayoHipot, 1)
            cont = 1
            
    rayos_ecos.append(rayo_eco)

for f in range(0,len(choque)):
    print("Colision: x: %s. y: %s" % (choque[f].x,choque[f].y))
print("len(grupo_choque):%s. len(choque):%s." %
      (len(grupo_choque), len(choque)))

print("Rayos eco")
for g in range(0, len(rayos_ecos)):
    for j in range(0, len(rayos_ecos[g])):
        pygame.draw.circle(screen, (191, 255, 244),(rayos_ecos[g][j].x, rayos_ecos[g][j].y), 1)
        #print("x:%s. y:%s" % (rayos_ecos[g][j].x, rayos_ecos[g][j].y))

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
