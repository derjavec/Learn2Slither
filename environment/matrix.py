COLOR_RESET = "\033[0m"
COLOR_SNAKE = "\033[34m"
COLOR_GREEN_APPLE = "\033[32m"
COLOR_RED_APPLE = "\033[31m"

def update_matrix(self):
    matrix = []
    for y in range(self.size):
        row = []
        for x in range(self.size):
            if (x, y) in self.snake_pos:
                row.append('S')
            elif (x, y) in self.green_apples:
                row.append('G')
            elif (x, y) in self.red_apples:
                row.append('R')
            else:
                row.append('0')
        matrix.append(row)
    self.matrix = matrix


def print_board(self):
    for row in self.matrix:
        line = ""
        for cell in row:
            if cell == 'S':
                line += f"{COLOR_SNAKE}S{COLOR_RESET} "
            elif cell == 'G':
                line += f"{COLOR_GREEN_APPLE}G{COLOR_RESET} "
            elif cell == 'R':
                line += f"{COLOR_RED_APPLE}R{COLOR_RESET} "
            else:
                line += "0 "
        print(line)