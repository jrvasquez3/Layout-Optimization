

import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

# Set the object's initial position
x = 300

# Create a font for displaying the user input prompt and the user's input
font = pygame.font.Font(None, 36)

# Set up variables for tracking the user's input
user_input = ""

process = 1

# Run the game loop
running = True
while running:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Add the key press to the user's input if it is a number
            elif event.unicode.isdigit():
                user_input += event.unicode
            # Remove the last character from the user's input if they press backspace
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            # Update the object's position and reset the user's input if they press enter
            elif event.key == pygame.K_RETURN:
                speed = int(user_input)
                x -= speed
                user_input = ""
                if process == 1:
                    process = 2
                else:
                    process = 1
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Display the user input prompt
    if process == 1:
        text = font.render("Enter a speed:", True, (0, 0, 0))
        screen.blit(text, (20, 20))
    elif process == 2:
        text = font.render("Enter a Server:", True, (0, 0, 0))
        screen.blit(text, (20, 20))

    
    # Display the user's input
    text = font.render(user_input, True, (0, 0, 0))
    screen.blit(text, (20, 50))

    pygame.draw.circle(screen, (0, 0, 0), (x, 150), 20)

    # Update the display
    pygame.display.flip()


# Quit pygame
pygame.quit()
    
   
