import pygame,sys
##from pygame.locals import *
from Clases import Cursor,Boton

color = (225,225,225)
##color2 = pygame.Color(255,120,9)

pygame.init()#sentencia obligatoria
ventana = pygame.display.set_mode((600,500))#recibe una tupla
pygame.display.set_caption("Menu")
imagen1 = pygame.image.load("boton1.jpg")
imagen2 = pygame.image.load("boton1.1.jpg")
imagen3 = pygame.image.load("boton2.jpg")
imagen4 = pygame.image.load("boton2.1.jpg")
imagen5 = pygame.image.load("boton3.jpg")
imagen6 = pygame.image.load("boton3.1.jpg")

cursor1 = Cursor()
boton1 = Boton(imagen1,imagen2,200,10)
boton2 = Boton(imagen3,imagen4,200,110)
boton3 = Boton(imagen5,imagen6,200,210)

#mostrar esa ventana
while True:
    ventana.fill(color)#llena a la ventana
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                print("boton1")
            elif cursor1.colliderect(boton2.rect):
                print("boton2")
            elif cursor1.colliderect(boton3.rect):
                print("boton3")
        if evento.type == pygame.QUIT:
            pygame.quit()#detenemos todos los modulos
            sys.exit()
    cursor1.update()
    boton1.update(ventana,cursor1)
    boton2.update(ventana,cursor1)
    boton3.update(ventana,cursor1)
    pygame.display.update()
