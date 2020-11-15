import numpy as np 
import pygame
import random
from PIL import Image
from Point import *
import rt
import math
import threading
from math import atan,sin,cos,asin,acos,pi,tan,inf

def getPuntoFromAnguloAndDistancia(angulo,origen=Point(0,0),distancia=9999):
    return Point(distancia*cos(angulo)+origen.x,distancia*sin(angulo)+origen.y)
def getChoqueIfChoca(rayo,pared):
        X1=pared[0].x
        X2=pared[1].x
        Y1=pared[0].y
        Y2=pared[1].y
        X3=rayo.origen.x
        finRayo=getPuntoFromAnguloAndDistancia(rayo.direccion,rayo.origen)
        X4=finRayo.x
        Y3=rayo.origen.y
        Y4=finRayo.y
        if max(X1,X2)<min(X3,X4):
            return False
        if X1==X2: 
            A1=inf
        else:
            A1=(Y1-Y2)/(X1-X2)
        if X3==X4:
            A2=inf
        else:
            A2=(Y3-Y4)/(X3-X4)
        if A1==A2:
            return False
        b1=Y1-A1*X1
        b2=Y3-A2*X3
        Xi=(b2-b1)/(A1-A2)
        Yi=A1*Xi+b1
        if Xi<max(min(X1,X2),min(X3,X4))or Xi > min(max(X1,X2),max(X3,X4)):
            return False
        return Point(Xi,Yi)
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
        return Point(sin(self.direccion), cos(self.direccion))
    def parseResultado(self):
        return Resultado(self)
    def getString(self):
        print("Direccion:%s. Origen:%s. Energia:%s. DistanciaRecorrida:%s" % (self.direccion, self.origen, self.energia, self.distanciaRecorrida))
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
            
            #resultados=enviarSonido(direccion)
            #for resultado in resultados:
                #px[resultado.posicion.x][resultado.posicion.y]=(resultado.intensidad,resultado.intensidad,resultado.intensidad)
    def anguloPrincipal(self,angulo):
        while angulo<-pi or angulo>pi:
            angulo+=2*pi*(1-2*(angulo>pi))
        return angulo
    def obtenerAnguloDeReflexion(self,s,r):
        s+=p/2
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
    s+=pi/2
    return pi-(r-s)+s


#Global
conjunto_rayos = []
# COLORS
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
grisamarillento=(149, 150, 80)
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
scale.reverse()

#pygame stuff
h, w = 550, 550
border = 50
pygame.init()
screen = pygame.display.set_mode((w+(2*border), h+(2*border)))
screen.fill(black)
px = pygame.PixelArray(screen)
pygame.display.set_caption("2D Raytracing")
clock = pygame.time.Clock()

def pintaColisionEscalable(punto_choque, energia: int):
    #Divido las escala de grises para tener rangos de referencia para cada cantidad de energia
    print("len(scale):%s" % len(scale))
    if(energia >= 0 and energia <= 7):
        pygame.draw.circle(screen,scale[0],punto_choque,1)
    if(energia >= 8 and energia <= 15):
        pygame.draw.circle(screen,scale[1],punto_choque,1)
    if(energia >= 16 and energia <= 23):
        pygame.draw.circle(screen,scale[2],punto_choque,1)
    if(energia >= 24 and energia <= 31):
        pygame.draw.circle(screen,scale[3],punto_choque,1)
    if(energia >= 32 and energia <= 39):
        pygame.draw.circle(screen,scale[4],punto_choque,1)
    if(energia >= 40 and energia <= 47):
        pygame.draw.circle(screen,scale[5],punto_choque,1)
    if(energia >= 48 and energia <= 55):
        pygame.draw.circle(screen,scale[6],punto_choque,1)
    if(energia >= 56 and energia <= 63):
        pygame.draw.circle(screen,scale[7],punto_choque,1)
    if(energia >= 64 and energia <= 71):
        pygame.draw.circle(screen,scale[8],punto_choque,1)
    if(energia >= 72 and energia <= 79):
        pygame.draw.circle(screen,scale[9],punto_choque,1)
    if(energia >= 80 and energia <= 87):
        pygame.draw.circle(screen,scale[10],punto_choque,1)
    if(energia >= 88 and energia <= 95):
        pygame.draw.circle(screen,scale[11],punto_choque,1)
    if(energia >= 96 and energia <= 103):
        pygame.draw.circle(screen,scale[12],punto_choque,1)
    if(energia >= 104 and energia <= 111):
        pygame.draw.circle(screen, scale[13], punto_choque, 1)
    if(energia >= 112 and energia <= 119):
        pygame.draw.circle(screen, scale[14], punto_choque, 1)
    if(energia >= 120 and energia <= 127):
        pygame.draw.circle(screen, scale[15], punto_choque, 1)
    if(energia >= 128 and energia <= 135):
        pygame.draw.circle(screen, scale[16], punto_choque, 1)
    if(energia >= 136 and energia <= 143):
        pygame.draw.circle(screen, scale[17], punto_choque, 1)
    if(energia >= 144 and energia <= 151):
        pygame.draw.circle(screen, scale[18], punto_choque, 1)
    if(energia >= 152 and energia <= 159):
        pygame.draw.circle(screen, scale[19], punto_choque, 1)
    if(energia >= 160 and energia <= 167):
        pygame.draw.circle(screen, scale[20], punto_choque, 1)
    if(energia >= 168 and energia <= 175):
        pygame.draw.circle(screen, scale[21], punto_choque, 1)
    if(energia >= 176 and energia <= 183):
        pygame.draw.circle(screen, scale[22], punto_choque, 1)
    if(energia >= 184 and energia <= 191):
        pygame.draw.circle(screen, scale[23], punto_choque, 1)
    if(energia >= 192 and energia <= 199):
        pygame.draw.circle(screen, scale[24], punto_choque, 1)
    if(energia >= 200 and energia <= 207):
        pygame.draw.circle(screen, scale[25], punto_choque, 1)
    if(energia >= 208 and energia <= 215):
        pygame.draw.circle(screen, scale[26], punto_choque, 1)
    if(energia >= 216 and energia <= 223):
        pygame.draw.circle(screen, scale[27], punto_choque, 1)
    if(energia >= 224 and energia <= 231):
        pygame.draw.circle(screen, scale[28], punto_choque, 1)
    if(energia >= 232 and energia <= 239):
        pygame.draw.circle(screen, scale[29], punto_choque, 1)
    if(energia >= 240 and energia <= 246):
        pygame.draw.circle(screen, scale[30], punto_choque, 1)
    if(energia >= 247 and energia <= 250):
        pygame.draw.circle(screen, scale[31], punto_choque, 1)
    if(energia >= 251 and energia <= 255):
        pygame.draw.circle(screen, scale[32], punto_choque, 1)


