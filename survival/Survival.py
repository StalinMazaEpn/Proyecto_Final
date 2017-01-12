import sys
import pygame
from pygame.locals import *
 
anchoPantalla = 900
altoPantalla = 380
ubicacionP1=250

cont=9# contador que aumentara en el bucle principal para la velocidad de los sprites
direccionP1= True
i=0

posicionDer= {} #comienza y  finaliza cada sprite del personaje
posicionIzq={}

def movimiento_Personaje1():
    global cont  
    contCambiar=9
    global i
    posicionDer[0]=(0,0,34,61)
    posicionDer[1]=(33,0,45,61)
    posicionDer[2]=(75,0,55,61)
    posicionDer[3]=(130,0,40,61)
    posicionDer[4]=(170,0,45,61)
    posicionDer[5]=(220,0,45,61)
    posicionDer[6]=(270,0,44,61)
    posicionDer[7]=(310,0,43,61)
    posicionDer[8]=(352,0,45,61)
   
    posicionIzq[0]=(380,0,45,61)
    posicionIzq[1]=(337,0,44,61)
    posicionIzq[2]=(285,0,51,61)
    posicionIzq[3]=(245,0,40,61)
    posicionIzq[4]=(200,0,45,61)
    posicionIzq[5]=(150,0,40,61)
    posicionIzq[6]=(105,0,40,61)
    posicionIzq[7]=(62,0,40,61)
    posicionIzq[8]=(20,0,40,61)
 
    if cont==contCambiar:
        i=0
        
    if cont==contCambiar*1:
        i=1
    if cont==contCambiar*2:
        i=2
    if cont==contCambiar*3:
        i=3
    if cont==contCambiar*4:
        i=4
    if cont==contCambiar*5:
       i=5
    if cont==contCambiar*6:
        i=6
    if cont==contCambiar*7:
        i=7
    if cont==contCambiar*8:
        i=8
        cont=0
 

def movimiento_teclado_P1():
    teclado = pygame.key.get_pressed()

    global ubicacionP1
    global i
    global cont, direccionP1
    
    if teclado[K_RIGHT]:
        ubicacionP1 +=2
        cont+=1
        direccionP1=True
    elif teclado[K_LEFT]:
        ubicacionP1-=2
        cont+=1
        direccionP1=False
    else:
        i=0
        direccionAlterna=True

pygame.init()# inicializa pygame

screen = pygame.display.set_mode((anchoPantalla, altoPantalla))#ancho y alto de pantalla
pygame.display.set_caption("SURVIVAL")#titulo  a la ventana
fondo = pygame.image.load('fondo1.jpg').convert()# fondo para la pantalla
personaje1= pygame.image.load('personaje1.png').convert()#sprites personaje1
color= personaje1.get_at((0,0))# color transparente
personaje1.set_colorkey(color,RLEACCEL)#hace transparente el fondo del sprite del personaje
personaje1_inv= pygame.transform.flip(personaje1,True,False);#Invierte el sprite,TRUE invierte la imagen al eje X, y FLASE quiere invertir de arriba poara abajo

clock = pygame.time.Clock()# tiempo en de los fotogramas

#bucle principal
while True:
    time= clock.tick(80)
    movimiento_Personaje1()
    movimiento_teclado_P1()
        
    fondo= pygame.transform.scale(fondo,(1000,400))#Agranda o Achica la imagen segun las dimensiones que se de
    screen.blit(fondo,(0,0))#dibuja la imagen

    if direccionP1== True:#si se presiona la tecla derecha imprimira sprites normales
        screen.blit(personaje1,(ubicacionP1, 280),(posicionDer[i]))
    if direccionP1 == False:# si se presiona izquierda imprimira sprites ivertidos
        screen.blit(personaje1_inv,(ubicacionP1, 280),(posicionIzq[i]))
    
        
    pygame.display.flip()#actualiza la pantalla

        
    for eventos in pygame.event.get():# determina si el usuario dio presiona salir y cierra el juego
        if eventos.type == QUIT:
            pygame.quit()




