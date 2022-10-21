import pygame
import os, sys
from fcntl import ioctl
import time
from operator import xor

'''
    Constants
'''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFont("Ubuntu", 40)

delay = 30

paddle_speed = 20

paddle_width = 10
paddle_height = 100

p1_x_pos = 10
p1_y_pos = HEIGHT / 2 - paddle_height / 2

p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = HEIGHT / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2
ball_width = 8
ball_x_vel = -10
ball_y_vel = 0

num_buttons = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RD_BUTTON = 29430 

def button_pressed(button_set):
    """
    Return an array of pressed buttons, 1 if pressed else 0 
    """
    return [1 if button_set & (1 << actual) else 0 for actual in range(num_buttons)]

def read_button_set():
    """
    Return array containing button set state
    """
    ioctl(fd, RD_PBUTTONS)
    read = os.read(fd, 4); # read 4 bytes and store in red var
    read = int.from_bytes(read, 'little')
    return read

def draw_objects():
    pygame.draw.rect(
        screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height)
    )
    pygame.draw.rect(
        screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height)
    )
    pygame.draw.circle(screen, WHITE, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH / 2, 30))
    # Debug ONLY
    # p1_state = game_font.render(f"{str(p1_down)} + ',' + {str(p1_up)}", False, WHITE)
    # p2_state = game_font.render(f"{str(p2_down)} + ',' + {str(p2_up)}", False, WHITE)
    # screen.blit(p1_state, (WIDTH / 2, 60))
    # screen.blit(p2_state, (WIDTH / 2, 90))


def apply_player_movement():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 5)
    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, 485)
    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 5)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, 485)


def apply_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global p1_score
    global p2_score

    if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (
        p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height
    ):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel < 0:
        p2_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_vel = 10
        ball_y_vel = 0
    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (
        p2_y_pos < ball_y_pos + ball_y_vel + ball_width < p2_y_pos + paddle_height
    ):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel > HEIGHT:
        p1_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_vel = 10
        ball_y_vel = 0
    if ball_y_pos + ball_y_vel > HEIGHT or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel

def main_loop():
    pygame.display.set_caption("Pong Ping")
    screen.fill(BLACK)
    pygame.display.flip()
    fd =  os.open(sys.argv[1],os.O_RDWR)
    running = True
    while running:
        set_buttons = read_button_set()
        pressed_buttons = button_pressed(set_buttons)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if pressed_buttons[0]: # Player1 buttons, Only read the first valid position, ignore the rest of pressed buttons
                    p1_up, p1_down = True, False
            elif pressed_buttons[1]:
                    p1_up, p1_down = False, True
            if pressed_buttons[2]: # Player2 buttons
                    p2_up, p2_down = True, False
            elif pressed_buttons[3]:
                    p2_up, p2_down = False, True
            if event.type == pygame.KEYUP:
                if xor(event.key == pygame.K_w, event.key == pygame.K_s):
                    p1_up, p1_down = False, False
                if xor(event.key == pygame.K_UP, event.key == pygame.K_DOWN):
                    p2_up, p2_down = False, False

        screen.fill(BLACK)
        apply_player_movement()
        apply_ball_movement()
        draw_objects()
        pygame.display.flip()
        pygame.time.wait(delay)

if __name__ == '__main__':
   fd = os.open(sys.argv[1], os.O_RDWR)
   main_loop()
   os.close(fd)
   pygame.quit()