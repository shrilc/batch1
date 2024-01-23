import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("KBC Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Set up questions and answers
questions = {
    "What is the capital of India?": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "What is the largest ocean in the world?": ["Pacific", "Atlantic", "Indian", "Arctic"],
    "What is the highest mountain in the world?": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"]
}

# Set up current question and answer
current_question = random.choice(list(questions.keys()))
current_answer = questions[current_question][0]

# Set up score
score = 0

# Set up game loop
running = True

while running:
    # Set keyboard repeat rate and mouse visibility
    pygame.key.set_repeat(1, 10)
    pygame.mouse.set_visible(True)

    # Clear screen
    window.fill(white)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if current_answer == questions[current_question][0]:
                    score += 1
                    current_question = random.choice(list(questions.keys()))
                    current_answer = questions[current_question][0]
                else:
                    running = False
            elif event.key == pygame.K_2:
                if current_answer == questions[current_question][1]:
                    score += 1
                    current_question = random.choice(list(questions.keys()))
                    current_answer = questions[current_question][0]
                else:
                    running = False
            elif event.key == pygame.K_3:
                if current_answer == questions[current_question][2]:
                    score += 1
                    current_question = random.choice(list(questions.keys()))
                    current_answer = questions[current_question][0]
                else:
                    running = False
            elif event.key == pygame.K_4:
                if current_answer == questions[current_question][3]:
                    score += 1
                    current_question = random.choice(list(questions.keys()))
                    current_answer = questions[current_question][0]
                else:
                    running = False

    # Draw question and answers
    question_text = font.render(current_question, True, black)
    window.blit(question_text, (50, 50))

    answer_1_text = font.render("1. " + questions[current_question][0], True, black)
    window.blit(answer_1_text, (50, 150))

    answer_2_text = font.render("2. " + questions[current_question][1], True, black)
    window.blit(answer_2_text, (50, 200))

    answer_3_text = font.render("3. " + questions[current_question][2], True, black)
    window.blit(answer_3_text, (50, 250))

    answer_4_text = font.render("4. " + questions[current_question][3], True, black)
    window.blit(answer_4_text, (50, 300))

    # Draw score
    score_text = font.render("Score: " + str(score), True, black)
    window.blit(score_text, (50, 500))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()

