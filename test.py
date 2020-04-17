from board import Board

board = Board(8, 6)

board.random_populate()
board.print()
print("starting the game...")
for x in range(10):
    board.generation()
    board.print()