pintaColisionEscalable((400, 600), 211)



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
origen = Point(aleatorio_posicion_sonar_x, aleatorio_posicion_sonar_y)
#origen = Point(250, 250)

# Primera recursibidad
sonar = Sonar(origen,angulo_limite_izquierda, angulo_limite_derecha)

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
            ([Point(520, 555), Point(415, 555)]),
            ([Point(380, 590), Point(380, 486)]),
            ([Point(380, 486), Point(340, 486)]),
            ([Point(520, 520), Point(560, 520)]),
            ([Point(380, 450), Point(380, 335)])
            ]
for i in segments:
    pygame.draw.line(screen, blue, (i[0].x, i[0].y), (i[1].x, i[1].y), 2)

#Start
sonar.ejecutar()

# Rayos
conjunto_aleatorio = []
total_rayos_aleatorios = random.randint(30, 40)
for num in range(0,total_rayos_aleatorios):
    rayo_aleatorio = random.randint(0,len(conjunto_rayos)-1)
    rayo = conjunto_rayos.pop(rayo_aleatorio)
    conjunto_aleatorio.append(rayo)
print("Total de rayos %s" % len(conjunto_aleatorio))

# Intersección
grupo_choque = []
for imp1 in conjunto_aleatorio:
    cont = 0
    for imp2 in segments:
        if intersect(imp1[0],imp1[1],imp2[0],imp2[1]) and cont == 0:
            grupo_choque.append(([Point(imp1[0].x, imp1[0].y), Point(imp1[1].x, imp1[1].y), imp1[2], Point(imp2[0].x, imp2[0].y), Point(imp2[1].x, imp2[1].y)]))
            cont = 1
            print("Distancia:%s" % imp1[2])

# Matriz de pixeles, Rayo reflejado
matriz_pixeles = pygame.PixelArray(screen)
choque = []
segmento_rayos = []
segmento_rayos2 = []
for hp in grupo_choque:
    cont = 0
    anguloReflejoHipot = ()
    hp1x = int(round(hp[1].x))
    hp1y = int(round(hp[1].y))
    angulo_pared = getAngulo(hp[4], hp[3])
    trayectoria_rayo = getRoute(hp[0], Point(hp1x, hp1y), (300))
    for h in trayectoria_rayo:
        x = int(round(h.x))
        y = int(round(h.y))
        if matriz_pixeles[x][y] != screen.map_rgb(black) and matriz_pixeles[x][y] != screen.map_rgb(green) and cont == 0:
            choque.append(Point(x,y))
            anguloReflejoHipot = obtenerAnguloDeReflexion2(angulo_pared, hp[2])
            finalRayoHipot = (x+150*cos(anguloReflejoHipot),
                              y+150*sin(anguloReflejoHipot))
            pygame.draw.line(screen, green, (x, y), finalRayoHipot, 1)
            cont = 1
            
    rayoPrimigenio = Rayo(hp[2], origen)
    rayo_eco = Rayo(angulo_pared, anguloReflejoHipot)
    segmento_rayos.append(([rayoPrimigenio, rayo_eco]))

    rayoPrimigenio2 = [hp[2], origen]
    rayo_eco2 = [angulo_pared, anguloReflejoHipot]
    segmento_rayos2.append(([rayoPrimigenio2, rayo_eco2]))

#Impresiones
for f in range(0,len(choque)):
    print("Colision: x: %s. y: %s" % (choque[f].x,choque[f].y))
print("len(grupo_choque):%s. len(choque):%s." %
      (len(grupo_choque), len(choque)))
for u in segmento_rayos2:
    print("rayoPrimarioDistancia:%s. rayoPrimarioOrigen:%s. rayoEcoAnguloPared:%s. rayoEcoAnguloReflejoHipot:%s" %
          (u[0][0], u[0][1], u[1][0], u[1][1]))
    
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
