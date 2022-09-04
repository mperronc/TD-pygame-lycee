import pygame
import sys

BLACK = (0, 0, 0)

# Notre image
# /!\ L'image doit se trouver dans un dossier nommé "images", le dossier se
# /!\ trouvant dans le même dossier que le script !
bunny = pygame.image.load("images/bunny.png")

# Démarrage Pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Bunny picture")

# Boucle de jeu
while True:
    # Évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BLACK)

    # Pose l'image "bunny" dans la fenêtre, à la position (10;10)
    window.blit(bunny, (10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()


