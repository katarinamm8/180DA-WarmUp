import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock-Paper-Scissors")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
user_choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
results = {'win': 0, 'lose': 0, 'draw': 0}

def get_user_choice():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_r, pygame.K_p, pygame.K_s]:
                    return chr(event.key).lower()

def get_bot_choice():
    return random.choice(list(user_choices.keys()))

def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return 'draw'
    elif (user_choice == 'r' and bot_choice == 's') or \
         (user_choice == 'p' and bot_choice == 'r') or \
         (user_choice == 's' and bot_choice == 'p'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, bot_choice, result):
    screen.fill(white)

    user_text = font.render(f"You chose: {user_choices[user_choice]}", True, black)
    bot_text = font.render(f"Bot chose: {user_choices[bot_choice]}", True, black)
    result_text = font.render(f"You {result}!", True, black)

    screen.blit(user_text, (width // 2 - 100, height // 3))
    screen.blit(bot_text, (width // 2 - 100, height // 2))
    screen.blit(result_text, (width // 2 - 50, 2 * height // 3))

    pygame.display.flip()
    pygame.time.wait(2000)  # Display result for 2 seconds

def print_results():
    print("----- Results -----")
    print(f"Wins: {results['win']}")
    print(f"Loses: {results['lose']}")
    print(f"Draws: {results['draw']}")
    print("-------------------")

# Main game loop
while True:
    user_choice = get_user_choice()
    bot_choice = get_bot_choice()

    result = determine_winner(user_choice, bot_choice)
    display_result(user_choice, bot_choice, result)

    results[result] += 1
    print_results()
