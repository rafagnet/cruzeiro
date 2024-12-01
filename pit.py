import pygame
import random
import sys
import os

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guerras Estelares")  #Título do jogo

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

# Configuração dos inimigos
enemy_width, enemy_height = 40, 30
enemy_speed = 3
num_enemies = 5  # Número de inimigos na tela
enemies = [
    [random.randint(0, WIDTH - enemy_width), random.randint(50, 150), enemy_speed]
    for _ in range(num_enemies)
]

# Configuração do projétil
bullet_width, bullet_height = 5, 10
bullet_speed = -5
bullets = []  # Lista para armazenar os projéteis
shoot_cooldown = 0  # Tempo até o próximo disparo

# Configuração do placar
score = 0
font = pygame.font.SysFont(None, 36)  # Fonte para o texto do placar

# Caminho para a pasta de áudio
audio_folder = "audio"

# Carregar sons
shoot_sound = pygame.mixer.Sound(os.path.join(audio_folder, "shoot.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(audio_folder, "hit.wav"))
background_music = os.path.join(audio_folder, "background.mp3")

# Reproduzir música de fundo (em loop)
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)  # -1 faz a música tocar indefinidamente

# Função para desenhar o placar
def draw_score(score):
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

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
        shoot_cooldown = 10  # Cooldown entre disparos

    # Movimento dos projéteis
    for bullet in bullets[:]:  # Itera sobre uma cópia da lista de projéteis
        bullet[1] += bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)  # Remove projétil fora da tela

    # Movimento dos inimigos
    for enemy in enemies:
        enemy[0] += enemy[2]  # Move horizontalmente
        if enemy[0] <= 0 or enemy[0] >= WIDTH - enemy_width:
            enemy[2] = -enemy[2]  # Inverte direção ao atingir a borda
            enemy[1] += 40  # Move para baixo

    # Detecção de colisão entre projéteis e inimigos
    for bullet in bullets[:]:  # Itera sobre uma cópia da lista de projéteis
        bullet_removed = False  # Flag para rastrear se o projétil já foi removido
        for enemy in enemies[:]:  # Itera sobre uma cópia da lista de inimigos
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_width
                and enemy[1] < bullet[1] < enemy[1] + enemy_height
            ):
                if bullet in bullets:  # Garante que o projétil ainda está na lista
                    bullets.remove(bullet)  # Remove o projétil que acertou
                    bullet_removed = True  # Marca como removido
                enemies.remove(enemy)  # Remove o inimigo atingido
                hit_sound.play()
                score += 10  # Incrementa a pontuação
                # Adiciona um novo inimigo
                enemies.append(
                    [
                        random.randint(0, WIDTH - enemy_width),
                        random.randint(50, 150),
                        random.choice([-3, 3]),
                    ]
                )
                break  # Sai do loop de inimigos, pois o projétil foi processado
        if bullet_removed:  # Garante que não tentaremos processar o mesmo projétil novamente
            continue

    # Desenha o jogador
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Desenha os inimigos
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Desenha os projéteis
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Desenha o placar
    draw_score(score)

    # Atualiza a tela
    pygame.display.flip()

    # Taxa de quadros
    clock.tick(60)

pygame.quit()
sys.exit()