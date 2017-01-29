import sys
import pygame
import random
from pygame.locals import *



#colores
azul = (100,0,250)
amarillo =(250,250,0)
rojo = (250,0,0)
morado = (150,0,150)
rosa = (250,100,250)
negro = (0,0,0)
verde =(20,130,20)
cafe = (150,100,50)
reloj = pygame.time.Clock()

anchoPantalla = 900
altoPantalla = 380
ubicacionP1=250 # ubicacion del personaje 1 en el eje X
ubicacionP1Y=280 # ubicacion del personaje 1 en el eje Y

cont=9  # contador que aumentara en el bucle principal para la velocidad de los sprites
direccionP1= True
i=0

NaveD = True
posicionDer= {} #comienza y  finaliza cada sprite del personaje
posicionIzq={}#comienza y  finaliza cada sprite del personaje de manera inversa
saltar= False # determina si salta el personaje o esta en el suelo
saltarMovi=False# determina si el personaje salto al presionar tecla derecha o izquierda

class Nave(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen 
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

class Personaje(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen 
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)


class Disparo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen 
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left
    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)  
        
    
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
    if teclado[K_SPACE] and teclado[K_RIGHT] == True and saltarMovi == False:
        saltarMovi = True

    #lo mismo del if anterior pero con la tecla izquierda y salto sera hacia atras
    elif teclado[K_SPACE] and teclado[K_LEFT]== True  and saltarMovi == False:
        saltarMovi = True

    # si presiono tecla derecha y las variables de saltar son falsas
    #significara que el personaje solo caminara
    elif teclado[K_RIGHT] and saltar== False and saltarMovi==False:
        ubicacionP1 +=2
        cont+=1
        direccionP1=True
    # lo mismo del if anterior pero con la tecla izquierda
    elif teclado[K_LEFT] and saltar == False and saltarMovi==False:
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
    salir = False
    pygame.init()# inicializa pygame
    sonido1 = pygame.mixer.Sound("sound1.wav")

    listaR = []
    for x in range(15):
        #w = random.randrange(20,30)
        (w,h) = (50,15)
        #h = random.randrange(20,25)
        x = random.randrange(anchoPantalla)
        y = random.randrange(altoPantalla-100)
        listaR.append(pygame.Rect(x,y,w,h))
        

    screen = pygame.display.set_mode((anchoPantalla, altoPantalla))#ancho y alto de pantalla
    pygame.display.set_caption("SURVIVAL")#titulo  a la ventana
    fondo = pygame.image.load('fondo1.jpg').convert()# fondo para la pantalla
    personaje1= pygame.image.load('personaje1.png').convert()#sprites personaje1    
    color= personaje1.get_at((0,0))# color transparente   
    personaje1.set_colorkey(color,RLEACCEL)#hace transparente el fondo del sprite del personaje
    personaje1_inv= pygame.transform.flip(personaje1,True,False);#Invierte el sprite,TRUE invierte la imagen al eje X, y FLASE quiere invertir de arriba poara abajo
 
    #-----------------------NAVE Y DISPARO    
    imgN=pygame.image.load("nave2.png").convert_alpha()
    nave1=Nave(imgN)
    disparoActivo = False
    imgD=pygame.image.load("disparo.png").convert_alpha()
    disparo1=Disparo(imgD)
    personajeVisible = True    
    #-------------------------------------------------------------------
    
        
    clock = pygame.time.Clock()# tiempo en de los fotogramas
    global saltarMovi
    caer= False # define si el personaje cae solo verticalmente
    caerMovi=False# define si el personaje cae hacia adelante o hacia atras
    #nave1.mover(2,10) #tamaño pantalla es 900*380 ancho-alto
    
    #BUCLE PRINCIPAL DEL JUEGO
    while salir != True:
    
        time= clock.tick(80)
        movimiento_Personaje1()
        movimiento_teclado_P1()
        fondo= pygame.transform.scale(fondo,(1000,400)) #Agranda o Achica la imagen segun las dimensiones que se de
        screen.blit(fondo,(0,0))#dibuja la imagen
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
        #-----------MOVER NAVE Y DISPARO------------------
        if   not disparoActivo:         # Nuevo en 0.05
            disparoActivo = True                        # Nuevo en 0.05
            disparo1.rect.left = nave1.rect.left + 18  # Nuevo en 0.05
            disparo1.rect.bottom = nave1.rect.bottom - 10

        nave1.rect.left += 3   
        if  nave1.rect.right > anchoPantalla:
            nave1.rect.left = 0

        if disparoActivo:                      # Nuevo en 0.05
            disparo1.rect.bottom += 4        # Nuevo en 0.05
            b = disparo1.rect.bottom
            c = disparo1.rect.bottom            
            if b <= 0:     # Nuevo en 0.05
                disparoActivo = False                
            if c >altoPantalla:
                disparoActivo = False 
        #------------------------------------  ----------------        
        sonido1.play()       
        for r in listaR:
            pygame.draw.rect(screen,azul,r)
        #------------------------mostrando disparo------------------
        if disparoActivo:
            disparo1.update(screen)        
        nave1.update(screen)
        #-----------------------------------------------------------
        for eventos in pygame.event.get():# determina si el usuario dio presiona salir y cierra el juego
            if eventos.type == QUIT:
                salir = True      
        pygame.display.flip()#actualiza la pantalla
        reloj.tick(40)
        
    pygame.quit()
    
bucle_juego()
