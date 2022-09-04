import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Dans ce programme, l'écran change de couleur quand on appuie sur Entrée.

# La "lumière" controllée par la touche Entrée
lumiere = False

# Texte qui sera affiché à l'écran
pygame.font.init()
text_font = pygame.font.SysFont("Arial", 18)
text = text_font.render("Apppuyez sur Entrée pour allumer / éteindre la lumière", True, RED)

# Démarrage Pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Lights On")

# Boucle de jeu
while True:
    # Évènements
    for event in pygame.event.get():

        # Si une touche est appuyée...
        if event.type == pygame.KEYDOWN:
            # Si cette touche est la touche Entrée
            if event.key == pygame.K_RETURN:
                # Active/Desactive la lumière
                lumiere = not lumiere

        # Quitter le jeu
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # On remplit l'écran en blanc si la lumière est allumée, en noir sinon
    fill_color = WHITE if lumiere else BLACK
    window.fill(fill_color)

    window.blit(text, (10, 10))
    pygame.display.flip()

