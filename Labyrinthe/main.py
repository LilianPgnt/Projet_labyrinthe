import pygame
from game import Game
from player import Player
from monster import Monster


pygame.init()

pygame.display.set_caption("Projet Jeu Labyrinthe Lilian POIGNANT L3 MN");
screen = pygame.display.set_mode((1080, 720))


background = pygame.image.load('images/fond.jpg')
decor = pygame.image.load('images/block.png') ###################
drapeau = pygame.image.load('images/drapeau.png')
tache_boue = pygame.image.load('images/boue.png')
tache_eau = pygame.image.load('images/eau.png')
running = True

#charger notre jeu
game = Game()


#charger notre personnage
player = Player()
#tant que running est vrai la fenetre reste ouverte

while running:
    #arriere plan jeu

    pygame.display.flip()
    screen.blit(background, (0, 0))
    #------------------------------------------
    screen.blit(tache_eau, (590, 80))
    screen.blit(tache_eau, (480, 500))
    screen.blit(tache_eau, (1000, 475))
    #-------------------------------------------
    screen.blit(tache_boue, (500, 300))
    screen.blit(tache_boue, (135, 465))
    screen.blit(tache_boue, (100, 190))
    #-------------------------------------------
    screen.blit(drapeau, (1000, 615))
    # -------------------------------------------
    screen.blit(decor, (60, 0))
    screen.blit(decor, (60, 38))
    screen.blit(decor, (60, 76))
    screen.blit(decor, (90, 76))
    screen.blit(decor, (120, 76))##########
    screen.blit(decor, (90, 0))############ 1
    screen.blit(decor, (120, 0))###########
    screen.blit(decor, (150, 0))
    screen.blit(decor, (180, 0))
    screen.blit(decor, (150, 76))
    screen.blit(decor, (180, 76))
    screen.blit(decor, (180, 38))
    #--------------------------------------
    screen.blit(decor, (0, 190))
    screen.blit(decor, (0, 228))
    screen.blit(decor, (0, 266))
    screen.blit(decor, (0, 304))
    screen.blit(decor, (0, 342))
    screen.blit(decor, (0, 380))
    screen.blit(decor, (0, 418))########
    screen.blit(decor, (0, 456))######## 3
    screen.blit(decor, (0, 494))########
    screen.blit(decor, (30, 190))
    screen.blit(decor, (30, 228))
    screen.blit(decor, (30, 266))
    screen.blit(decor, (30, 304))
    screen.blit(decor, (30, 342))
    screen.blit(decor, (30, 380))
    screen.blit(decor, (30, 418))
    screen.blit(decor, (30, 456))
    screen.blit(decor, (30, 494))
    #---------------------------------
    screen.blit(decor, (60, 380))
    screen.blit(decor, (90, 380))
    screen.blit(decor, (120, 380))
    screen.blit(decor, (150, 380))
    screen.blit(decor, (180, 380))

    screen.blit(decor, (180, 342))
    screen.blit(decor, (180, 304))
    screen.blit(decor, (180, 266))
    screen.blit(decor, (180, 228))

    screen.blit(decor, (270, 0))
    screen.blit(decor, (270, 38))
    screen.blit(decor, (270, 76))

    #---------------------------------

    screen.blit(decor, (60, 589))
    screen.blit(decor, (90, 589))
    screen.blit(decor, (120, 589))
    screen.blit(decor, (150, 589))
    screen.blit(decor, (180, 589))

    #---------------------------------

    screen.blit(decor, (1020, 152))
    screen.blit(decor, (1020, 190))
    screen.blit(decor, (1020, 228))
    screen.blit(decor, (1020, 266))
    screen.blit(decor, (1020, 304))
    screen.blit(decor, (1020, 342))
    screen.blit(decor, (1020, 380))
    screen.blit(decor, (1020, 418))
    screen.blit(decor, (1050, 418))

    #--------------------------------
    screen.blit(decor, (720, 0))
    screen.blit(decor, (750, 0))
    screen.blit(decor, (780, 0))
    screen.blit(decor, (810, 0))
    screen.blit(decor, (840, 0))
    screen.blit(decor, (870, 0))

    screen.blit(decor, (720, 38))
    screen.blit(decor, (750, 38))
    screen.blit(decor, (780, 38))
    screen.blit(decor, (810, 38))
    screen.blit(decor, (840, 38))
    screen.blit(decor, (870, 38))

    #-------------------------------
    screen.blit(decor, (420, 76))
    screen.blit(decor, (450, 76))
    screen.blit(decor, (480, 76))
    screen.blit(decor, (510, 76))
    screen.blit(decor, (540, 76))
    screen.blit(decor, (570, 76))

    screen.blit(decor, (420, 114))
    screen.blit(decor, (450, 114))
    screen.blit(decor, (480, 114))
    screen.blit(decor, (510, 114))
    screen.blit(decor, (540, 114))
    screen.blit(decor, (570, 114))

    screen.blit(decor, (600, 152))
    screen.blit(decor, (600, 190))
    screen.blit(decor, (600, 228))
    screen.blit(decor, (600, 266))
    screen.blit(decor, (600, 304))
    screen.blit(decor, (600, 342))
    screen.blit(decor, (600, 380))
    screen.blit(decor, (600, 418))
    screen.blit(decor, (600, 456))

    screen.blit(decor, (630, 152))
    screen.blit(decor, (630, 190))
    screen.blit(decor, (630, 228))
    screen.blit(decor, (630, 266))
    screen.blit(decor, (630, 304))
    screen.blit(decor, (630, 342))
    screen.blit(decor, (630, 380))
    screen.blit(decor, (630, 418))
    screen.blit(decor, (630, 456))

    #------------------------------

    screen.blit(decor, (330, 228))
    screen.blit(decor, (360, 228))

    screen.blit(decor, (300,570))
    screen.blit(decor, (300,608))
    screen.blit(decor, (300,646))
    screen.blit(decor, (300,684))

    screen.blit(decor, (330,608))
    screen.blit(decor, (330,646))
    screen.blit(decor, (330,684))

    #------------------------------

    screen.blit(decor, (390,456))
    screen.blit(decor, (420,456))
    screen.blit(decor, (450,456))
    screen.blit(decor, (480,456))
    screen.blit(decor, (510,456))
    screen.blit(decor, (540,456))
    screen.blit(decor, (570,456))

    screen.blit(decor, (390,304))
    screen.blit(decor, (390,342))
    screen.blit(decor, (390,380))
    screen.blit(decor, (390,418))

    screen.blit(decor, (420,304))
    screen.blit(decor, (450,304))

    screen.blit(decor, (570,494))
    screen.blit(decor, (570,532))
    screen.blit(decor, (570,570))

