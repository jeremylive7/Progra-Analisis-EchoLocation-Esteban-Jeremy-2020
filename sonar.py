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
        self.x=pos.x+cos(rayo.direccionOriginal)*d
        self.y=+pos.y+sin(rayo.direccionOriginal)*d
        e=rayo.energia
        self.intensidad=(e,e,e)

class Rayo:
    def pintar(self):
        p=getPuntoFromAnguloAndDistancia(self.direccion,self.origen,50)
        pygame.draw.line(screen,red,(self.origen.x,self.origen.y),(p.x,p.y),1)
    def __init__(self,direccion,origen,distancia=0,energia=255,direccionOriginal=None,direccionPrivilegiada=None):
        self.direccion=direccion
        if direccionOriginal==None:
            self.direccionOriginal=direccion
        else:
            self.direccionOriginal=direccionOriginal
        self.origen=origen
        self.energia=energia
        self.distanciaRecorrida=distancia
        if direccionPrivilegiada!=None:
            self.restarEnergiaPorAngulo(direccionPrivilegiada)

    def getVectorDireccion(self):
        return Point(sin(direccion),cos(direccion))
    def restarEnergiaPorDistancia(self,fin):
        self.energia-=H*self.origen.distance(fin)
        return self.energia
    def restarEnergiaPorAngulo(self,b):
        """
        Simula gastar energía y retorna la energía resultante.
        """
        self.energia-=K*compararAngulos(b,self.direccion)
        return self.energia
    def lanzar(self,cantRecursividades=0,resultados=[]):
        if cantRecursividades>=QR:
            return resultados
        # Si llega al sonar, termina la llamada después de convertirse en resultado.    
        if sonar.loEscucha(self):
            puntoChoque=pos
            self.distanciaRecorrida+=self.origen.distance(puntoChoque)
            self.restarEnergiaPorDistancia(puntoChoque)
            if self.energia>0:
                resultados += [Resultado(self)]
            return resultados
        
        ##Encontrar donde choca
        choques=[]
        for pared in segments:
            choque=self.getChoqueIfChoca(pared)
            if choque != False and choque != self.origen:
                choques += [[pared,choque]]
        if len(choques) == 0:
            return resultados
        minimo=999999
        choque=None
        for x in choques:
            if x[1].distance(self.origen)<minimo:
                minimo=x[1].distance(self.origen)
                choque=x
        
        #Se ubica el ángulo de la pared y el punto en el que choca con esa pared
        anguloPared=getAngulo(choque[0][0],choque[0][1])
        puntoChoque=choque[1]
        #Luego se calcula el ángulo de reflexión
        anguloReflejo=obtenerAnguloDeReflexion(anguloPared,self.direccion)
        
        #Se realiza la simulación de que el rayo llega a la pared
        self.distanciaRecorrida+=self.origen.distance(puntoChoque)
        self.restarEnergiaPorDistancia(puntoChoque)

        #Se crean y se lanzan los rayos indispensables, el que continúa sobre el ángulo de reflejo y el que se devuelve por donde vino
        rayoReflejado=self.clone(anguloReflejo,puntoChoque)
        rayoOmega=self.clone(self.direccion+pi,puntoChoque,anguloReflejo)

        #rayoOmega.pintar()
        #rayoReflejado.pintar()

        rayoOmega.lanzar(cantRecursividades+1,resultados)
        rayoReflejado.lanzar(cantRecursividades+1,resultados)
        
        #Por último se tiran rayos secundarios desde self.origen, pierde energía respecto al ángulo de self.dirección y teniendo en cuenta el ángulo de visión que tiene jaja :'v
        cantRayosSecundarios=abs(int(random.normalvariate(10,5)))
        for _ in range(cantRayosSecundarios):
            direccion=random.normalvariate(self.direccion,pi/4)
            nuevoRayo=self.clone(direccion,self.origen,self.direccion)
            #nuevoRayo.pintar()
            nuevoRayo.lanzar(cantRecursividades+1, resultados)
        return resultados
    def clone(self,nuevaDireccion,nuevoOrigen,direccionPrivilegiada=None):
        return Rayo(nuevaDireccion,nuevoOrigen,self.distanciaRecorrida,self.energia,self.direccionOriginal,direccionPrivilegiada=direccionPrivilegiada)
    
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
    def __init__(self,posicion:Point,low:float,high:float,cantRayosPrimigenios):
        self.cantRayosPrimigenios=abs(int(cantRayosPrimigenios))
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
        if rayo.origen==pos:
            return False
        distancia=pos.distance(rayo.origen)
        p=Point(rayo.origen.x+distancia*cos(rayo.direccion),rayo.origen.y+distancia*sin(rayo.direccion))
        if p.distance(pos)>10:
            return False
        for pared in segments:
            choque=rayo.getChoqueIfChoca(pared)
            if choque!=False and distancia>choque.distance(rayo.origen)and choque.distance(pos)<distancia:
                return False
        return True

    def ejecutar(self):
        for _ in range(self.cantRayosPrimigenios):
            rayoPrimigenio=Rayo(random.uniform(self.low,self.high),pos)
            resultados=rayoPrimigenio.lanzar()
            if len(resultados)>0:
                for resultado in resultados:
                    #calcular distancia con el sonar desde el punto de choque y restarle la energía al reflejo perfecto
                    #pygame.draw.circle(screen,resultadoRebotePerfecto.intensidad,(int(resultadoRebotePerfecto.x),int(resultadoRebotePerfecto.y)),2)
                    if int(resultado.x)>0 and int(resultado.x)<len(px)  and int(resultado.y)>0 and int(resultado.y)<len(px[int(resultado.x)]) and getRGBfromI(px[int(resultado.x)][int(resultado.y)])[0]<resultado.intensidad[0]:
                        px[int(resultado.x)][int(resultado.y)]=resultado.intensidad
        print("FIN")
                    #print(f"Se registró un resultado en ({resultadoRebotePerfecto.x}, {resultadoRebotePerfecto.y}) con intensidad: {int(resultadoRebotePerfecto.intensidad[0])}!!!%$")
            #finalLinea=puntoChoqueHipot
            #finalRayoHipot=(finalLinea[0]+300*cos(anguloReflejoHipot),finalLinea[1]+300*sin(anguloReflejoHipot))
            
            #pygame.draw.line(screen, grisamarillento, (pos.x,pos.y), finalLinea, 1)
            #pygame.draw.line(screen, (0, 145, 77),finalLinea,finalRayoHipot,1)
            
            #resultados=enviarSonido(direccion)
            #for resultado in resultados:
                #px[resultado.posicion.x][resultado.posicion.y]=(resultado.intensidad,resultado.intensidad,resultado.intensidad)
