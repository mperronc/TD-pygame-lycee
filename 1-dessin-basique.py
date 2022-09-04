import pygame
import sys

# Quelques couleurs qu'on va utiliser
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Démarrage Pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Basic drawing")

# Boucle de jeu
while True:
    # Évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)

    # Dessine un rectangle de 100x150 en (10;10), en bleu.
    pygame.draw.rect(window, BLUE, (10, 10, 100, 150))

    # Dessine une ellipse de 150x100 en (200;10), en vert.
    pygame.draw.ellipse(window, GREEN, (200, 10, 150, 100))

    # Dessine une line allant de (10;400) a (500;350) en rouge
    pygame.draw.line(window, RED, (10, 400), (500, 350))

    # Il existe d'autres fonctions de dessin
    # https://www.pygame.org/docs/ref/draw.html

    pygame.display.flip()

