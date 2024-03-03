# import tkinter as tk
# from tkinter import messagebox

# def check_winner(board, player):
#     # Check rows, columns, and diagonals for a win
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)):
#             return True
#         if all(board[j][i] == player for j in range(3)):
#             return True
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True
#     return False

# def on_click(row, col):
#     global player, turns
#     if board[row][col] == " ":
#         buttons[row][col].config(text=player)
#         board[row][col] = player
#         if check_winner(board, player):
#             messagebox.showinfo("Winner", f"Player {player} wins!")
#             reset_game()
#         elif turns == 8:
#             messagebox.showinfo("Draw", "It's a draw!")
#             reset_game()
#         player = "O" if player == "X" else "X"
#         turns += 1

# def reset_game():
#     global player, turns, board
#     player = "X"
#     turns = 0
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     for row in range(3):
#         for col in range(3):
#             buttons[row][col].config(text=" ", state="normal")

# root = tk.Tk()
# root.title("Tic Tac Toe")

# buttons = []
# board = [[" " for _ in range(3)] for _ in range(3)]
# player = "X"
# turns = 0

# for i in range(3):
#     row_buttons = []
#     for j in range(3):
#         button = tk.Button(root, text=" ", font=("Helvetica", 24), width=4, height=2, command=lambda row=i, col=j: on_click(row, col))
#         button.grid(row=i, column=j, padx=5, pady=5)
#         row_buttons.append(button)
#     buttons.append(row_buttons)

# reset_button = tk.Button(root, text="Reset", font=("Helvetica", 12), command=reset_game)
# reset_button.grid(row=3, column=1, columnspan=3, pady=10)

# root.mainloop()

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surfers Lite")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect(center=(100, HEIGHT - 50))
player_speed = 5

# Obstacles
obstacle_img = pygame.image.load('obstacle.png')
obstacle_rect = obstacle_img.get_rect(center=(WIDTH + 200, HEIGHT - 50))
obstacle_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_rect.y -= player_speed

    player_rect.y += 1

    if player_rect.colliderect(obstacle_rect):
        running = False

    if obstacle_rect.x <= -100:
        obstacle_rect.x = WIDTH + 200
        obstacle_rect.y = random.randint(HEIGHT - 150, HEIGHT - 50)
        score += 1

    obstacle_rect.x -= obstacle_speed

    screen.blit(player_img, player_rect)
    screen.blit(obstacle_img, obstacle_rect)

    draw_text(f"Score: {score}", font, RED, 100, 50)

    pygame.display.update()
    clock.tick(60)

pygame.quit()


