import pygame
from random import randrange

def showInsertionSort():
    
    pygame.init()
    width,height = 800,800
    length = 10
    pixel = width // length

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Insertion Sort")
    screen.fill((255, 255, 255))
    fontSize = int(pixel / 2.5)
    font = pygame.font.Font("freesansbold.ttf", fontSize)
    clock = pygame.time.Clock()
    
    def randArray(n):
        a = [randrange(n) for _ in range(n)]
        return a
    
    randList = randArray(length)
    
    def drawList(l):
        screen.fill((255,255,255))
        coords = [0,height]
        for el in l:
            pygame.draw.rect(screen, (0,0,0), (coords[0],coords[1], pixel, -el*pixel), 0)
            text = font.render(str(el), True, (0,0,0))
            screen.blit(text, (coords[0]+pixel//4, height-el*pixel-fontSize*2))
            coords[0] += pixel
        pygame.display.update()
    
    def insertion_sort(a):
        drawList(a)
        for i in range(1,len(a)):
            j = i
            clock.tick(5)
            while j > 0 and a[j-1] > a[j]:
                highlight(a,j,(255,0,0))
                a[j],a[j-1] = a[j-1],a[j]
                j-=1
                clock.tick(1)
                drawList(a)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
        drawList(a)

    def highlight(l,ind,color):
        coords = [0,height]
        for i in range(len(l)):
            el = l[i]
            if i == ind:
                pygame.draw.rect(screen, color, (coords[0],coords[1], pixel, -el*pixel), 0)
                text = font.render(str(el), True, color)
                screen.blit(text, (coords[0]+pixel//4, height-el*pixel-fontSize*2))
            coords[0] += pixel
        pygame.display.update()

    insertion_sort(randList)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()

def showSelectionSort():
    pygame.init()
    def selection_sort(a):
        drawList(a)
        for i in range(len(a)-1):
            p=i
            highlight(a,i,(255,0,0))
            #sleep(length/(100*(length/10)))
            pygame.time.delay(int(1000*length/(100*(length/10))))
            for j in range(i+1, len(a)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                highlight(a,j,(0,55,0))
                if a[j] < a[p]:
                    p = j
                #sleep(length/(100*(length/10)))
                pygame.time.delay(int(1000*length/(100*(length/10))))
            drawList(a)
            highlight(a,p,(0,255,0))
            highlight(a,i,(255,0,0))
            #sleep(3*(length/(100*(length/10))))
            pygame.time.delay(int(1000*3*(length/(100*(length/10)))))
            if p > i:
                (a[i], a[p]) = (a[p], a[i])
            clock.tick(1)
            drawList(a)
        
    def randArray(n):
        a = [randrange(n) for _ in range(n)]
        return a

    width,height = 800,800
    length = 10
    randList = randArray(length)
    pixel = width//length

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Selection Sort")
    screen.fill((255,255,255))
    fontSize = int(pixel/2.5)
    font = pygame.font.Font("freesansbold.ttf", fontSize)
    clock = pygame.time.Clock()

    def drawList(l):
        screen.fill((255,255,255))
        coords = [0,height]
        for el in l:
            pygame.draw.rect(screen, (0,0,0), (coords[0],coords[1], pixel, -el*pixel), 0)
            text = font.render(str(el), True, (0,0,0))
            screen.blit(text, (coords[0]+pixel//4, height-el*pixel-fontSize*2))
            coords[0] += pixel
        pygame.display.update()
            
    def highlight(l,ind,color):
        coords = [0,height]
        for i in range(len(l)):
            el = l[i]
            if i == ind:
                pygame.draw.rect(screen, color, (coords[0],coords[1], pixel, -el*pixel), 0)
                text = font.render(str(el), True, color)
                screen.blit(text, (coords[0]+pixel//4, height-el*pixel-fontSize*2))
            coords[0] += pixel
        pygame.display.update()

    sorting = True
    while sorting:
        selection_sort(randList)
        sorting = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
        
pygame.init()

screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
pygame.display.set_caption("Menu")
font = pygame.font.Font("freesansbold.ttf",32)

text1 = font.render("Selection Sort", True, (0,0,0))
pygame.draw.rect(screen, (0,0,0), (80, 90, 245, 52))
pygame.draw.rect(screen, (150,150,150), (85, 95, 235, 42))

text2 = font.render("Insertion Sort", True, (0,0,0))
pygame.draw.rect(screen, (0,0,0), (80, 180, 245, 52))
pygame.draw.rect(screen, (150,150,150), (85, 185, 235, 42))

menu = True
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    mouse = pygame.mouse.get_pos()
    if (mouse[0] > 80 and mouse[0] < 325) and (mouse[1] > 90 and mouse[1] < 142):
        pygame.draw.rect(screen, (0,0,0), (80, 90, 245, 52))
        pygame.draw.rect(screen, (200,200,200), (85, 95, 235, 42))
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            showSelectionSort()
    else:
        pygame.draw.rect(screen, (0,0,0), (80, 90, 245, 52))
        pygame.draw.rect(screen, (150,150,150), (85, 95, 235, 42))

    if (mouse[0] > 80 and mouse[0] < 325) and (mouse[1] > 180 and mouse[1] < 232):
        pygame.draw.rect(screen, (0,0,0), (80, 180, 245, 52))
        pygame.draw.rect(screen, (200,200,200), (85, 185, 235, 42))
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            showInsertionSort()
    else:
        pygame.draw.rect(screen, (0, 0, 0), (80, 180, 245, 52))
        pygame.draw.rect(screen, (150, 150, 150), (85, 185, 235, 42))

    screen.blit(text1, (90,100))
    screen.blit(text2, (95,190))
    pygame.display.update()