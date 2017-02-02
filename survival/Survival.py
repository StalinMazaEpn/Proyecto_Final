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
#---------------------------------------------------------------------
LARGO_PANTALLA = 900
ALTO_PANTALLA = 600
#--------------------------------------CLASES----------------------------------------------------
class Nivel(object):
    #Esta es una súper clase genérica usada para definir un nivel.
    #Crea una clase hija específica para cada nivel con una info específica.        
    def __init__(self, protagonista):
        #Constructor. Requerido para cuando las plataformas móviles colisionan con el protagonista
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista

class Plataforma(pygame.sprite.Sprite):
    #Plataforma sobre la que el usuario puede saltar
    def __init__(self, largo, alto ):
        #Constructor de plataforma. Asume su construcción cuando el usuario le haya pasado 
        #un array de 5 números, tal como se ha definido al principio de este código.
        super().__init__()        
        self.image = pygame.image.load('imagenes/bloque.png').convert()  
        self.image = pygame.transform.scale(self.image,(50,50))        
        self.rect = self.image.get_rect()
        
class Nivel(object):
    #Esta es una súper clase genérica usada para definir un nivel.        
    def __init__(self, protagonista):
        #Constructor. Requerido para cuando las plataformas móviles colisionan con el protagonista.
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
        # Imagen de fondo
        self.imagende_fondo = None 
    # Actualizamos todo en este nivel
    def update(self):
        #Actualizamos todo en este nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()
    #def devolver(self,a):
     #   return self.listade_plataformas
    def draw(self, pantalla):
        # Dibujamos todas las listas de sprites que tengamos
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)

class Nivel_01(Nivel):
    #Definición para el nivel 1
    def __init__(self, protagonista):
        #Creamos el nivel 1        
        # llamamos al constructor padre
        Nivel.__init__(self, protagonista)        
        # Array con la información sobre el largo, alto, x, e y
        nivel = [ [210, 70, 500, 500],
                  [210, 70, 200, 400],
                  [210, 70, 600, 300],
                  [210, 70, 300, 500],
                  [210, 80, 375, 400]
                  ]
        # Iteramos sobre el array anterior y añadimos plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)

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

class Protagonista(pygame.sprite.Sprite): 
    #Esta clase representa la barra inferior que controla el protagonista  
    # -- Atributos 
    # Establecemos el vector velocidad del protagonista
    cambio_x = 0
    cambio_y = 0    
    # Lista de todos los sprites contra los que podemos botar
    nivel = None    
    # -- Métodos
    def __init__(self,imagen): 
        #Función Constructor        
        #  -- Llama al constructor padre 
        super().__init__()        
        # Crea una imagen del bloque y lo rellena con color rojo.
        # También podríamos usar una imagen guardada en disco	
        largo = 60
        alto = 60
        self.image = pygame.image.load(imagen).convert()
        color= self.image.get_at((0,0))
        self.image.set_colorkey(color,RLEACCEL)
        # Establecemos una referencia hacia la imagen rectangular
        self.rect = self.image.get_rect() 
      
    def update(self): 
        #Desplazamos al protagonista
        # Gravedad
        self.calc_grav()        
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x        
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y        
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
            # Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0
    def devolver(self):
        return self.nivel.listade_plataformas
    def calc_grav(self):
        #Calculamos el efecto de la gravedad 
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
        # Observamos si nos encontramos sobre el suelo. 
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height

    def saltar(self):
        #Llamado cuando el usuario pulsa el botón de 'saltar'        
        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien 
	# si solo descendemos uno).
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2        
        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
            self.cambio_y = -10
            
    # Movimiento controlado por el protagonista
    def ir_izquierda(self):
        #Es llamado cuando el usuario pulsa la flecha izquierda
        self.cambio_x = -6

    def ir_derecha(self):
        #Es llamado cuando el usuario pulsa la flecha derecha
        self.cambio_x = 6

    def stop(self):
        #Es llamado cuando el usuario abandona el teclado
        self.cambio_x = 0

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
            leftrandom=  random.randrange(LARGO_PANTALLA-100)
            toprandom= random.randrange(50,ALTO_PANTALLA-120)
            width= 60
            height= 15
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))            
    def pos(self,i):
        return self.lista[i]    
    def mover(self,x,y):
        for rectangulo in self.lista:
            rectangulo.move_ip(x,y)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,verde,rectangulo)        

def colision(player,rec):
    if player.rect.colliderect(rec):
        return True
    else:
        return False

