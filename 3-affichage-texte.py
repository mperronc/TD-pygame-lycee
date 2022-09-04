import pygame
import sys

BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Démarrage Pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Displaying Text")

# Démarre le système qui gère les polices.
pygame.font.init()
# Crée une police Arial taille 32
text_font = pygame.font.SysFont("Arial", 32)
# Crée le texte, avec la police créée au-dessus, lissé et en rouge.
text = text_font.render("Bienvenue dans Pygame !", True, RED)

# Boucle de jeu
while True:
    # Évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Affiche le texte créé au début du programme à l'écran
    window.blit(text, (10, 10))

    pygame.display.flip()