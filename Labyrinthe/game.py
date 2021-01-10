import pygame
from player import Player
from monster import Monster


# creer une  classe qui va représenter le jeu

class Game:
    def __init__(self):
        #générer le joueur
        self.player = Player()
        #  monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed ={}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)