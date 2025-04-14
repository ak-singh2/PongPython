from sys import exit
import time
import pygame


def movement(paddle_rect, barrier_rect, barrier_rect2, screen):
    keys = pygame.key.get_pressed()
    paddle_speed = 8

    if not paddle_rect.colliderect(barrier_rect2) and not paddle_rect.colliderect(barrier_rect):
        if keys[pygame.K_UP]:
            paddle_rect.y -= paddle_speed

        elif keys[pygame.K_DOWN]:
            paddle_rect.y += paddle_speed

    elif paddle_rect.colliderect(barrier_rect):
        if keys[pygame.K_DOWN]:
            paddle_rect.y += paddle_speed

    elif paddle_rect.colliderect(barrier_rect2):
        if keys[pygame.K_UP]:
            paddle_rect.y -= paddle_speed



def movement2(paddle_rect2, barrier_rect, barrier_rect2, screen):
    keys = pygame.key.get_pressed()
    paddle_speed = 8


    if not paddle_rect2.colliderect(barrier_rect2) and not paddle_rect2.colliderect(barrier_rect):
        if keys[pygame.K_w]:
            paddle_rect2.y -= paddle_speed

        elif keys[pygame.K_s]:
            paddle_rect2.y += paddle_speed

    elif paddle_rect2.colliderect(barrier_rect):
        if keys[pygame.K_s]:
            paddle_rect2.y += paddle_speed

    elif paddle_rect2.colliderect(barrier_rect2):
        if keys[pygame.K_w]:
            paddle_rect2.y -= paddle_speed




def pong_movement(pong_rect, Vx, Vy, object_hit, name):
    speed_modifier = 0.5
    if Vx < 0:
        Vx = Vx - speed_modifier

    else:
        Vx = Vx + speed_modifier

    if Vy < 0:
        Vy = Vy - speed_modifier

    else:
        Vy = Vy + speed_modifier

    if name == 'paddle_rect' or name == 'paddle_rect2':
        Vx *= -1


    elif name == 'barrier_rect' or name == 'barrier_rect2':
        Vy *= -1

    return Vx, Vy

def run():
    pygame.init()
    width = 800
    height = 400

    screen = pygame.display.set_mode((width, height))

    paddle_rect = pygame.Rect(width - 40, height//2 - 40, 10, 60)
    paddle_rect2 = pygame.Rect(width - 760, height//2 - 40, 10, 60)

    barrier_rect = pygame.Rect(0, 0, width, 5)
    barrier_rect2 = pygame.Rect(0, height-5, width, 5)

    pong_rect = pygame.Rect(width//2, height//2, 10, 10)
    clock = pygame.time.Clock()
    background_surface = pygame.Surface((800, 400))

    player1_score = 0
    player2_score = 0
    font = pygame.font.Font(None, 64)


    # line_list = []
    # for i in range(5,height,15):
    #     line_list.append((height-2, i))

    rect_list = []
    for i in range(5, height, 10):
        rect_list.append(pygame.Rect(width//2-5, i, 5, 5))



    Vx = 5
    Vy = -2


    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(background_surface, (0,0))
        movement(paddle_rect, barrier_rect, barrier_rect2, screen) #sets up the two paddles
        movement2(paddle_rect2, barrier_rect, barrier_rect2, screen)


        if pong_rect.colliderect(paddle_rect):
            Vx, Vy = pong_movement(pong_rect, Vx, Vy, paddle_rect, 'paddle_rect')

        elif pong_rect.colliderect(paddle_rect2):
            Vx, Vy = pong_movement(pong_rect, Vx, Vy, paddle_rect2, 'paddle_rect2')

        elif pong_rect.colliderect(barrier_rect):
            Vx, Vy = pong_movement(pong_rect, Vx, Vy, barrier_rect, 'barrier_rect')

        elif pong_rect.colliderect(barrier_rect2):
            Vx, Vy = pong_movement(pong_rect, Vx, Vy, barrier_rect2, 'barrier_rect2')


        pong_rect.x += Vx
        pong_rect.y += Vy

        if pong_rect.x >= width + 10:
            player2_score += 1
            Vx = 5
            Vy = -2
            if player2_score < 5:
                pong_rect = pygame.Rect(width//2, height//2, 10, 10)
                time.sleep(0.05)


        elif pong_rect.x <= -10:
            player1_score += 1
            Vx = 5
            Vy = -2
            if player1_score < 5:
                pong_rect = pygame.Rect(width//2, height//2, 10, 10)
                time.sleep(0.05)

        screen.fill((0,0,0))
        for rect in rect_list:
            pygame.draw.rect(screen, 'white', rect)
        pygame.draw.rect(screen, 'white', paddle_rect)
        pygame.draw.rect(screen, 'white', pong_rect)
        pygame.draw.rect(screen, 'white', paddle_rect2)
        pygame.draw.rect(screen, 'white', barrier_rect)
        pygame.draw.rect(screen, 'white', barrier_rect2)

        text = font.render(f" {player2_score}     {player1_score}", True, 'white')
        text_pos = text.get_rect(centerx=background_surface.get_width()//2 - 10, y = 20)
        screen.blit(text, text_pos)


        if player1_score >= 5:
            text = font.render('Player 1 Wins!', True, 'white')
            text_pos = text.get_rect(centerx=background_surface.get_width()//2 + 5, y = 160)
            screen.blit(text, text_pos)
            pygame.display.flip()
            time.sleep(1)
            break

        elif player2_score >= 5:
            text = font.render('Player 2 Wins!', True, 'white')
            text_pos = text.get_rect(centerx=background_surface.get_width()//2 + 5, y = 160)
            screen.blit(text, text_pos)
            pygame.display.flip()
            time.sleep(1)
            break

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    run()
