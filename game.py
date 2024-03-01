import pygame
from random import randint

#Defines the functions used in the code
def generate_startPosition_X() -> float:
    return float(randint(10, SCREEN_WIDTH-10))

def generate_startPosition_Y() -> float:
    return float(randint(10, SCREEN_HEIGHT-10))

def create_target() -> None:
    target = pygame.rect.Rect([generate_startPosition_X(),generate_startPosition_Y(), PIXEL_WIDTH,PIXEL_WIDTH])
    pygame.draw.rect(screen, "red", target)


#Starts the pygame class
pygame.init()

#Defines width and height of the screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

#Defines the width of the pixel
PIXEL_WIDTH = 50

#Starts the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Defines the loop controler
runing = True;

#Starts the snake atributes
# snake_y = [generate_startPosition()]
# snake_x = [generate_startPosition()]
snake_length = 1

#Creates the snake pixel to be drawn on screen
snake_starting_positions = [generate_startPosition_X(),generate_startPosition_Y()]
snake_px = pygame.rect.Rect([snake_starting_positions[0],snake_starting_positions[1], PIXEL_WIDTH,PIXEL_WIDTH])
snake_center = [snake_starting_positions[0],snake_starting_positions[1]]
snake = [snake_px.copy()]

#Creates the target pixel to be drawn on screen
target_starting_positions = [generate_startPosition_X(),generate_startPosition_Y()]
target_px = pygame.rect.Rect([target_starting_positions[0],target_starting_positions[1], PIXEL_WIDTH,PIXEL_WIDTH])
target_center = [target_starting_positions[0],target_starting_positions[1]]
target = [snake_px.copy()]

#Starts the game loop
while runing:
    for event in pygame.event.get(): #Iterates through the event list (Event handler)
        if event.type == pygame.QUIT:
            runing = False;

    key_pressed = pygame.key.get_pressed() #Gets the key pressed

    #Handles the key pressed
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        snake_center[1] -= PIXEL_WIDTH
    
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        snake_center[1] += PIXEL_WIDTH

    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        snake_center[0] -= PIXEL_WIDTH

    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        snake_center[0] += PIXEL_WIDTH

    snake_px = pygame.rect.Rect([snake_center[0],snake_center[1], PIXEL_WIDTH,PIXEL_WIDTH])

    #Cleans your last frame
    screen.fill("black")

    #GAME HERE

    pygame.draw.rect(screen, "red", target_px)
    pygame.draw.rect(screen, "green", snake_px)
    
    #GAME UP THERE

    #Makes your work go on screen
    pygame.display.flip()

    #Defines the game tickrate
    pygame.time.Clock().tick(10)

#Ends the game once the code is over
pygame.quit()