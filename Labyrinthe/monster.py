import pygame

#classe qui gère les monstres

class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/monstre.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 10
        self.velocity = 2

    def forward(self):
        self.rect.x -= self.velocity