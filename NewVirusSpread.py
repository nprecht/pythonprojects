import pygame, sys
from random import choice,randint
from math import sqrt
import matplotlib.pyplot as plt

#pygame start values
pygame.init()
CLOCK = pygame.time.Clock()
BGCOLOR = (0,0,0)
SIZE = (1200,700)
#QUARANTINEZONE = (100,100)
SCREEN = pygame.display.set_mode(SIZE)
SCREEN.fill(BGCOLOR)
RADIUS = 10
step = 0
infectedCount = 0
pygame.display.set_caption("Virus Spread Sim")
pList = []

#matplotlib start values
xVals = []
yVals = []


class Person:
    def __init__(self,x,y,color):
        self.x = x; self.y = y; self.color = color; self.restrict = False
        self.changeX = choice([-1,1]); self.changeY = choice([-1,1])
        self.draw()
        pList.append(self)
    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x,self.y), RADIUS)
    def erase(self):
        pygame.draw.circle(SCREEN, BGCOLOR, (self.x, self.y), RADIUS)
    def move(self,step):
        if step % randint(100,200) == 0 and not self.restrict:
            self.changeX = choice([-10,10])
            self.changeY = choice([-10,10])
        elif step % randint(100,200) == 0 and self.restrict:
            self.changeX = choice([-1,0,1])
            self.changeY = choice([-1,0,1])
        self.erase()
        if self.x + self.changeX - RADIUS >= 0 and self.x + self.changeX + RADIUS <= SIZE[0]:
            self.x += self.changeX
        else:
            self.changeX = -self.changeX
        if self.y + self.changeY - RADIUS >= 0 and self.y + self.changeY + RADIUS <= SIZE[1]:
            self.y += self.changeY
        else:
            self.changeY = -self.changeY
        self.draw()


class Susceptible(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(0,0,255))

class Infectious(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(255,0,0))
        self.infectionProbability = 1/35 #probability of infecting another person on contact
        self.recoverRate = 300 #steps it takes for an infected person to recover
        self.initStep = step
    def infect(self,other):
        if sqrt((self.x-other.x)**2 + (self.y-other.y)**2) <= 2*RADIUS and randint(0,int(1/self.infectionProbability)) == 1:
            temp = (other.x,other.y)
            pList.remove(other)
            Infectious(temp[0],temp[1])
            global infectedCount
            infectedCount += 1
    def heal(self):
        if step != 0 and step != self.initStep and (step - self.initStep) % self.recoverRate == 0:
            temp = (self.x,self.y)
            pList.remove(self)
            Recovered(temp[0],temp[1])
            global infectedCount
            infectedCount -= 1

class Recovered(Person):
    def __init__(self,x,y):
        super().__init__(x,y,(125,125,125))
        
class Wuhan():
    def __init__(self,x,y):
        self.x = x; self.y = y; self.color = (0,255,0); self.infectionProbability = 1/50
    def draw(self):
        pygame.draw.circle(SCREEN, self.color, (self.x,self.y), RADIUS)
    def infect(self,other):
        if sqrt((self.x-other.x)**2 + (self.y-other.y)**2) <= 2*RADIUS and randint(0,int(1/self.infectionProbability)) == 1:
            temp = (other.x,other.y)
            pList.remove(other)
            Infectious(temp[0],temp[1])
            global infectedCount
            infectedCount += 1
    
W1 = Wuhan(600,350)

#S1 = Susceptible(100,300)
#I1 = Infectious(300,300)
#R = Recovered(500,300)

pCount=0

#create mutliple susceptible persons
for i in range(RADIUS+5,SIZE[0],75):
    for j in range(RADIUS+5,SIZE[1],75):
        Susceptible(i,j)
        pCount+=1

running = True
while running:
    CLOCK.tick(30)
    W1.draw()
    if infectedCount > 10:
        for p in pList:
            p.restrict = True
    else:
        for p in pList:
            p.restrict = False

    for i in range(len(pList)):
        pList[i].move(step)
        if isinstance(pList[i],Infectious):
            pList[i].heal()
        elif isinstance(pList[i],Susceptible):
            W1.infect(pList[i])
        for j in range(len(pList)):
            if isinstance(pList[i],Infectious) and isinstance(pList[j],Susceptible):
                pList[i].infect(pList[j])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    step += 1
    yVals.append(infectedCount)

pygame.quit()

#make plot
xVals = list(range(0,step))
plt.plot(xVals,yVals)
#plt.scatter(xVals,yVals)
plt.xlabel("Step")
plt.ylabel("Infected")
plt.show()

sys.exit()
