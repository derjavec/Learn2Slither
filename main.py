from environment.board import Board

def main():

    game_board = Board()
    init_snake_pos = game_board.reset()
    game_board.print_board()
    game_board.move('RIGHT')
    print('----')
    game_board.print_board()
    game_board.move('RIGHT')
    print('----')
    game_board.print_board()




if __name__ == '__main__':
    main()