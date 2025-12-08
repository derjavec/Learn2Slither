"""
Snake game visualizer using Pygame.
"""

import pygame
import sys


class Visualizer:
    def __init__(self, size: int, cell: int = 50):
        pygame.init()
        self.size = size
        self.cell = cell
        self.screen = pygame.display.set_mode((size * cell, size * cell + 40))
        pygame.display.set_caption("Snake Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.colors = {
            "background": (40, 40, 40),
            "snake": (0, 180, 255),
            "green_apple": (50, 205, 50),
            "red_apple": (255, 100, 100),
            "text": (200, 200, 200)
        }

    def draw(self, board, moves: int = 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill(self.colors["background"])

        points = [(x * self.cell + self.cell // 2, y * self.cell + self.cell // 2)
                  for x, y in board.snake_pos]
        if points:
            pygame.draw.lines(self.screen, self.colors["snake"], False, points, self.cell // 2)

        for gx, gy in board.green_apples:
            pygame.draw.circle(self.screen, self.colors["green_apple"],
                               (gx * self.cell + self.cell // 2, gy * self.cell + self.cell // 2),
                               self.cell // 3)

        for rx, ry in board.red_apples:
            pygame.draw.circle(self.screen, self.colors["red_apple"],
                               (rx * self.cell + self.cell // 2, ry * self.cell + self.cell // 2),
                               self.cell // 3)

        info_text = f"Moves: {moves} | Snake Length: {len(board.snake_pos)}"
        text_surface = self.font.render(info_text, True, self.colors["text"])
        self.screen.blit(text_surface, (10, self.size * self.cell + 10))

        pygame.display.flip()
        self.clock.tick(10)

    def wait_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
