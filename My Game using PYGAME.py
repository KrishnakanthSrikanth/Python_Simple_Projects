import pygame
from pygame.locals import *

# Set attributes
x_axis = 10  # left,right
y_axis = 10  # up,down
screen = 0


# Creating func to quit
def quitgame():
    if event.type == QUIT:
        pygame.quit()
        sys.exit(0)


# Creating func for Event loop
def eventloop(some_event):
    global x_axis, y_axis, screen
    for event in some_event:
        if event.key == K_ESCAPE:
            quitgame()
        else:
            if event.type == KEYDOWN:
                if event.key == K_LEFT and event.key == "A":
                    x_axis -= 5
                    print("Moving left")
                elif event.key == K_RIGHT and event.key == "D":
                    x_axis += 5
                    print("Moving right")
                elif event.key == K_UP and event.key == "W":
                    y_axis += 5
                    print("Moving up")
                elif event.key == K_DOWN and event.key == "S":
                    y_axis -= 5
                    print("Moving down")

                else:
                    print("Invalid key pressed ", event.type)
    pygame.fill((colour))
    pygame.draw.rect(screen, (51, 0, 0), (x_axis, y_axis, 10, 10))  # screen,(colour),(left,top,width,height)
    pygame.display.update()


# Creating func main
def main():
    global screen
    # Initialize pygame
    pygame.init()

    screen_width = 600
    screen_height = 500

    colour = [0, 0, 255]  # Blue colour

    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('My Game')

    screen = pygame.display.get_surface()

    # pygame.display.flip(0,0,0)
    pygame.display.update()

    while True:
        eventloop(pygame.event.get())


main()