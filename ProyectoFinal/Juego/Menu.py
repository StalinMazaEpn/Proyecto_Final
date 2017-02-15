import pygame,sysimport pygame,sys
from Clases import Cursor,Boton
from Survival import bucle_juego

##VARIABLES GLOBALES
largoV = 756
anchoV = 945
blanco= (255,255,255)
Puntajes =[] 
seleccion = 0
nomPersonaje = ''
personajeSelec = False

imagen1 = pygame.image.load("botones/botton1.png")
imagen2 = pygame.image.load("botones/botton1.1.png")
imagen3 = pygame.image.load("botones/botton2.png")
imagen4 = pygame.image.load("botones/botton2.1.png")
imagen5 = pygame.image.load("botones/botton3.png")
imagen6 = pygame.image.load("botones/botton3.1.png")
imagen7 = pygame.image.load("botones/botton4.png")
imagen8 = pygame.image.load("botones/botton4.1.png")
imagen9 = pygame.image.load("botones/mario.png")
imagen10 = pygame.image.load("botones/mario1.png")
imagen11 = pygame.image.load("botones/personaje.png")
imagen12 = pygame.image.load("botones/personaje1.png")


def opciones(opcion,fuente,ventana):
    global personajeSelec,nomPersonaje
    mensaje = ''
    posx,posy = 0,0
    if opcion ==1:
        if personajeSelec == True:
            bucle_juego(nomPersonaje)
            personajeSelec = False
            main()
        else:
            mensaje = 'Seleccione un personaje'
            posx,posy = 450,450
    elif opcion ==2:
        mensaje = 'Personajes'
        posx,posy =500,280
    elif opcion ==3:
        mensaje = 'Records'
        posx,posy =535,280
        record(fuente,ventana)
    return mensaje,posx,posy

def personaje(opcion,nombre,boton1,boton2,ventana,cursor,fuente):
    global personajeSelec
    if opcion == 2:
        boton1.update(ventana,cursor)
        boton2.update(ventana,cursor)
        mensaje = "No has escogido ningun personaje"
        if personajeSelec == True:
            mensaje = "Seleccionastes: "+nombre
        nombreP = fuente.render(mensaje,0,blanco)
        ventana.blit(nombreP,(380,600))

def record(fuente,ventana):
    global Puntajes
    contador  = len(Puntajes)-5
    if contador < 0:
        contador = 0
    texto  = ""
    ultimos5 = Puntajes[contador:len(Puntajes)]
    for i in range(len(ultimos5)):
        texto1 = 'Record'+' '+str(contador+1)+'      '+str(ultimos5[i])
        texto2 = fuente.render(texto1,1,blanco)
        contador += 1
        ventana.blit(texto2,(450,50*i+350))
    contador = 0

    
def lecturaP(texto):
    try:
        global Puntajes
        archivo = open(texto,'r')
        linea = archivo.readline()
        while linea != '':
            eliminar = linea.replace("\n","")
            Puntajes.append(eliminar)
            linea = archivo.readline()
        archivo = open(texto,'w')
        archivo.close()
    except FileNotFoundError:
        archivo = open(texto,'w')
        archivo.close()
    

def lecturaR(nombre):
    global Puntajes
    try:
        archivo = open(nombre+'.txt','r')
        linea = archivo.readline()
        while linea != '':
            eliminar = linea.replace("\n","")
            Puntajes.append(eliminar)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        archivo = open(nombre+'.txt','w')
        archivo.close()
        
def escrituraP(lista,nombre):
    archivo = open(nombre+'.txt','w')
    for i in range(len(lista)):
        archivo.write(str(lista[i])+'\n')
    archivo.close()

#mostrar esa ventana
def main():
    global seleccion,nomPersonaje,personajeSelec
    ## creacion, lectura y escritura del texo puntaje
    lecturaP('puntaje.txt')
    escrituraP(Puntajes,'records')
    pygame.init()#sentencia obligatoria
    ventana = pygame.display.set_mode((anchoV,largoV))#recibe una tupla
    pygame.display.set_caption("Menu")
    fondo = pygame.image.load("imagenes/fondo.jpg").convert()
    fondo = pygame.transform.scale(fondo,(anchoV,largoV))
    marco = pygame.image.load("botones/marco2.png")
    marco = pygame.transform.scale(marco,(500,450))
    cursor1 = Cursor()
    boton1 = Boton(imagen1,imagen2,100,265)
    boton2 = Boton(imagen3,imagen4,100,365)
    boton3 = Boton(imagen5,imagen6,100,465)
    boton4 = Boton(imagen7,imagen8,100,565)
    boton5 = Boton(imagen9,imagen10,560,360)
    boton6 = Boton(imagen11,imagen12,560,460)

    fuente1= pygame.font.SysFont("Arial", 23, True, False)
    pygame.mixer.music.load("audio/intro.mp3")
    pygame.mixer.music.play()
    while True:
        ventana.blit(fondo,(0,0))
        ventana.blit(marco,(330,235))
        
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccion = 1
                elif cursor1.colliderect(boton2.rect):
                    seleccion = 2
                elif cursor1.colliderect(boton3.rect):
                    seleccion = 3
                elif cursor1.colliderect(boton4.rect):
                    seleccion = 4
                    pygame.quit()
                    sys.exit()
                elif cursor1.colliderect(boton5.rect):
                    nomPersonaje = "Mario"
                    personajeSelec = True
                elif cursor1.colliderect(boton6.rect):
                    nomPersonaje = "Seiya"
                    personajeSelec = True
                    
            if evento.type == pygame.QUIT:
                pygame.quit()#detenemos todos los modulos
                sys.exit()
                
        mensaje,posx,posy = opciones(seleccion,fuente1,ventana)
        texto =  fuente1.render(mensaje,1,blanco)
        personaje(seleccion,nomPersonaje,boton5,boton6,ventana,cursor1,fuente1)
        cursor1.update()
        boton1.update(ventana,cursor1)
        boton2.update(ventana,cursor1)
        boton3.update(ventana,cursor1)
        boton4.update(ventana,cursor1)
        ventana.blit(texto,(posx,posy))
        pygame.display.update()
        
lecturaR('records')
main()
