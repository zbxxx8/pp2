import pygame
pygame.init()
size = width, height = 500, 200
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Animation')
clock = pygame.time.Clock()
fps = 50
v = 40
x = 20
y = 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20, 0)
    x += v / fps
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()