import pygame
 
# Definimos algunos colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
 
# Inicializamos
pygame.init()
 
# Creamos una pantalla de 800x600.
pantalla = pygame.display.set_mode([1500, 900])
 
# Establecemos el nombre de la ventana.
pygame.display.set_caption('CMSC 150 es divertido')
 
reloj = pygame.time.Clock()
 
# Antes del bucle cargamos el sonido:
sonido_click = pygame.mixer.Sound("0945.ogg")
 
# Establecemos la posición de los gráficos
posicion_base = [0, 0]
 
# Carga y sitúa los gráficos.
imagen_de_fondo = pygame.image.load("fondo1.png").convert()
imagen_personaje = pygame.image.load("mario4.png").convert()
imagen_personaje.set_colorkey(NEGRO)
 
hecho = False
 
while not hecho:
    reloj.tick(100)
     
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("============")
            sonido_click.play() 
             
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, posicion_base)
 
    # Obtiene la posición actual del ratón. Devuelve ésta como
    # una lista de dos números.
    posicion_del_personaje = pygame.mouse.get_pos()
    x = posicion_del_personaje[0]
    y = posicion_del_personaje[1]
     
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_personaje, [x, y])
     
    pygame.display.flip()
    reloj.tick(100)
 
pygame.quit()
