from environment.board import Board

key_to_action = {
    'w': 'UP',
    's': 'DOWN',
    'a': 'LEFT',
    'd': 'RIGHT'
}

board = Board(size=10)
board.reset()
while not board.go_flag:
    board.print_board()
    key = input("Movimiento (w=arriba s=abajo a=izq d=der): ")

    if key not in key_to_action:
        print("Tecla inválida")
        continue

    action = key_to_action[key]
    board.move(action)
print("GAME OVER!")
board.print_board()
