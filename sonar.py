import numpy as np 
import pygame
import random
from PIL import Image
import math
import threading
from shapely.geometry import LineString as Line,Point
from math import atan,sin,cos,asin,acos,pi,radians
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
def compararAngulos(cita,cita0):
    r=pow(cos(cita-cita0),2)
    return r
class Resultado:
    def __init__(self,rayo):
        d=rayo.distanciaRecorrida/2
        self.x=sonar.pos.x+cos(rayo.direccionOriginal)*d
        self.y=+sonar.pos.y+sin(rayo.direccionOriginal)*d
        e=rayo.energia
        self.intensidad=(e,e,e)

class Rayo:
    def pintar(self):
        p=getPuntoFromAnguloAndDistancia(self.direccion,self.origen,50)
        pygame.draw.line(screen,red,(self.origen.x,self.origen.y),(p.x,p.y),1)
    def __init__(self,direccion,origen,distancia=0,energia=255,direccionOriginal=None):
        self.direccion=direccion
        if direccionOriginal==None:
            self.direccionOriginal=direccion
        else:
            self.direccionOriginal=direccionOriginal
        self.origen=origen
        self.energia=energia
        self.distanciaRecorrida=distancia

    def getVectorDireccion(self):
        return Point(sin(direccion),cos(direccion))

    def restarEnergiaPorDistancia(self,fin):
        self.energia-=H*self.origen.distance(fin)
        return self.energia
    def lanzar(self,cantRecursividades=0,resultados=[]):
        if cantRecursividades>=2:
            return resultados
        if sonar.loEscucha(self):
            puntoChoque=sonar.pos
            self.distanciaRecorrida+=self.origen.distance(puntoChoque)
            self.restarEnergiaPorDistancia(puntoChoque)
            resultados += [Resultado(self)]
            return resultados
        
        ##Encontrar donde choca
        choques=[]
        for pared in segments:
            choque=self.getChoqueIfChoca(pared)
            if choque!=False and choque!=self.origen:
                choques+=[[pared,choque]]
        if len(choques)==0:
            return resultados

        minimo=999999
        choque=None
        for x in choques:
            if x[1].distance(self.origen)<minimo:
                minimo=x[1].distance(self.origen)
                choque=x

        ## Del choque más cercano nos importa el ángulo de la pared con la que choca y el punto de choque.
        
        #self.pintar()
        
        anguloPared=getAngulo(choque[0][0],choque[0][1])
        puntoChoque=choque[1]
        anguloReflejo=obtenerAnguloDeReflexion(anguloPared,self.direccion)
        
        #Se realiza la simulación de que el rayo llega a la pared
        self.distanciaRecorrida+=self.origen.distance(puntoChoque)
        self.restarEnergiaPorDistancia(puntoChoque)

        #Se crean y se lanzan los rayos indispensables, el que continúa sobre el ángulo de reflejo y el que se devuelve por donde vino
        rayoReflejado=Rayo(anguloReflejo,puntoChoque,self.distanciaRecorrida,self.energia,self.direccionOriginal)
        rayoOmega=Rayo(self.direccion+pi,puntoChoque,self.distanciaRecorrida,self.energia,self.direccionOriginal)
        rayoOmega.restarEnergiaPorAngulo(anguloReflejo)
        #rayoOmega.pintar()
        #rayoReflejado.pintar()

        rayoReflejado.lanzar(cantRecursividades+1,resultados)
        rayoOmega.lanzar(cantRecursividades+1,resultados)
        
        #Por último se tiran rayos secundarios desde self.origen, pierde energía respecto al ángulo de self.dirección y teniendo en cuenta el ángulo de visión que tiene jaja :'v
        #for _ in range(CANT_RAYOS_MONTECARLO):
            #nuevoRayo=Rayo(self.direccion,origen,self.distanciaRecorrida,self.energia,self.direccionOriginal)
            #nuevoRayo.lanzar(cantRecursividades+1, resultados)
        return resultados
    def restarEnergiaPorAngulo(self,b):
        """
        Simula gastar energía y retorna la energía resultante.
        """
        print(f"Energía anterior: {self.energia}")
        print(f"Ángulo rayo secundario: {b}")
        print(f"Ángulo rayo principal: {self.direccion}")
        print(f"Resultado de la comparación: {compararAngulos(b,self.direccion)}")
        print(f"Correspondiente energía a restar: {K*compararAngulos(b,self.direccion)}")
        energia=self.energia-K*compararAngulos(b,self.direccion)
        print(f"Energía final: {energia}")
        return energia
    def getChoqueIfChoca(self,pared):
        finRayo=getPuntoFromAnguloAndDistancia(self.direccion,self.origen)
        pared=Line([(pared[0].x,pared[0].y),(pared[1].x,pared[1].y)])
        rayo=Line([(self.origen.x,self.origen.y),(finRayo.x,finRayo.y)])
        interseccion=pared.intersection(rayo)
        try:
            Xi=interseccion.x
            Yi=interseccion.y
        except:
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
    def loEscucha(self,rayo):
        if rayo.origen==self.pos:
            return False
        distancia=self.pos.distance(rayo.origen)
        p=Point(rayo.origen.x+distancia*cos(rayo.direccion),rayo.origen.y+distancia*sin(rayo.direccion))
        if p.distance(self.pos)>10:
            return False
        for pared in segments:
            choque=rayo.getChoqueIfChoca(pared)
            if choque!=False and distancia>choque.distance(rayo.origen)and choque.distance(self.pos)<distancia:
                return False
        return True

    def ejecutar(self):
        for _ in range(CANTIDAD_RAYOS_PRIMIGENIOS):
            rayoPrimigenio=Rayo(random.uniform(self.low,self.high),self.pos)
            resultados=rayoPrimigenio.lanzar()
            if len(resultados)>0:
                for resultadoRebotePerfecto in resultados:
                    #calcular distancia con el sonar desde el punto de choque y restarle la energía al reflejo perfecto
                    #pygame.draw.circle(screen,resultadoRebotePerfecto.intensidad,(int(resultadoRebotePerfecto.x),int(resultadoRebotePerfecto.y)),2)
                    px[int(resultadoRebotePerfecto.x)][int(resultadoRebotePerfecto.y)]=resultadoRebotePerfecto.intensidad
                    print(f"Se registró un resultado en ({resultadoRebotePerfecto.x}, {resultadoRebotePerfecto.y}) con intensidad: {int(resultadoRebotePerfecto.intensidad[0])}!!!%$&")
                resultados=[]

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
blue=(0,0,125)
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
sonar=Sonar(Point(322,300),0,-pi)
px[int(sonar.pos.x)][int(sonar.pos.y)]=red
K=150 #Para pérdida de energía por el ángulo
H=1/5#Para pérdida de energía por distancia
CANTIDAD_RAYOS_PRIMIGENIOS=100
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
    pygame.draw.line(screen, blue, (i[0].x,i[0].y), (i[1].x,i[1].y), 1)

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
