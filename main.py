import pygame
from os import path

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))  # окно 800x600
pygame.display.set_caption("Pusheen Game")          # заголовок окна
clock = pygame.time.Clock()

music_path = path.join("snd", "mp3.ogg")  # путь к музыке
pygame.mixer.music.load(music_path)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

background_img = pygame.image.load("assets/bg.png").convert()
background_img = pygame.transform.scale(background_img, (800, 400))

player_img = pygame.image.load("assets/player.png").convert_alpha() 
player_img = pygame.transform.scale(player_img, (110, 110))
player_rect = player_img.get_rect(center=(400, 500))

gravity = 0.8
jump_power = -15
player_y_speed = 0
on_ground = True

running = True
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP] and on_ground:
        player_y_speed = jump_power
        on_ground = False
        
    player_y_speed += gravity
    player_rect.y += player_y_speed     
    
    if player_rect.bottom >= 380:
        player_rect.bottom = 380
        player_y_speed = 0
        on_ground = True     

    # Ограничения по краям экрана
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800

    screen.blit(background_img, (0, 0))
    screen.blit(player_img, player_rect)  # рисуем игрока
    pygame.display.flip()  # обновляем экран
    clock.tick(60)

pygame.quit()