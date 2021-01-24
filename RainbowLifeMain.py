import pygame
pygame.init()
WIN_WIDE = 1000
WIN_HIGH = 750
SURF_WIDE = 660
SURF_HIGH = 660
mash = 15
y_surf = (WIN_HIGH-SURF_HIGH)//2
x_surf = y_surf
n = SURF_WIDE//(mash)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 225) #1
GREEN = (0, 255, 0) #2
RED = (255, 0, 0) #3
coef = [-1, 0, 1]

Arr1 = [0] * n
for k in range(n):
    Arr1[k] = [0] * n
Arr2 = Arr1

scr = pygame.display.set_mode((WIN_WIDE, WIN_HIGH))
font = pygame.font.SysFont('couriernew', 24)

col = 'Зеленый'
def TextForSimulation():
    global font
    text14 = font.render('Для паузы', True, WHITE)
    text15 = font.render("нажмите на 'p'", True, WHITE)
    text16 = font.render('Для сброса', True, WHITE)
    text17 = font.render("нажмите на 'f'", True, WHITE)
    scr.blit(text14, (785, 45))
    scr.blit(text15, (755, 70))
    scr.blit(text16, (780, 105))
    scr.blit(text17, (755, 130))

def TextForRanking(Col):
    global font, col
    text1 = font.render('Для заселения', True, WHITE)
    text2 = font.render('щелкайте по клеткам', True, WHITE)
    text3 = font.render('Текущий цвет:', True, WHITE)

    if Col == RED:
        pygame.draw.rect(scr, BLACK, (790, 150, 150, 26))
        col = 'Красный'
    elif Col == GREEN:
        pygame.draw.rect(scr, BLACK, (790, 150, 150, 26))
        col = 'Зеленый'
    elif Col == BLUE:
        pygame.draw.rect(scr, BLACK, (790, 150, 150, 26))
        col = 'Синий'

    text4 = font.render(col, True, Col)
    text5 = font.render('Для выбора цвета', True, WHITE)
    text6 = font.render('нажмите на:', True, WHITE)
    text7 = font.render("'r' - красный", True, WHITE)
    text8 = font.render("'g' - зеленый", True, WHITE)
    text9 = font.render("'b' - синий", True, WHITE)
    text10 = font.render('Для смены поколений', True, WHITE)
    text11 = font.render("нажмите на 's'", True, WHITE)
    text12 = font.render('Для сброса', True, WHITE)
    text13 = font.render("нажмите на 'f'", True, WHITE)

    scr.blit(text1, (755, 45))
    scr.blit(text2, (720, 70))
    scr.blit(text3, (755, 120))
    if col == 'Синий':
        scr.blit(text4, (805, 150))
    else:
        scr.blit(text4, (790, 150))
    scr.blit(text5, (735, 185))
    scr.blit(text6, (775, 210))
    scr.blit(text7, (750, 235))
    scr.blit(text8, (750, 260))
    scr.blit(text9, (750, 285))
    scr.blit(text10, (720, 320))
    scr.blit(text11, (760, 345))
    scr.blit(text12, (780, 380))
    scr.blit(text13, (755, 405))

def StartFill():
    global x_surf, y_surf
    pygame.draw.rect(scr, WHITE, (x_surf, y_surf, SURF_WIDE, SURF_HIGH))
    for i in range(1, n+1):
        pygame.draw.line(scr, BLACK, (x_surf+mash*i, y_surf), (x_surf+mash*i, WIN_HIGH-y_surf))
        pygame.draw.line(scr, BLACK, (x_surf, y_surf+mash*i), (WIN_WIDE-x_surf, y_surf+mash*i))
    pygame.display.update()

def CellPaint(clik, Color):
    global x_surf, y_surf, n, mash, Arr1
    x_clik = clik[0]
    y_clik = clik[1]
    x, y = 0, 0
    i, j = 0, 0
    for i in range(n):
        if x_clik > x_surf+i*mash and x_clik < x_surf+(i+1)*mash:
            x = x_surf+i*mash
            break
    for j in range(n):
        if y_clik > y_surf+j*mash and y_clik < y_surf+(j+1)*mash:
            y = y_surf+j*mash
            break
    if (x > x_surf and x < x_surf+SURF_WIDE) and (y > y_surf and y < y_surf+SURF_WIDE):
        pygame.draw.rect(scr, Color, (x+1, y+1, mash-1, mash-1))
    if Color == BLUE:
        Arr1[j][i] = 1
    elif Color == GREEN:
        Arr1[j][i] = 2
    elif Color == RED:
        Arr1[j][i] = 3
    pygame.display.update()

def Simulation():
    N, N1, N2, N3 = 0, 0, 0, 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if Arr1[i][j] == 0:
                for k1 in coef:
                    for k2 in coef:
                        if Arr1[i + k1][j + k2] == 1:
                            N += 1
                            N1 += 1
                        elif Arr1[i + k1][j + k2] == 2:
                            N += 1
                            N2 += 1
                        elif Arr1[i + k1][j + k2] == 3:
                            N += 1
                            N3 += 1
                if N == 3:
                    if N1 == 2:
                        Arr2[i][j] = 1
                    elif N2 == 2:
                        Arr2[i][j] = 2
                    elif N3 == 2:
                        Arr2[i][j] = 3

            if Arr1[i][j] == 1:
                for k1 in coef:
                    for k2 in coef:
                        if Arr1[i + k1][j + k2] > 0 and Arr1[i + k1][j + k2] <= 3:
                            N += 1
                if N <= 2:
                    Arr2[i][j] = 1

            if Arr1[i][j] == 2:
                for k1 in coef:
                    for k2 in coef:
                        if Arr1[i + k1][j + k2] > 0 and Arr1[i + k1][j + k2] <= 3:
                            N += 1
                if N >= 3 and N <= 5:
                    Arr2[i][j] = 2

            if Arr1[i][j] == 3:
                for k1 in coef:
                    for k2 in coef:
                        if Arr1[i + k1][j + k2] > 0 and Arr1[i + k1][j + k2] <= 3:
                            N += 1
                if N >= 6 and N <= 8:
                    Arr2[i][j] = 3

game = True
sim = False
start_game = True
ranking = True
pause = False
color = GREEN
while game:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            game = False
        if i.type == pygame.KEYDOWN:
            if i.unicode == 'r' and ranking == True:
                color = RED
                print(1)
            elif i.unicode == 'g' and ranking == True:
                color = GREEN
            elif i.unicode == 'b' and ranking == True:
                color = BLUE
            elif i.unicode == 'f':
                start_game = True
            elif i.unicode == 's':
                ranking = False
                sim = True
            elif i.unicode == 'p':
                pause = True
                ranking = True
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1 and ranking == True:
                if color == RED or color == GREEN or color == BLUE:
                    CellPaint(i.pos, color)

    if start_game == True:
        StartFill()
        start_game  = False
        ranking = True

    if ranking == True:
        pygame.draw.rect(scr, BLACK, (x_surf + SURF_WIDE, 0, 300, WIN_HIGH))
        TextForRanking(color)
        pygame.display.update()
    else:
        pygame.draw.rect(scr, BLACK, (x_surf+SURF_WIDE, 0, 300, WIN_HIGH))
        TextForSimulation()
        pygame.display.update()
