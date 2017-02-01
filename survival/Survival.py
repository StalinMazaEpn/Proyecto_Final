import sys
import pygame
import random
from pygame.locals import *

#--------------colores
azul = (100,0,250)
amarillo =(250,250,0)
rojo = (250,0,0)
morado = (150,0,150)
rosa = (250,100,250)
negro = (0,0,0)
verde =(14,102,85) #14, 102, 85   (20,130,20)
cafe = (150,100,50)
reloj = pygame.time.Clock()
#--------------------------------

anchoPantalla = 900
altoPantalla = 380
ubicacionP1=250 # ubicacion del personaje 1 en el eje X
ubicacionP1Y=280 # ubicacion del personaje 1 en el eje Y

ubicacionP2=250 # ubicacion del personaje 2 en el eje X
ubicacionP2Y=180 # ubicacion del personaje 2 en el eje Y

direccionP1= True

direccionP2= True
i=0

NaveD = True
posicionDer= {} #comienza y  finaliza cada sprite del personaje
posicionIzq={}#comienza y  finaliza cada sprite del personaje de manera inversa
saltar= False # determina si salta el personaje o esta en el suelo
#saltarMovi=False# determina si el personaje salto al presionar tecla derecha o izquierda



def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error.message:
                raise SystemExit.message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

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


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]        
        for x in range(numeroinicial):
            #creo un rect random
            leftrandom=  random.randrange(anchoPantalla-100)
            toprandom= random.randrange(50,altoPantalla-120)
            width= 60
            height= 15
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))            
    def pos(self,i):
        return self.lista[i]
    def reagrear(self):
        pass
    def agregarotro(self):
        pass
    def mover(self,x,y):
        for rectangulo in self.lista:
            rectangulo.move_ip(x,y)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,verde,rectangulo)        


def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False
   
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
 
def movimiento_Personaje2():
    global cont2  
    contCambiar=5
    global i
    posicionDer[0]=(0,0,91,175)#posicion de cada sprite x,y, ancho, alto
    posicionDer[1]=(90,0,95,175)
    posicionDer[2]=(180,0,92,175)
    posicionDer[3]=(270,0,94,175)
    posicionDer[4]=(3600,0,95,175)
   
    posicionIzq[0]=(405,0,91,175)
    posicionIzq[1]=(311,0,94,175)
    posicionIzq[2]=(219,0,90,175)
    posicionIzq[3]=(195,0,92,175)
    posicionIzq[4]=(89,0,89,175)
    
    # se va multiplicando contador cambiar, cada que es igual al cont del personaje
     #para ir cambiando de sprites
    if cont2==contCambiar:
        i=0
        
    if cont2==contCambiar*1:
        i=1
    if cont2==contCambiar*2:
        i=2
    if cont2==contCambiar*3:
        i=3
    if cont2==contCambiar*4:
        i=4
        cont2=0


def movimiento_teclado_P1():
    teclado = pygame.key.get_pressed()    

    global ubicacionP1
    global i
    global cont, direccionP1, saltar, saltarMovi,i

    if teclado[K_UP]:
            saltar=True
    if teclado[K_RIGHT] and ubicacionP1<=860: # ubicacionp1 <=860 detecta colision en pared derecha
            ubicacionP1+=2
            cont+=1
            direccionP1=True
    elif teclado[K_LEFT] and ubicacionP1>=3:
            ubicacionP1-=2
            cont+=1
            direccionP1=False            
    else :
         cont=9

