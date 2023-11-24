import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la ventana de visualización
ventana = pygame.display.set_mode((800, 600))

# Configura el reloj para limitar los fps
reloj = pygame.time.Clock()

# Define el objeto del jugador
jugador = pygame.Rect(400, 300, 50, 50)

# Bucle del juego
corriendo = True
while corriendo:
    # Limita los fps a 60
    reloj.tick(60)

    # Maneja los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Maneja las entradas del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.move_ip(-5, 0)
    if teclas[pygame.K_RIGHT]:
        jugador.move_ip(5, 0)
    if teclas[pygame.K_UP]:
        jugador.move_ip(0, -5)
    if teclas[pygame.K_DOWN]:
        jugador.move_ip(0, 5)

    # Llena la ventana con color negro
    ventana.fill((0, 0, 0))

    # Dibuja el jugador
    pygame.draw.rect(ventana, (255, 0, 0), jugador)

    # Actualiza la pantalla
    pygame.display.flip()

# Finaliza Pygame
pygame.quit()
sys.exit()