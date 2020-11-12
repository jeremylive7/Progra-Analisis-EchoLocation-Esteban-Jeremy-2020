
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
# Comentarios
# ------------------------------

#if event.type == pygame.MOUSEBUTTONDOWN:
#if event.type == pygame.MOUSEBUTTONUP:
#    pass

#pygame.display.update() es lo mismo que pygame.display.flip()
#screen.fill(BLACK) es lo mismo que screen.blit(surface2,..)

        #surface.fill(BLACK)
        #surface.blit(surface2, rect2)
        #surface.blit(surface3, rect3)
        #surface.blit(surface4, rect4)

surface3 = pygame.Surface((0, 0), pygame.SRCALPHA)
surface3.fill(BLACK)
rect3 = surface3.get_rect()
rect3.center = (200, 200)

##Sonar
surface4 = pygame.Surface((0, 0), pygame.SRCALPHA)
surface4.fill(BLACK)
rect4 = surface4.get_rect()
rect4.center = (300, 300)

#for circulo in puntos:
#    surface.fill(BLACK)
#    surface.blit(surface2, circulo)

pygame.draw.line(surface, WHITE, (400, 210), (400, 400))
pygame.draw.line(surface, WHITE, (250, 400), (400, 210))
pygame.draw.line(surface, WHITE, (250, 400), (400, 400))

pygame.draw.line(surface, WHITE, (800, 610), (800, 800))
pygame.draw.line(surface, WHITE, (650, 800), (800, 610))
pygame.draw.line(surface, WHITE, (650, 800), (800, 800))

pygame.draw.line(surface, WHITE, (800, 410), (800, 600))
pygame.draw.line(surface, WHITE, (650, 600), (800, 410))
pygame.draw.line(surface, WHITE, (650, 600), (800, 600))


#Rayo primario
#Supongo que el random dio 2, direccion derecha inferior
for num in range(0, ((SCREEN_WIDTH // 2) // 5) - 16):
    rayo.x = pos_rayo_x
    rayo.y = pos_rayo_y
    punto = pygame.draw.circle(surface, WHITE, (rayo.x, rayo.y), 1)
    puntos_rayo_primario.append(punto)
    pos_rayo_x += 5
    pos_rayo_y += 5

    #Evento de mouse, se mueve circulo
    posx, posy = pygame.mouse.get_pos()
    rayo.center = (posx, posy)
    pygame.draw.circle(surface, WHITE, rayo.center, 1)

           #Colision con pared de la izquierda
           for y in range(5, 875):
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

            #Colision con pared de la derecha
            for k in range(5, 875):
                dist5 = math.hypot(rayo.x - 1035, rayo.y - k)
                if dist5 < (1 + 1):
                    print('Colision con pared de la derecha.')

            #distacia
            #mess='La distancia es de {}'.format( str(int(dist2)))

            #Colision con sonar
            #dist = math.hypot(posx - sonar[0],  posy - sonar[1])
            #if dist < (1 + 1):
            #    print('Llego al sonar.')


todosRayos = []
def todosLosRayosTodasDirecciones():
    #Inserto rayo de la derecha inferior
    for num in range(0, ((SCREEN_WIDTH // 2) // 5) - 16):
        posicion_x = sonar[0]
        posicion_y = sonar[1]
        rayo.x = posicion_x
        rayo.y = posicion_x
        punto = [rayo.x, rayo.y]
        posicion_x += 5
        posicion_y += 5
        todosRayos.append(punto)

    #Inseto rayo de la derecha
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x += 5
    todosRayos.append(punto)

    #Inserto rayo de la arriba
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_y += 5
    todosRayos.append(punto)

    #Inserto rayo izquierda
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x -= 5
    todosRayos.append(punto)

    #Inserto rayo abajo
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_y -= 5
    todosRayos.append(punto)

    #Inserto rayo izquirda superior
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x -= 5
    posicion_y -= 5
    todosRayos.append(punto)

    #Inserto rayo derecha superior
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x += 5
    posicion_y -= 5
    todosRayos.append(punto)
    
    #Inserto rayo izquierda inferior
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x -= 5
    posicion_y += 5
    todosRayos.append(punto)

    #Inserto rayo izquierda inferior 2
    posicion_x = sonar[0]
    posicion_y = sonar[1]
    rayo.x = posicion_x
    rayo.y = posicion_x
    punto = [rayo.x, rayo.y]
    posicion_x -= 2.5
    posicion_y += 3.5
    todosRayos.append(punto)



estructura = []
def obtencionDeRayos(x:int, y:int, direccion:float):
    print ('Cargando rayos...')   
    #La direccion es 1.8 
    #El angulo es 120 grados
    
    obtencionDeRayos(400,400,0.8)
    print (estructura)


#Metodos de obtencion de rayo reflector

#Metodo de formula de reflexion difusa

#Metodo de definir cuantas llamadas recursivas son
