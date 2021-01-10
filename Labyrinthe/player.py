import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 1 #vitesse du joueur
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect() #permet de recupérer la position de joueur
        self.rect.x = -25
        self.rect.y = -10

    def move_right(self):
        #si le joueur n'est pas en colision

        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y += self.velocity

    def move_down(self):
        self.rect.y -= self.velocity