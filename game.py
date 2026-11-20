import pygame

# Initializing all imported pygame modules
(numpass, numfail) = pygame.init()

# Setting size of the window
screen = pygame.display.set_mode((800, 600))
# Gets default screen size assigned above
x, y = screen.get_size()

print("Width of the window:", x, " Height of the window:", y)

pygame.display.set_caption("Hello pygame")

print("Number of modules initialized successfully: ", numpass)
print("Number of modules failed to initialize: ", numfail)

# Bool value to check if game is running, default true
running = True
while running:
    # Checking for events
    for event in pygame.event.get():

        # Event to quit the game
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
