# Créé par Yota, le 31/08/2022 en Python 3.7
import pygame
import sys

# Démarre le système PyGame
pygame.init()

# Crée une fenêtre de 640 par 480 pixels et donne le titre "My First Game"
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game")

# Définit un rectangle
my_rectangle = pygame.Rect(10, 10, 200, 300)

# Le code du jeu qui doit tourner en boucle
while True:
    # Remplir la fenêtre avec du rouge
    window.fill((255, 0, 0))

    # Dessine le rectangle défini plus haut, en bleu.
    pygame.draw.rect(window, (0, 0, 255), my_rectangle)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Lire les évenements
    for event in pygame.event.get():
        # Quitter le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()