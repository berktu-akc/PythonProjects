# Import Modules
import pygame
import random
import time

# Initialize module
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255,255,0)
blue = (0,0,255)
grey = (128,128,128)


# Define canvas size and title
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

#define wall

item=pygame.image.load("img.jpg")
def DrawBackground(item, xpos, ypos):
    gameDisplay.blit(item, [xpos, ypos])

# Snake speed
clock = pygame.time.Clock()
FPS = 20
# Snake and apple size
block_size = 10

# Font style and size
font = pygame.font.SysFont(None, 25)

# Define Random Colour

colours = [white, black, red, green, yellow]

# Draw Snake
def snake(block_size, snakelist, snake_renk):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, snake_renk, [XnY[0], XnY[1], block_size, block_size])

# Message parameters
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 5, display_height / 2])


# Start the game function
def gameLoop():
    gameExit = False
    gameOver = False
    # Change direction of snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    snake_renk = [yellow]
    # Assign apple random location
    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
    rand_renk  = random.choice(colours)
    first_renk = rand_renk

    while not gameExit:
        # Game menu
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over.   SCORE:{}    Press C to play again or Q to quit".format(score), red,)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Change direction of snake with arrows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Create boundaries
        """if lead_x >= display_width:  # or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            lead_x = 0
        if lead_x < 0:
            lead_x = display_width
        if lead_y >= display_height:
            lead_y = 0
        if lead_y < 0:
            lead_y = display_height
        # gameOver = True"""

        if lead_x == display_width or lead_x == 0:
            gameOver = True
        if lead_y == display_height or lead_y == 0:
            gameOver = True

        score=0

        lead_x += lead_x_change
        lead_y += lead_y_change
        #gameDisplay.fill(white)
        DrawBackground(item, 0, 0)

        # Define apple and size
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, rand_renk, [randAppleX, randAppleY, block_size, block_size])
        # Increase snake size function
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver == True

        for counter in range(0,len(snake_renk)):
            snake(block_size, snakeList, snake_renk[counter-1])
            if counter == 1:
                snake(block_size, snakeList, first_renk)
        pygame.display.update()
        # Round the size of apple to match coordinates with snake
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            rand_renk = random.choice(colours)
            snakeLength += 1
            snake_renk.append(rand_renk)

        for i in range(0,len(snakeList)):
            score += 10


        for i in snakeList[1:]:
            touch = len(snakeList)
            if snakeList[0] == i :
                gameOver = True

        # Set speed of snake
        clock.tick(FPS)
    # Game Exit
    pygame.quit()
    quit()


# Game Over
gameLoop()
