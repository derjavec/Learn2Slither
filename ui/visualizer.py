import pygame
import sys

class Visualizer:
    def __init__(self, size, cell=50):
        pygame.init()
        self.size = size
        self.cell = cell
        self.screen = pygame.display.set_mode((size * cell, size * cell + 40))  # espacio para texto
        pygame.display.set_caption("Snake Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)

        # Diccionario de colores
        self.colors = {
            "background": (40, 40, 40),     # gris oscuro
            "snake": (0, 180, 255),         # azul más vibrante
            "green_apple": (50, 205, 50),   # verde más llamativo
            "red_apple": (255, 100, 100),   # rojo más suave
            "text": (200, 200, 200)         # gris claro para texto
        }

    def draw(self, board, moves=0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fondo
        self.screen.fill(self.colors["background"])

        # Dibujar serpiente como círculos
        for x, y in board.snake_pos:
                        # Convertir posiciones de la serpiente a coordenadas de píxeles (centro del celda)
            points = [(x * self.cell + self.cell // 2, y * self.cell + self.cell // 2) 
                    for x, y in board.snake_pos]

            # Dibujar la línea conectando todos los segmentos
            pygame.draw.lines(
                self.screen,         # pantalla
                self.colors["snake"],# color
                False,               # no cerrar la línea
                points,              # lista de puntos
                self.cell // 2       # ancho de la línea
            )


        # Dibujar manzanas verdes
        for gx, gy in board.green_apples:
            pygame.draw.circle(
                self.screen,
                self.colors["green_apple"],
                (gx * self.cell + self.cell // 2, gy * self.cell + self.cell // 2),
                self.cell // 3
            )

        # Dibujar manzanas rojas
        for rx, ry in board.red_apples:
            pygame.draw.circle(
                self.screen,
                self.colors["red_apple"],
                (rx * self.cell + self.cell // 2, ry * self.cell + self.cell // 2),
                self.cell // 3
            )

        # Texto con movimientos y largo de la serpiente
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
