import pygame, sys, copy

pygame.init()
SIZE = (800,660)
screen = pygame.display.set_mode(SIZE)
gen = 0; pop = 0; aliveCol = (255,255,0); deadCol = (0,0,255); mousePos = []
pygame.display.set_caption(f"Generation: {gen}; Population: {pop}")
Clock = pygame.time.Clock()

class Cell:
    def __init__(self,state,nbCount):
        self.state = state
        self.nbCount = nbCount

def createEmptyPop():
    newPop = []
    for _ in range(75):
        newPop.append([])
    for row in newPop:
        for _ in range(100):
            row.append(Cell(False,0))
    return newPop

currentPop = createEmptyPop()

def draw_buttons():
    pygame.draw.rect(screen,(255,255,255),(0,600,800,60)) #white background
    pygame.draw.rect(screen,(0,255,0),(30,615,200,30)) #green button
    pygame.draw.rect(screen,(255,0,0),(300,615,200,30)) #red button
    pygame.draw.rect(screen,(0,0,255),(570,615,200,30)) #blue button

def draw_cell(display, x, y, colour):
    pygame.draw.rect(display, colour, (y+1,x+1,6,6))

def draw_board(display,currentPop):
    for i in range(75): #rows
        for j in range(100): #columnss
            if currentPop[i][j].state == True:
                draw_cell(display,i*8,j*8,aliveCol)
            else:
                draw_cell(display,i*8,j*8,deadCol)

def evolve(currentPop):
    newPop = copy.deepcopy(currentPop)
    for i in range(75):
        for j in range(100):
            if currentPop[i][j].state and currentPop[i][j].nbCount != 2 and currentPop[i][j].nbCount != 3:
                invert_cells(newPop,i,j)
            elif not currentPop[i][j].state and currentPop[i][j].nbCount == 3:
                invert_cells(newPop,i,j)
    return newPop


def invert_cells(currentPop,X,Y):
    global pop
    X,Y = Y,X
    test1 = X - 1 >= 0
    test2 = X + 1 < 100
    test3 = Y - 1 >= 0
    test4 = Y + 1 < 75
    if not currentPop[Y][X].state:
        currentPop[Y][X].state = True
        pop += 1
        if test3:
            if test1:
                currentPop[Y - 1][X - 1].nbCount += 1
            if test2:
                currentPop[Y - 1][X + 1].nbCount += 1
            currentPop[Y - 1][X].nbCount += 1
        if test1:
            currentPop[Y][X-1].nbCount += 1
        if test2:
            currentPop[Y][X+1].nbCount += 1
        if test4:
            if test1:
                currentPop[Y + 1][X - 1].nbCount += 1
            if test2:
                currentPop[Y + 1][X + 1].nbCount += 1
            currentPop[Y + 1][X].nbCount += 1
    else:
        currentPop[Y][X].state = False
        pop -= 1
        if test3:
            if test1:
                currentPop[Y - 1][X - 1].nbCount -= 1
            if test2:
                currentPop[Y - 1][X + 1].nbCount -= 1
            currentPop[Y - 1][X].nbCount -= 1
        if test1:
            currentPop[Y][X - 1].nbCount -= 1
        if test2:
            currentPop[Y][X + 1].nbCount -= 1
        if test4:
            if test1:
                currentPop[Y + 1][X - 1].nbCount -= 1
            if test2:
                currentPop[Y + 1][X + 1].nbCount -= 1
            currentPop[Y + 1][X].nbCount -= 1

def calcCells(mousePos):
    if mousePos == []:
        return
    start = mousePos[0];end = mousePos[-1]
    if 0 <= start[0] < 800 and 0 <= start[1] < 600 and 0 <= end[0] < 800 and 0 <= end[1] < 600:
        if start == end:
            invert_cells(currentPop, start[1] // 8, start[0] // 8)
        else:
            for i in range(start[1],end[1],8): #rows
                for j in range(start[0],end[0],8): #columns
                    invert_cells(currentPop,i//8,j//8)

def press_green_button():
    global currentPop,gen
    if 30 <= pygame.mouse.get_pos()[0] <= 230 and 615 <= pygame.mouse.get_pos()[1] <= 645:
        currentPop = evolve(currentPop)
        gen += 1
def press_red_button():
    global currentPop,gen
    if 300 <= pygame.mouse.get_pos()[0] <= 500 and 615 <= pygame.mouse.get_pos()[1] <= 645:
        for _ in range(10):
            currentPop = evolve(currentPop)
        gen += 10
def press_blue_button():
    global currentPop,pop,gen
    if 570 <= pygame.mouse.get_pos()[0] <= 770 and 615 <= pygame.mouse.get_pos()[1] <= 645:
        currentPop = createEmptyPop()
        pop = 0; gen = 0

running = True
while running:
    if pygame.mouse.get_pressed()[0]:
        mousePos.append(pygame.mouse.get_pos())
        press_green_button()
        press_red_button()
        press_blue_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            calcCells(mousePos)
            mousePos = []
    draw_board(screen, currentPop)
    draw_buttons()
    pygame.display.update()
    pygame.display.set_caption(f"Generation: {gen}; Population: {pop}")
    Clock.tick(120)

pygame.quit()
sys.exit()
