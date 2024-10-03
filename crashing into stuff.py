import pygame
import os
import random
from time import sleep

A= "fallingobj"
b = 1
list =[]
list_rect = []
list_spy = []
list_spx = []
class Settings:
    WINDOW = pygame.rect.Rect(0, 0, 600, 400)
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")


class Barrier (pygame.sprite.Sprite):
       def __init__(self,pos_x,pos_y,width,height):
           self.pos_x  = pos_x
           self.pos_y  = pos_y
           self.width  = width
           self.height = height
           super().__init__()
           self.barrier_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "barrier01.png")).convert()
           self.barrier_image.set_colorkey("black")
           self.barrier_image = pygame.transform.scale(self.barrier_image, (self.width, self.height))
           self.barrier_rect = self.barrier_image.get_rect()
           self.barrier_rect.topleft = (self.pos_x, self.pos_y)


class fallingobjt  (pygame.sprite.Sprite):
    def __init__(self,speed_x,speed_y):
      self.speed_x =speed_x
      self.speed_y =speed_y
      self.pos_y   = 20
      self.pos_y   = 20
      self.direction_x = 1
      self.direction_y = -1
      A = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "fall1.png")).convert()
      A.set_colorkey("black")
      A  = pygame.transform.scale(A, (50, 45))
      self.A_rect = A.get_rect()
      self.A_rect .topleft = (10, 10)
    
    def update(self):
        self.rect = self.rect.move(self.speed_x * self.direction_x, self.speed_y * self.direction_y)
        if self.rect.left < 0 or self.rect.right > Settings.WINDOW.right:
            self.direction_x *= -1
        if self.rect.top < 0 or self.rect.bottom > Settings.WINDOW.bottom:
            self.direction_y *= -1
        if self.A_rect.colliderect(self.barrier1.rect):
           self.pos_y = 10000
           self.pos_x = 10000
           self.speed_x = 0
           self.speed_y = 0
        if self.A_rect.colliderect(self.barrier2.rect):
           self.pos_y = 10000
           self.pos_x = 10000
           self.speed_x = 0
           self.speed_y = 0
        if self.A_rect.colliderect(self.barrier3.rect):
           self.pos_y = 10000
           self.pos_x = 10000
           self.speed_x = 0
           self.speed_y = 0
        if self.A_rect.colliderect(self.barrier4.rect):
           self.pos_y = 10000
           self.pos_x = 10000
           self.speed_x = 0
           self.speed_y = 0
        if self.A_rect.colliderect(self.barrier5.rect):
           self.pos_y = 10000
           self.pos_x = 10000
           self.speed_x = 0
           self.speed_y = 0
           
class Game:
        def __init__(self) -> None:
               os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
               pygame.init()     
            
               self.surface = pygame.display.set_mode(Settings.WINDOW.size)
               pygame.display.set_caption("crash into stuff")
               self.clock = pygame.time.Clock()


               self.barrier1 = Barrier (180,100,50,40)
               self.barrier2 = Barrier (300,45,75,35)
               self.barrier3 = Barrier (220,200,90,78)
               self.barrier4 = Barrier (200,250,50,40)
               self.barrier5 = Barrier (360,89,60,250)

               self.clock = pygame.time.Clock()
               self.all_sprites = pygame.sprite.Group()
               self.all_sprites.add(self.barrier1)
               self.all_sprites.add(self.barrier2)
               self.all_sprites.add(self.barrier3)
               self.all_sprites.add(self.barrier4)
               self.all_sprites.add(self.barrier5)
               self.hinter_image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "hinter1.png")).convert()
               self.hinter_image = pygame.transform.scale(self.hinter_image, (600, 400))
               self.running = True
        def run (self):

            C = newfallingobj ()

            while self.running:
            # Event-Handling
             self.watch_for_events()

            # Spiellogik
             self.update()

            # Objekte zeichnen
             self.draw()

             self.clock.tick(Settings.FPS)

             C.create_new_object
            pygame.quit()
             
            
        def draw(self):
         self.surface.blit(self.hinter_image, (0, 0))
         self.all_sprites.draw(self.surface)
         pygame.display.flip()

        def watch_for_events(self):
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        def update(self):
         self.all_sprites.update()

class newfallingobj ():
    def __init__(self):
        self.A = "fallingobj"
        self.b = 1
    def create_new_object (self):
        bnumber = str(self.b)
        self.b +1  
        A = self.A+bnumber
        self.speed_x    = random.randint (1,9)
        self.speed_y    = random.randint (1,9)
        A = fallingobjt(self.speed_x,self.speed_x)
        Game.all_sprites.add(A)


        
       
def main ():
    game = Game()
    game.run()


    


if __name__ == "__main__":
  main()