#movimiento del personaje 2
def movimiento_teclado_P2():
    teclado = pygame.key.get_pressed()    

    global ubicacionP2
    global i
    global cont2, direccionP1, saltar, saltarMovi,i
    
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
        ubicacionP2 +=2
        cont2+=1
        direccionP2=True
    # lo mismo del if anterior pero con la tecla izquierda
    elif teclado[K_LEFT] and saltar == False and saltarMovi==False:
        ubicacionP2-=2
        cont2+=1
        direccionP2=False
        
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
    #sonido1 = pygame.mixer.Sound("audio/sound1.wav")

    screen = pygame.display.set_mode((anchoPantalla, altoPantalla))#ancho y alto de pantalla
    pygame.display.set_caption("SURVIVAL")#titulo  a la ventana
    fondo = imagen('imagenes/fondo1.jpg')# fondo para la pantalla
    personaje1= imagen('imagenes/personaje1.png',True)#sprites personaje1
    personaje1_inv= pygame.transform.flip(personaje1,True,False);
    #Invierte el sprite,TRUE invierte la imagen al eje X, y
    #FLASE quiere invertir de arriba poara abajo
    ##personaje2= imagen('imagenes/personaje2.png',True)#sprites personaje1
    ##personaje2_inv= pygame.transform.flip(personaje2,True,False);  
  
    bloque = pygame.image.load('imagenes/Bloque.png')
    #-----------------------NAVE Y DISPARO    
    imgN=pygame.image.load("imagenes/nave.png").convert_alpha()
    nave1=Nave(imgN)
    disparoActivo = False
    imgD=pygame.image.load("imagenes/disparo.png").convert_alpha()
    disparo1=Disparo(imgD)
    personajeVisible = True    
    #--------CONTADOR----------------------------------------------
    fuente1= pygame.font.SysFont("Arial", 25, True, False)
    info0=fuente1.render("Game is running..",0,(255,255,255))
    relojC= pygame.time.Clock()
    segundosint=0    
    #recs1=Recs(15) #num de rectangulos a graficar
    #------------------------------------    
    clock = pygame.time.Clock()# tiempo en de los fotogramas
    caer= False # define si el personaje cae solo verticalmente
    
    global saltarMovi
    caer= False # define si el personaje cae solo verticalmente
    caerMovi=False# define si el personaje cae hacia adelante o hacia atras
    #nave1.mover(2,10) #tamaño pantalla es 900*380 ancho-alto
    pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    
    
    #BUCLE PRINCIPAL DEL JUEGO
    while salir != True:
    
        time= clock.tick(80)
        movimiento_Personaje1()
        movimiento_teclado_P1()
        fondo= pygame.transform.scale(fondo,(1000,400)) #Agranda o Achica la imagen segun las dimensiones que se de
        screen.blit(fondo,(0,0))#dibuja la imagen

        #Posiciones de los bloque en la ventana
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
        if direccionP1== True and saltar == False:
            #si se presiona la tecla derecha imprimira sprites normales
            screen.blit(personaje1,(ubicacionP1, ubicacionP1Y),(posicionDer[i]))
        if direccionP1 == False and saltar== False:
            # si se presiona izquierda imprimira sprites ivertidos
            screen.blit(personaje1_inv,(ubicacionP1, ubicacionP1Y),(posicionIzq[i]))
        
        #SALTO MEJORADO VERTICAL Y CON MOVIMIENTO DEL PERSONAJE 1
        if saltar==True:
            if direccionP1==True:
                screen.blit(personaje1, ( ubicacionP1, ubicacionP1Y),(posicionDer[6]))
            if direccionP1==False:
                screen.blit(personaje1_inv,(ubicacionP1, ubicacionP1Y),(posicionIzq[6]))
            if caer==False:
                ubicacionP1Y-=4
            if caer==True:
                ubicacionP1Y+=4
            if ubicacionP1Y <= 186:
                caer=True
            if ubicacionP1Y >= 280:
                caer=False
                saltar=False

        #-----------MOVER NAVE Y DISPARO------------------
        if   not disparoActivo:         # Nuevo en 0.05
            disparoActivo = True                        # Nuevo en 0.05
            disparo1.rect.left = nave1.rect.left + 18  # Nuevo en 0.05
            disparo1.rect.bottom = nave1.rect.bottom - 10

        nave1.rect.left += 3   
        if  nave1.rect.right > anchoPantalla:
            nave1.rect.left = 0

        if disparoActivo:                      # Nuevo en 0.05
            disparo1.rect.bottom += 5        # Nuevo en 0.05
            b = disparo1.rect.bottom
            c = disparo1.rect.bottom            
            if b <= 0:     # Nuevo en 0.05
                disparoActivo = False                
            if c >altoPantalla:
                disparoActivo = False
            #if  colision(disparo1,recs1):
             #   disparoActivo = False
            #if colision()
        #-------RECTANGULOS--------------------------------
        #recs1.pintar(screen)
        #------------------------mostrando disparo------------------
        if disparoActivo:
            disparo1.update(screen)        
        nave1.update(screen)
        #------------------CONTADOR--------------------------------------
        segundosint= pygame.time.get_ticks()/1000        
        normal = int(segundosint)        
        segundos= str(normal)
        contador=fuente1.render(segundos,0,(155,155,255))
        screen.blit(contador,(850,340))        
        #-------------------------------------------------------             
        #-------------------------------------------------------
        for eventos in pygame.event.get():# determina si el usuario dio presiona salir y cierra el juego
            if eventos.type == QUIT:
                salir = True
                pygame.quit()#detenemos todos los modulos
                sys.exit()
        pygame.display.flip()#actualiza la pantalla
        reloj.tick(50)
        
    pygame.quit()

##bucle_juego()
