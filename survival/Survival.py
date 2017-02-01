import sys
import pygame
from pygame.locals import *
 
anchoPantalla = 900
altoPantalla = 380
ubicacionP1=250 # ubicacion del personaje 1 en el eje X
ubicacionP1Y=280 # ubicacion del personaje 1 en el eje Y

cont=9# contador que aumentara en el bucle principal para la velocidad de los sprites
direccionP1= True
i=0

posicionDer= {} #comienza y  finaliza cada sprite del personaje
posicionIzq={}#comienza y  finaliza cada sprite del personaje de manera inversa
saltar= False # determina si salta el personaje o esta en el suelo
saltarMovi=False# determina si el personaje salto al presionar tecla derecha o izquierda

def movimiento_Personaje1():
    global cont  
    contCambiar=9
    global i
    posicionDer[0]=(0,0,34,61)#posicion de cada sprite x,y, ancho, alto
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

 # se va multiplicando contador cambiar, cada que es igual al cont del personaje
 #para ir cambiando de sprites
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
    global cont, direccionP1, saltar, saltarMovi,i
    
   #si presiona espacio, flecha derecha y la variable saltarMovi es falsa,
    #saltarMovi se igualara a Verdadero y el salto sera hacia adelante
    if teclado[K_SPACE] and teclado[K_RIGHT] == False and saltarMovi == False:
        saltarMovi = True

    #lo mismo del if anterior pero con la tecla izquierda y salto sera hacia atras
    elif teclado[K_SPACE] and teclado[K_LEFT]== False  and saltarMovi == False:
        saltarMovi = True

    # si presiono tecla derecha y las variables de saltar son falsas
    #significara que el personaje solo caminara
    elif teclado[K_RIGHT] and saltar== False and saltarMovi==False and ubicacionP1<=860:
        ubicacionP1 +=2
        cont+=1
        direccionP1=True
    # lo mismo del if anterior pero con la tecla izquierda
    elif teclado[K_LEFT] and saltar == False and saltarMovi==False and ubicacionP1>=3:
        ubicacionP1-=2
        cont+=1
        direccionP1=False
        
    #si presion espacio y las variables para saltar son falsas
    #significara que el personaje solo saltara verticalmente
    elif teclado[K_SPACE] and saltar== False and saltarMovi==False:
        saltar=True
        
    #si nada de esto sucede el personaje quedara quieto con el sprite 0
    else:
        i=0

def bucle_juego():
    pygame.init()# inicializa pygame

    screen = pygame.display.set_mode((anchoPantalla, altoPantalla))#ancho y alto de pantalla
    pygame.display.set_caption("SURVIVAL")#titulo  a la ventana
    fondo = pygame.image.load('imagenes/fondo1.jpg').convert()# fondo para la pantalla
    personaje1= pygame.image.load('imagenes/personaje1.png').convert()#sprites personaje1
    color= personaje1.get_at((0,0))# color transparente
    personaje1.set_colorkey(color,RLEACCEL)#hace transparente el fondo del sprite del personaje
    personaje1_inv= pygame.transform.flip(personaje1,True,False);#Invierte el sprite,TRUE invierte la imagen al eje X, y FLASE quiere invertir de arriba poara abajo

    bloque = pygame.image.load('Bloque.png')
    
    clock = pygame.time.Clock()# tiempo en de los fotogramas
    global saltarMovi
    caer= False # define si el personaje cae solo verticalmente
    caerMovi=False# define si el personaje cae hacia adelante o hacia atras

    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    
#BUCLE PRINCIPAL DEL JUEGO
    while True:
    
        time= clock.tick(80)
        movimiento_Personaje1()
        movimiento_teclado_P1()
        
        fondo= pygame.transform.scale(fondo,(1000,400)) #Agranda o Achica la imagen segun las dimensiones que se de
        screen.blit(fondo,(0,0))#dibuja la imagen

        ##Posiciones de los bloque en la ventana
        bloque= pygame.transform.scale(bloque,(30,30))
        screen.blit(bloque,(150,310))
        screen.blit(bloque,(190,270))
        screen.blit(bloque,(230,230))
        screen.blit(bloque,(270,190))
        screen.blit(bloque,(310,150))
        screen.blit(bloque,(350,110))
        
        screen.blit(bloque,(390,150))
        screen.blit(bloque,(430,190))
        screen.blit(bloque,(470,230))
        screen.blit(bloque,(510,270))
        screen.blit(bloque,(550,310))
        

        
        global ubicacionP1
        global ubicacionP1Y
        global saltar,i
        if direccionP1== True and saltar == False:#si se presiona la tecla derecha imprimira sprites normales
            screen.blit(personaje1,(ubicacionP1, ubicacionP1Y),(posicionDer[i]))
        if direccionP1 == False and saltar== False:# si se presiona izquierda imprimira sprites ivertidos
            screen.blit(personaje1_inv,(ubicacionP1, ubicacionP1Y),(posicionIzq[i]))

#SALTO VERTICAL DEL PERSONAJE 1
        if saltar==True: #comprueba si se presiono la tecla espacio
            if direccionP1 == True:#comprueba si se aplasto la tecla derecha para dibujar
                screen.blit(personaje1, ( ubicacionP1, ubicacionP1Y),(posicionDer[5]))
            if direccionP1 == False:#comprueba si se aplasto la tecla izquierda para dibujar invertido
                screen.blit(personaje1_inv, ( ubicacionP1, ubicacionP1Y),(posicionIzq[5]))
#si se preciono espacio y el personaje esta en el suelo ira restando 2
#para que el personaje suba
            if caer == False:
                ubicacionP1Y -=2
# si se llego a la maxima altura  que se puede saltar "170" entonces se va
#sumando 2 hasta que llegue al tope del suelo "280" 
            if caer == True:
                ubicacionP1Y +=2
            if ubicacionP1Y == 170:#maxima altura que puede llegar el salto
                caer=True
            if ubicacionP1Y == 280:#tope del suelo
                #deja al personaje en el suelo
                caer = False
                saltar=False

#SALTO CON MOVIMIENTI HACIA ATRAS O ADELANTE PERSONAJE 1
        if saltarMovi == True and direccionP1 == True:
            screen.blit(personaje1,( ubicacionP1, ubicacionP1Y),(posicionDer[5]))
            if caerMovi == False:
               ubicacionP1Y -= 2
               ubicacionP1 += 1
               
            if caerMovi == True:
                ubicacionP1Y += 2
                ubicacionP1 += 1
            if ubicacionP1Y == 170:
                caerMovi = True
            if ubicacionP1Y == 280:
                caerMovi = False
                saltarMovi = False

        elif saltarMovi == True and direccionP1 == False:
            screen.blit(personaje1_inv,(ubicacionP1, ubicacionP1Y),(posicionIzq[5]))
            if caerMovi== False:
                ubicacionP1Y -= 2
                ubicacionP1 -= 1
            if caerMovi == True:
                ubicacionP1Y += 2
                ubicacionP1 -= 1
            if ubicacionP1Y == 170:
                caerMovi= True
            if ubicacionP1Y == 280:
                caerMovi = False
                saltarMovi= False
                    
        
        pygame.display.flip()#actualiza la pantalla

        
        for eventos in pygame.event.get():# determina si el usuario dio presiona salir y cierra el juego
            if eventos.type == QUIT:
                pygame.quit()
                sys.exit()

##bucle_juego()