def anguloPrincipal(angulo):
    while angulo<-pi or angulo>pi:
        angulo+=2*pi*(1-2*(angulo>pi))
    return angulo
def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue
    
    
    

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
pygame.display.set_caption("Sonar")
clock = pygame.time.Clock()

#init random
random.seed()
def getSonar():
    angulos_direcciones = [0, pi*5/6, pi*3/4, pi*2/3, pi/2, pi/3, pi/4, pi/6, pi, -pi/6, -pi/4, -pi/3, -pi/2, -pi*2/3, -pi*3/4, -pi*5/6]
    largo_angulos_posibles = len(angulos_direcciones)-1

    # Recursibidad posiciones aleatorias del Sonar
    total_rayos_aleatorios = random.normalvariate(10000,20)
    sonar_inicial_random = random.randint(0, largo_angulos_posibles)
    sonar_inicial = angulos_direcciones[sonar_inicial_random]
    angulo_limite_izquierda = sonar_inicial_random-1
    angulo_limite_derecha = sonar_inicial_random+1
    if angulo_limite_derecha > largo_angulos_posibles:
        angulo_limite_derecha = 0
    if angulo_limite_izquierda < 0:
        angulo_limite_izquierda = largo_angulos_posibles
    x_limite_sonar_izq = int(round((w+(2*border))/4))
    x_limite_sonar_der = int(round(((w+(2*border))/(1/8)/10)))
    y_limite_sonar_izq = int(round((h+(2*border))/4))
    y_limite_sonar_der = int(round(((h+(2*border))/(1/8)/10)))
    aleatorio_posicion_sonar_x = random.randint(x_limite_sonar_izq, x_limite_sonar_der)
    aleatorio_posicion_sonar_y = random.randint(y_limite_sonar_izq, y_limite_sonar_der)
    origen = Point(aleatorio_posicion_sonar_x, aleatorio_posicion_sonar_y)
    return Sonar(origen,angulos_direcciones[angulo_limite_izquierda], angulos_direcciones[angulo_limite_derecha]+pi,total_rayos_aleatorios)
