import pygame

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagenNormal = imagen1
        self.imagenSeleccion = imagen2
        self.imagenActual= self.imagenNormal
        self.sonido = pygame.mixer.Sound("audio/laser.ogg")
        self.continuar = True
        self.x=0
        self.y=0
        self.rect = self.imagenActual.get_rect()
        self.rect.left,self.rect.top = (x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):#si el cursor choca con nuestro rectangulo
            self.imagenActual = self.imagenSeleccion
            if self.continuar:
                self.sonido.play()
                self.continuar = False
     
        else:
            self.imagenActual = self.imagenNormal
            self.continuar = True
            

        pantalla.blit(self.imagenActual,self.rect)
