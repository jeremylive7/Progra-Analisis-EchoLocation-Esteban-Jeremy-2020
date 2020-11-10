
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
