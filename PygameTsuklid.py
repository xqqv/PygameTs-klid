
#1
import pygame
import sys


pygame.init()

lGreen = [153, 255, 153]


ekraani_pind = pygame.display.set_mode((640, 480))
ekraani_pind.fill(lGreen)
pygame.display.set_caption("Esimene mäng")

try:
    youWin = pygame.image.load("win.jpg")
except pygame.error as e:
    print(f"Не удалось загрузить изображение: {e}")
    sys.exit()
    
youWin = pygame.transform.scale(youWin, (300, 200))

gameover = False

while not gameover:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    ekraani_pind.fill(lGreen)
    ekraani_pind.blit(youWin, (170, 140))
    
  
    pygame.display.flip()

pygame.quit()

#2
import pygame
import random
import sys

pygame.init()


red = [255, 0, 0]
lGreen = [153, 255, 153]

pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Juhuslikud kujundid")
pind.fill(lGreen)

for i in range(1, 10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(pind, red, [x, y, 20, 20])
    pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()

#3
import pygame
import sys

pygame.init()


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
black = [0, 0, 0]  
red_roof = [255, 0, 0]  
brown = [139, 69, 19]  

# Экран
pind = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Majake")
pind.fill(lGreen) 

def drawHouse(x, y, width, height, screen, background_color, roof_color):
   
    pygame.draw.rect(screen, background_color, (x, y - height, width, height))
    
    pygame.draw.polygon(screen, roof_color, [
        (x, y - height),
        (x + width / 2, y - height * 5 / 4), 
        (x + width, y - height)
    ], 0)

    points = [
        (x, y - height),
        (x + width / 2, y - height * 5 / 4),
        (x + width, y - height),
        (x, y - height)
    ]
    lineThickness = 3
    pygame.draw.lines(screen, black, True, points, lineThickness)


def drawWindow(x, y, width, height, screen, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    
    pygame.draw.line(screen, (0, 0, 0), (x + width // 2, y), (x + width // 2, y + height), 2)
    pygame.draw.line(screen, (0, 0, 0), (x, y + height // 2), (x + width, y + height // 2), 2)

def drawDoor(x, y, width, height, screen, color):
    pygame.draw.rect(screen, color, (x, y, width, height))

drawHouse(100, 480, 300, 300, pind, black, red_roof)  

drawWindow(130, 280, 80, 80, pind, blue) 
drawWindow(300, 280, 80, 80, pind, blue)  

drawDoor(225, 380, 50, 100, pind, brown) 

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
