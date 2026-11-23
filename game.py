import pygame

# Initializing colour
ORANGE = (245, 123, 66)
YELLOW = (255, 255, 0)

# Initializing all imported pygame modules
(numpass, numfail) = pygame.init()

# Setting size of the window
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

Icon = pygame.image.load("Snake_icon.png")
pygame.display.set_icon(Icon)
# Gets default screen size assigned above
x, y = screen.get_size()

print("Width of the window:", x, " Height of the window:", y)

pygame.display.set_caption("Hello pygame")

print("Number of modules initialized successfully: ", numpass)
print("Number of modules failed to initialize: ", numfail)

colour = ORANGE
# Changing background colour
screen.fill(colour)
pygame.display.flip()


def swap_colour(colour):
    if (colour == ORANGE):
        screen.fill(YELLOW)
        pygame.display.flip()
        return YELLOW
    else:
        screen.fill(ORANGE)
        pygame.display.flip()
        return ORANGE


# Bool value to check if game is running, default true
running = True
while running:
    # Checking for events
    for event in pygame.event.get():
        # Detect Resizing event
        if event.type == pygame.WINDOWRESIZED:
            x, y = screen.get_size()
            print("New Width of the window:", x,
                  "New height of the window:", y)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            colour = swap_colour(colour)
            print(colour)
            # Event to quit the game
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
