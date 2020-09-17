import pygame

from board import Board

pygame.init()

screen = pygame.display.set_mode([1800, 1300])
pygame.display.set_caption("Game of Life")

screen.fill((155, 155, 155))
clock = pygame.time.Clock()

board = Board(130, 90)
board.random_populate(50)

running = True
generation = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw(screen)
    board.generation()
    pygame.display.flip()
    pygame.display.set_caption(f"Game of Life | generation {generation}")
    # clock.tick(1)
    generation +=1 
pygame.quit()