def bucle_juego():
    salir = False
    pygame.init()# inicializa pygame 
    screen = pygame.display.set_mode((LARGO_PANTALLA, ALTO_PANTALLA))
    #ancho y alto de pantalla
    pygame.display.set_caption("SURVIVAL")#titulo  a la ventana
    fondo= pygame.image.load('imagenes/fondo1.jpg').convert() #fondo pantalla   
    #-----------------------NAVE Y DISPARO---------------------------------------   
    imgN=pygame.image.load("imagenes/nave.png").convert_alpha()
    nave1=Nave(imgN)
    disparoActivo = False
    imgD=pygame.image.load("imagenes/disparo.png").convert_alpha()
    disparo1=Disparo(imgD)
    #-----------------------CONTADOR----------------------------------------------
    fuente1= pygame.font.SysFont("Arial", 25, True, False)
    info0=fuente1.render("Game is running..",0,(255,255,255))
    relojC= pygame.time.Clock()
    segundosint=0 
    #-----------------------personaje----------------------------
    objeto = Protagonista("imagenes/p1.png")
    #------------------------------------------
    clock = pygame.time.Clock()# tiempo en de los fotogramas
    caer= False # define si el personaje cae solo verticalmente
    
    global saltarMovi
    caer= False # define si el personaje cae solo verticalmente
    caerMovi=False# define si el personaje cae hacia adelante o hacia atras
    #----------------------MUSICA-----------------------------
    pygame.mixer.music.load('audio/music.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    #-----------------------------------
     # Creamos al protagonista
    protagonista = Protagonista("imagenes/p1.png")
    # Creamos todos los niveles
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))    
    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
    lista_sprites_activos = pygame.sprite.Group()
    protagonista.nivel = nivel_actual    
    protagonista.rect.x = 340
    protagonista.rect.y = ALTO_PANTALLA - protagonista.rect.height
    lista_sprites_activos.add(protagonista)
    bloques_activos = protagonista.devolver() 
    #Iteramos hasta que el usuario pulse sobre el botón de salida 
    hecho = False
    # Lo usamos para gestionar cuan rápido se actualiza la pantalla.
    reloj = pygame.time.Clock() 
    #------------------------------
    #BUCLE PRINCIPAL DEL JUEGO
    while salir != True:
        screen.blit(fondo,(0,0))#dibuja la imagen
        time= clock.tick(80)
        fondo= pygame.transform.scale(fondo,(LARGO_PANTALLA,ALTO_PANTALLA))
        #Agranda o Achica la imagen segun las dimensiones que se de                            
        #-----------MOVER NAVE Y DISPARO------------------
        if   not disparoActivo:        
            disparoActivo = True                      
            disparo1.rect.left = nave1.rect.left + 18
            disparo1.rect.bottom = nave1.rect.bottom - 10

        nave1.rect.left += 3   
        if  nave1.rect.right > LARGO_PANTALLA:
            nave1.rect.left = 0        
        
        if disparoActivo:                    
            disparo1.rect.bottom += 5       
            b = disparo1.rect.bottom
            c = disparo1.rect.bottom            
            if b <= 0:  
                disparoActivo = False                
            if c >ALTO_PANTALLA:
                disparoActivo = False
            if  colision(disparo1,protagonista.rect):                
                disparoActivo = False
            if  pygame.sprite.spritecollideany(disparo1, bloques_activos, collided = None):                
                disparoActivo = False
        #------------------------mostrando disparo------------------
        if disparoActivo:
            disparo1.update(screen)        
        nave1.update(screen)
        #------------------CONTADOR--------------------------------------
        segundosint= pygame.time.get_ticks()/1000        
        normal = int(segundosint)        
        segundos= str(normal)
        contador=fuente1.render(segundos,0,(155,155,255))
        screen.blit(contador,(860,540))        
        #-------------------------------------------------------             
        #-------------------------------------------------------
        for eventos in pygame.event.get():# determina si el usuario dio presiona salir y cierra el juego
            if eventos.type == QUIT:
                salir = True
                pygame.quit()#detenemos todos los modulos
                sys.exit()
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if eventos.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if eventos.key == pygame.K_UP:
                    protagonista.saltar()
                    
            if eventos.type == pygame.KEYUP:
                if eventos.key == pygame.K_LEFT and protagonista.cambio_x < 0: 
                    protagonista.stop()
                if eventos.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()
        #----------------------------------------------------------
        # Actualizamos al protagonista. 
        lista_sprites_activos.update()        
        # Actualizamos los objetos en este nivel
        nivel_actual.update()
        # Si el protagonista se aproxima al lado derecho, desplazamos su mundo a la izquierda (-x)
        if protagonista.rect.right > LARGO_PANTALLA:
            protagonista.rect.right = LARGO_PANTALLA    
        # Si el protagonista se aproxima al lado izquierdo, desplazamos su mundo a la derecha (+x)
        if protagonista.rect.left < 0:
            protagonista.rect.left = 0            
        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO 
        nivel_actual.draw(screen)
        lista_sprites_activos.draw(screen)
        pygame.display.flip()#actualiza la pantalla
        reloj.tick(60)        
    pygame.quit()

#bucle_juego()
