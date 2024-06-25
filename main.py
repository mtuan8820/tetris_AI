import pygame, sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python tetris")

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == pygame.KEYDOWN:

            if game.game_over == False:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down() 
                elif event.key == pygame.K_UP:
                    game.rotate()
            if game.game_over == True:
                game.reset()
    
        if event.type == GAME_UPDATE and game.game_over==False:
            game.move_down()

    #Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)