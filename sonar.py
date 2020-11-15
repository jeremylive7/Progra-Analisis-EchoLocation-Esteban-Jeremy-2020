import numpy as np 
import pygame
import random
from PIL import Image
from Point import *
import math
import threading
from math import atan,sin,cos,asin,acos,pi,inf
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
def obtenerAnguloDeReflexion(s,r):
        s+=pi/2
        return pi-(r-s)+s
def getPuntoFromAnguloAndDistancia(angulo,origen=Point(0,0),distancia=9999):
    return Point(distancia*cos(angulo)+origen.x,distancia*sin(angulo)+origen.y)
class Resultado:
    def __init__(self,rayo):
        self.x=3
    def __init__(self):
        pass

class Rayo:
    def __init__(self,direccion,origen,distancia=0,energia=255,direccionOriginal=None):
        self.direccion=direccion
        if direccionOriginal==None:
            self.direccionOriginal=direccion
        self.origen=origen
        self.energia=energia
        self.distanciaRecorrida=distancia
    def getVectorDireccion(self):
        return Point(sin(direccion),cos(direccion))
    def parseResultado(self,distanciaFinal):
        self.distanciaRecorrida+=distanciaFinal
        return Resultado(self)
    def restarEnergiaPorDistancia(self,fin):
        self.energia-=H*origen.distancia(fin)
        return self.energia
    def lanzar(self,cantRecursividades=0,resultados=[],puntoChoque=None):
        if cantRecursividades>=2:
            return resultados
        ##  V1
        #puntoQueChoca,segmentoConQueChoca=buscarPuntoDeImpacto(self.direccion,self.origen)#Considerando la oreja del sonar
        #if self.loEscucha(puntoQueChoca): pass
        #energia=restarEnergia(energia,origen,puntoQueChoca)        
        #anguloDeIncidencia=obtenerAnguloDeReflexion(segmentoConQueChoca,direccion)
        ##################################
        ## V2
        for pared in segments:
            choque=self.getChoqueIfChoca(pared)
            if choque!=False:#Faltaría chequear que no se interpone nada entre esa pared y el origen del rayo T-T
                anguloPared=getAngulo(pared[0],pared[1])
                anguloReflejado=obtenerAnguloDeReflexion(anguloPared,self.direccion)
                energiaHastaAqui=restarEnergiaPorDistancia(choque)
                rayoReflejado=Rayo(anguloReflejado,choque,self.distanciaRecorrida,energiaHastaAqui)
                resultados+=rayoReflejado.lanzar(cantRecursividades+1,resultados)

                resultadoRebote=Resultado()
                resultadoRebote.x=cos(self.direccionOriginal)*self.distanciaRecorrida
                resultadoRebote.y=sin(self.direccionOriginal)*self.distanciaRecorrida
                e=self.simularGastoDeEnergiaPorAngulo(self.direccionOriginal+pi)
                resultadoRebote.intensidad=(e,e,e)
                resultados+=[resultadoRebote]
                for _ in range(CANT_RAYOS_MONTECARLO):
                    nuevoRayo=Rayo(self.direccion,puntoChoque,distancia=origen.distancia(puntoChoque),energia=nuevaEnergia)

                    resultados+=nuevoRayo.lanzar(cantRecursividades+1, resultados)
        return resultados
    def compararAngulos(self,cita,cita0):
        return pow(cos(cita-cita0),2)
    def simularGastoDeEnergiaPorAngulo(self,b):
        """
        Simula gastar energía y retorna la energía resultante.
        """
        return self.energia-K*self.compararAngulos(b,self.direccion)
    def getChoqueIfChoca(self,pared):
        X1=pared[0].x
        X2=pared[1].x
        Y1=pared[0].y
        Y2=pared[1].y
        X3=self.origen.x
        finRayo=getPuntoFromAnguloAndDistancia(self.direccion,self.origen)
        X4=finRayo.x
        Y3=self.origen.y
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
class Sonar:
    def __init__(self,posicion:Point,low:float,high:float):
        self.pos:Point=posicion
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
            rayoPrimigenio=Rayo(random.uniform(self.low,self.high),self.pos)
            anguloReflejoHipot=self.obtenerAnguloDeReflexion(-pi/2,rayoPrimigenio.direccion)
            puntoChoqueHipot=(self.pos.x+300*cos(rayoPrimigenio.direccion),self.pos.y+300*sin(rayoPrimigenio.direccion))
            rayoReflejado=Rayo(anguloReflejoHipot,puntoChoqueHipot,300,rayoPrimigenio.energia-5)
            
            resultados=rayoReflejado.lanzar(puntoChoque=puntoChoqueHipot)
            resultadoRebotePerfecto=resultados[0]
            #calcular distancia con el sonar desde el punto de choque y restarle la energía al reflejo perfecto
            
            px[int(resultadoRebotePerfecto.x)][int(resultadoRebotePerfecto.y)]=resultadoRebotePerfecto.intensidad

            #finalLinea=puntoChoqueHipot
            #finalRayoHipot=(finalLinea[0]+300*cos(anguloReflejoHipot),finalLinea[1]+300*sin(anguloReflejoHipot))
            
            #pygame.draw.line(screen, grisamarillento, (self.pos.x,self.pos.y), finalLinea, 1)
            #pygame.draw.line(screen, (0, 145, 77),finalLinea,finalRayoHipot,1)
            
            #resultados=enviarSonido(direccion)
            #for resultado in resultados:
                #px[resultado.posicion.x][resultado.posicion.y]=(resultado.intensidad,resultado.intensidad,resultado.intensidad)
    def anguloPrincipal(self,angulo):
        while angulo<-pi or angulo>pi:
            angulo+=2*pi*(1-2*(angulo>pi))
        return angulo
    
    
    
    

# COLORS
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
grisamarillento=(149, 150, 80)

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
sonar=Sonar(Point(400,300),-4*pi/5,3*pi/4)
K=10 #Para pérdida de energía por el ángulo
H=1/4#Para pérdida de energía por distancia
CANT_RAYOS_MONTECARLO=0

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
