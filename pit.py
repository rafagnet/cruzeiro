import pygame
import random
import sys
import os

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guerras Estelares")  # Título do jogo

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
bullets = []  # Lista para armazenar os projéteis
shoot_cooldown = 0  # Tempo até o próximo disparo

# Caminho para a pasta de áudio
audio_folder = "audio"

# Carregar sons
shoot_sound = pygame.mixer.Sound(os.path.join(audio_folder, "shoot.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(audio_folder, "hit.wav"))
background_music = os.path.join(audio_folder, "background.mp3")

# Reproduzir música de fundo (em loop)
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)  # -1 faz a música tocar indefinidamente

# Loop principal do jogo
running = True
while running:
    # Preenche a tela com a cor preta
    screen.fill(BLACK)

    # Trata eventos (como teclas pressionadas e saída do jogo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar o cooldown
    if shoot_cooldown > 0:
        shoot_cooldown -= 1

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE] and shoot_cooldown == 0:
        # Adiciona um novo projétil à lista
        bullets.append([player_x + player_width // 2, player_y])
        shoot_sound.play()
        shoot_cooldown = 10  # Cooldown entre disparos (menor valor = mais rápido)

    # Movimento dos projéteis
    for bullet in bullets[:]:
        bullet[1] += bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)  # Remove projétil fora da tela

    # Desenha os projéteis
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Movimento do inimigo
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= WIDTH - enemy_width:
        enemy_speed = -enemy_speed
        enemy_y += 40

    # Detecção de colisão
    for bullet in bullets[:]:
        if (
            enemy_x < bullet[0] < enemy_x + enemy_width
            and enemy_y < bullet[1] < enemy_y + enemy_height
        ):
            bullets.remove(bullet)  # Remove o projétil que acertou
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = 50
            hit_sound.play()  # Som de acerto

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
