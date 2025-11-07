import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))  # окно 800x600
pygame.display.set_caption("My Game")          # заголовок окна
clock = pygame.time.Clock()

player_img = pygame.image.load("assets/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (80, 80))
player_rect = player_img.get_rect(center=(400, 300))

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
    
    if player_rect.bottom >= 550:
        player_rect.bottom = 550
        player_y_speed = 0
        on_ground = True     

    # Ограничения по краям экрана
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800

    screen.fill((30, 30, 30))  # фон
    screen.blit(player_img, player_rect)  # рисуем игрока
    pygame.display.flip()  # обновляем экран
    clock.tick(60)

pygame.quit()
