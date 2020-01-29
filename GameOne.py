import pygame
import sys
import time
import random

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
size2 = width-600, height-600
background = pygame.transform.scale(pygame.image.load("background.png"), (1920,1080))
# RED = (255, 0, 0)
ship = pygame.image.load("vaisseau.png") #Chargement du vaisseau
ship2 = pygame.image.load("vaisseau2.png") #Chargement du 2eme vaisseau
# meteorite = pygame.image.load("nyan_cat.png") #Chargement de la meteorite

x = width/2 #x du vaisseau
y = (height/2)+250 #y du vaisseau
x2 = width/2 #y du 2eme vaisseau
y2 = 0 #y du 2eme vaisseau
# xM = width/2 #x de la meteorite
# yM = 0 #y de la meteorite
# randy = random.randint(30, 40)#creation d'un nombre random pour le y de la meteorite

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE: #Quitter si echap appuyee
            sys.exit()
        elif event.key == pygame.K_LEFT: #Deplacement gauche
            x -= 10
        elif event.key == pygame.K_RIGHT: #Deplacement Droit
            x += 10

    if x >= width-160: #if pour eviter que le vaisseau sorte du cadre
        x -= 10
    if x <= -20: #if pour eviter que le vaisseau sorte du cadre
        x += 10

    randx = random.randint(-40, 40) #creation d'un nombre random pour le x de la meteorite
    x2 += randx
    print(x2)
    print(randx)
    # time.sleep(1)
    # yM += randy #Fait descendre la meteorite
    # xM += randx #Fait l'orientation horizontale de la meteorite

    # if yM >= 1920:
        # print("test")

    screen.blit(background, (0,0)) #Affichage du background
    screen.blit(ship, (x,y)) #Afficher le vaisseau
    screen.blit(ship2, (x2,y2)) #Afficher la meteorite
    # time.sleep(0.01)
    pygame.display.flip()
