# Dans ce programme un peu plus compliqué, on va déplacer un carré à l'aide
# des flèches du clavier.

import pygame
import sys

# Démarrage Pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving square")

# Variables du programme.

RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Position du carré
carre_x = 640 / 2
carre_y = 480 / 2

# Une horloge pour cadencer la boucle de jeu.
clock = pygame.time.Clock()

# Boucle de jeu
while True:
    # Le temps écoulé depuis le dernier affichage, en secondes.
    delta = clock.get_time() / 1000

    # Évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # On récupère la liste des touches enfoncées
    pressed_keys = pygame.key.get_pressed()

    # Si la touche D est enfoncée, augmenter carre_x de 100 par seconde
    if pressed_keys[pygame.K_d]:
        carre_x += 100 * delta
    # Et ainsi de suite...
    if pressed_keys[pygame.K_a]:
        carre_x -= 100 * delta
    if pressed_keys[pygame.K_w]:
        carre_y -= 100 * delta
    if pressed_keys[pygame.K_s]:
        carre_y += 100 * delta

    window.fill(BLACK)
    pygame.draw.rect(window, RED, (carre_x, carre_y, 50, 50))
    pygame.display.flip()

    # Limiter à 60 affichages par seconde.
    clock.tick(60)





