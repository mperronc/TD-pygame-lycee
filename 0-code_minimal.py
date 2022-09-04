import pygame
import sys

# Démarre le système PyGame
pygame.init()

# Crée une fenêtre de 640 par 480 pixels et donne le titre "Minimal Code"
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Minimal code")

# Le code du jeu qui doit tourner en boucle
while True:
    # Lecture des évènements
    # Un évènement se produit quand on appuie sur une touche du clavier,
    # qu'on essaie de quitter le jeu... etc...
    # ---
    # Pour chaque évènement depuis le dernier affichage...
    for event in pygame.event.get():
        # Quitter le jeu si l'utilisateur l'a demandé
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Remplit la fenêtre avec du rouge
    window.fill((255, 0, 0))

    # Met à jour l'affichage
    pygame.display.flip()
