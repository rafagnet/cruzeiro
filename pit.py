import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Configuração do jogador
player_width, player_height = 50, 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - 40
player_speed = 5

# Configuração do inimigo
enemy_width, enemy_height = 40, 30
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 50
enemy_speed = 3

# Configuração do projétil
bullet_width, bullet_height = 5, 10
bullet_speed = -5
bullet_active = False
bullet_x, bullet_y = 0, 0

# Loop principal do jogo
running = True
while running:
    # Preenche a tela com a cor preta
    screen.fill(BLACK)

    # Trata eventos (como teclas pressionadas e saída do jogo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet_active = True
        bullet_x = player_x + player_width // 2
        bullet_y = player_y

    # Movimento do projétil
    if bullet_active:
        bullet_y += bullet_speed
        pygame.draw.rect(screen, RED, (bullet_x, bullet_y, bullet_width, bullet_height))
        if bullet_y < 0:
            bullet_active = False

    # Movimento do inimigo
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= WIDTH - enemy_width:
        enemy_speed = -enemy_speed
        enemy_y += 40

    # Detecção de colisão
    if (
        bullet_active
        and enemy_x < bullet_x < enemy_x + enemy_width
        and enemy_y < bullet_y < enemy_y + enemy_height
    ):
        bullet_active = False
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = 50

    # Desenha o jogador
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Desenha o inimigo
    pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Atualiza a tela
    pygame.display.flip()

    # Taxa de quadros
    clock.tick(60)

pygame.quit()
sys.exit()

