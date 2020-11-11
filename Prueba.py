
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
