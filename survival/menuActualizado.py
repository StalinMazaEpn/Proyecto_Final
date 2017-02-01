import pygame,sys
##from pygame.locals import *
from Clases import Cursor,Boton
from Survival import bucle_juego

color = (225,225,225)
##color2 = pygame.Color(255,120,9)

pygame.init()#sentencia obligatoria
ventana = pygame.display.set_mode((800,600))#recibe una tupla
pygame.display.set_caption("Menu")
imagen1 = pygame.image.load("imagenes/boton1.jpg")
imagen2 = pygame.image.load("imagenes/boton1.1.jpg")
imagen3 = pygame.image.load("imagenes/boton2.jpg")
imagen4 = pygame.image.load("imagenes/boton2.1.jpg")
imagen5 = pygame.image.load("imagenes/boton3.jpg")
imagen6 = pygame.image.load("imagenes/boton3.1.jpg")

fondo = pygame.image.load("imagenes/fondo.jpg")

cursor1 = Cursor()
boton1 = Boton(imagen1,imagen2,285,250)
boton2 = Boton(imagen3,imagen4,285,350)
boton3 = Boton(imagen5,imagen6,285,450)
pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play()
#mostrar esa ventana
while True:
    ventana.fill(color)#llena a la ventana
    fondo = pygame.transform.scale(fondo,(800,600))
    ventana.blit(fondo,(0,0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                print("boton1")
                bucle_juego()
            elif cursor1.colliderect(boton2.rect):
                print("boton2")
            elif cursor1.colliderect(boton3.rect):
                print("boton3")
                pygame.quit()
                sys.exit()
        if evento.type == pygame.QUIT:
            pygame.quit()#detenemos todos los modulos
            sys.exit()
            
    cursor1.update()
    boton1.update(ventana,cursor1)
    boton2.update(ventana,cursor1)
    boton3.update(ventana,cursor1)
    pygame.display.update()