#----------------------------------

    screen.blit(decor, (750,152))
    screen.blit(decor, (840,152))
    screen.blit(decor, (870,152))
    screen.blit(decor, (900,152))

    screen.blit(decor, (750,190))
    screen.blit(decor, (780,190))
    screen.blit(decor, (810,190))
    screen.blit(decor, (840,190))
    screen.blit(decor, (870,190))
    screen.blit(decor, (900,190))

    #-----------------------------
    screen.blit(decor, (780,228))
    screen.blit(decor, (780, 266))
    screen.blit(decor, (780, 304))

    screen.blit(decor, (810, 342))
    screen.blit(decor, (810, 380))
    screen.blit(decor, (810, 418))
    screen.blit(decor, (810, 456))
    screen.blit(decor, (810, 494))

    screen.blit(decor, (930, 342))
    screen.blit(decor, (960, 342))
    screen.blit(decor, (990, 342))

    screen.blit(decor, (750,494))
    screen.blit(decor, (750,532))
    screen.blit(decor, (750,570))
    screen.blit(decor, (750,608))
    screen.blit(decor, (750,646))
    screen.blit(decor, (750,684))

    screen.blit(decor, (780,494))

    screen.blit(decor, (780, 570))
    screen.blit(decor, (810, 570))
    screen.blit(decor, (840, 570))

    screen.blit(decor, (840, 608))
    screen.blit(decor, (840, 646))
    screen.blit(decor, (840, 684))

    #-------------------------------

    screen.blit(decor, (300, 0))
    screen.blit(decor, (330, 0))

    screen.blit(decor, (300, 190))
    screen.blit(decor, (300, 266))
    screen.blit(decor, (360, 266))

    screen.blit(decor, (270, 418))
    screen.blit(decor, (270, 380))
    screen.blit(decor, (240, 532))
    screen.blit(decor, (270, 532))

    screen.blit(decor, (360, 646))
    screen.blit(decor, (360, 684))
    screen.blit(decor, (390, 684))
    screen.blit(decor, (420, 684))

    screen.blit(decor, (690, 646))
    screen.blit(decor, (720, 646))
    screen.blit(decor, (630, 684))
    screen.blit(decor, (660, 684))
    screen.blit(decor, (690, 684))
    screen.blit(decor, (720, 684))

    screen.blit(decor, (840, 494))
    screen.blit(decor, (870, 494))
    screen.blit(decor, (900, 494))

    screen.blit(decor, (990, 570))
    screen.blit(decor, (1020, 570))
    screen.blit(decor, (1050, 570))

    screen.blit(decor, (870, 646))
    screen.blit(decor, (900, 646))








    #image du joueur
    screen.blit(game.player.image, game.player.rect)

    #recupérer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward

     #affichage des monstrers
        game.all_monsters.draw(screen)

    #verifier su le joueur veut aller a gauche ou a droite et haut bas
    if game.pressed.get(pygame.K_RIGHT): #and game.player.rect.x < 1080:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT): #and game.player.rect.x > 0:
          game.player.move_left()
    elif game.pressed.get(pygame.K_DOWN): #and game.player.rect.y < 720:
        game.player.move_up()
    elif game.pressed.get(pygame.K_UP):# and game.player.rect.y > 0:
        game.player.move_down()



    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #decter si un joueur lache un touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
