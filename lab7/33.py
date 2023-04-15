import pygame
import pygame as pg
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    
    clock = pygame.time.Clock()

    x, y = 320, 240 
    
    
    while True:

        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                draw_circle()
                pygame.display.update()
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key==pygame.K_UP and y-50>=0:
                    y-=20
                if event.key==pygame.K_DOWN and y+50<=480:
                    y+=20
                if event.key==pygame.K_LEFT and x-50>=0:
                    x-=20   
                if event.key==pygame.K_RIGHT and x+50<=640:
                    x+=20

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255,0,0), (x, y), 25, 0)
        pygame.display.flip()
        clock.tick(60)

main()