sonar=getSonar()
CANT_SONARES=10
K=150 #Para pérdida de energía por el ángulo
H=1/5#Para pérdida de energía por distancia
QR=3
pos=Point(400,300)
px[int(pos.x)][int(pos.y)]=red
#warning, point order affects intersection test!!
segments = [
    ([Point(28,126), Point(6,197)]), 
    ([Point(6,197), Point(31, 197)]),
    ([Point(31, 197), Point(39, 168)]),
    ([Point(39, 168), Point(73, 168)]),
    ([Point(47, 168), Point(45,181)]),
    ([Point(45,181), Point(61, 181)]),
    ([Point(61, 181), Point(65,168)]),
    ([Point(73, 168), Point(67,198)]),
    ([Point(67,198), Point(90, 197)]),
    ([Point(90, 197), Point(106,127)]),
    [Point(106,126), Point(84,126)],
    [Point(84,126), Point(81,139)],
    [Point(72,139), Point(81,139)],
    [Point(72,139), Point(70,152)],
    [Point(70,152), Point(53,152)],
    [Point(55,140), Point(53,152)],
    [Point(55,140), Point(48,140)],
    [Point(48,140), Point(52,127)],
    [Point(52,127), Point(29,127)],
    [Point(115,127), Point(135,127)],
    [Point(115,127), Point(101,197)],
    [Point(101,197), Point(123,197)],
    [Point(123,197), Point(135,127)],
    [Point(146,127), Point(133,197)],
    [Point(133,197), Point(158,197)],
    [Point(158,197), Point(164,160)],
    [Point(164,160), Point(172,160)],
    [Point(172,160), Point(171,173)],
    [Point(171,173), Point(178,173)],
    [Point(178,173), Point(177,197)],
    [Point(199,197), Point(177,197)],
    [Point(199,197), Point(208,127)],
    [Point(208,127), Point(185,127)],
    [Point(185,127), Point(182,151)],
    [Point(173,151), Point(174,140)],
    [Point(174,140), Point(166,140)],
    [Point(166,140), Point(167,127)],
    [Point(167,127), Point(145,127)],
    [Point(218,127), Point(210,197)],
    [Point(268,197), Point(210,197)],
    [Point(268,197), Point(268,182)],
    [Point(268,182), Point(236,182)],
    [Point(236,182), Point(238,140)],
    [Point(236,166), Point(269,166)],
    [Point(269,166), Point(269,153)],
    [Point(269,153), Point(238,153)],
    [Point(239,139), Point(270,139)],
    [Point(270,139), Point(270,127)],
    [Point(279,127), Point(277,197)],
    [Point(289,197), Point(290,194)],
    [Point(298,193), Point(290,194)],
    [Point(298,193), Point(299,196)],
    [Point(299,196), Point(303,197)],
    [Point(303,197), Point(322,197)],
    [Point(322,197), Point(323,188)],
    [Point(323,188), Point(325,197)],
    [Point(325,197), Point(334,197)],
    [Point(334,197), Point(334,183)],
    [Point(334,183), Point(301,183)],
    [Point(301,183), Point(301,140)],
    [Point(301,140), Point(334,139)],
    [Point(334,140), Point(333,127)],
    [Point(333,127), Point(279,127)],
    [Point(342,127), Point(345,197)],
    [Point(345,197), Point(368,197)],
    [Point(368,197), Point(369,167)],
    [Point(369,166), Point(377,166)],
    [Point(377,166), Point(380,197)],
    [Point(380,197), Point(401,197)],
    [Point(401,197), Point(399,161)],
    [Point(399,161), Point(391,161)],
    [Point(391,161), Point(383,159)],
    [Point(383,159), Point(389,157)],
    [Point(389,157), Point(390,152)],
    [Point(390,152), Point(397,152)],
    [Point(397,152), Point(396,127)],
    [Point(396,127), Point(342,127)],
    [Point(405,127), Point(414,196)],
    [Point(435,196), Point(414,196)],
    [Point(435,196), Point(433,172)],
    [Point(443,172), Point(433,172)],
    [Point(443,172), Point(447,197)],
    [Point(447,197), Point(469,197)],
    [Point(469,197), Point(459,127)],
    [Point(459,127), Point(405,127)],
    [Point(469,127), Point(482,197)],
    [Point(482,197), Point(504,197)],
    [Point(504,197), Point(497,166)],
    [Point(497,166), Point(529,166)],
    [Point(529,166), Point(528,153)],
    [Point(496,153), Point(528,153)],
    [Point(496,153), Point(492,140)],
    [Point(492,140), Point(524,139)],
    [Point(524,140), Point(521,127)],
    [Point(521,127), Point(467,127)],
    [Point(530,126), Point(533,139)],
    [Point(533,139), Point(588,139)],
    [Point(551,140), Point(566,196)],
    [Point(566,196), Point(589,197)],
    [Point(589,197), Point(572,140)],
    [Point(585,127), Point(531,127)],
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
        px[int(pos.x)][int(pos.y)]=red
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type==pygame.KEYDOWN:
                    if event.key in [pygame.K_DOWN,pygame.K_UP,pygame.K_RIGHT,pygame.K_LEFT]:
                        px[int(pos.x),int(pos.y)]=(0,0,0)
                    if event.key==pygame.K_DOWN:
                        pos=Point(pos.x,pos.y+4)
                    if event.key==pygame.K_UP:
                        pos=Point(pos.x,pos.y-4)
                    if event.key==pygame.K_LEFT:
                        pos=Point(pos.x-4,pos.y)
                    if event.key==pygame.K_RIGHT:
                        pos=Point(pos.x+4,pos.y)
                    if event.key==pygame.K_b:
                        sonar.low+=pi/8
                        sonar.high+=pi/8
                        print (f"low: {sonar.low}\thigh: {sonar.high}")
                    if event.key==pygame.K_a:
                        sonar.low-=pi/8
                        sonar.high-=pi/8
                        print (f"low: {sonar.low}\thigh: {sonar.high}")
                    if event.key in [pygame.K_DOWN,pygame.K_UP,pygame.K_RIGHT,pygame.K_LEFT]:
                        print("hola")
                        px[int(pos.x),int(pos.y)]=red
        pygame.display.update()
        clock.tick(60)
pygame.quit()
quit()
