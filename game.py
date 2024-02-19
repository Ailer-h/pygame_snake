import pygame

#Starts the pygame class
pygame.init()

#Defines width and height of the screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

#Starts the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Defines the loop controler
runing = True;

#Starts the game loop
while runing:
    for event in pygame.event.get(): #Iterates through the event list (Event handler)
        if event.type == pygame.QUIT:
            runing = False;


pygame.quit()