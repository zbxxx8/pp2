import pygame
import pygame as pg
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((650, 490))
    
    clock = pygame.time.Clock()

    x, y = 325, 245 
    
    
    while True:

        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                draw_circle()
                pygame.display.update()
            
    
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key==pygame.K_UP:
                    y-=20
          

                if event.key==pygame.K_DOWN:
                    y+=20
            

                if event.key==pygame.K_LEFT:
                    x-=20   
  

                if event.key==pygame.K_RIGHT:
                    x+=20
               
        screen.fill((255, 255, 255))
       
        pygame.draw.circle(screen, (0,255,0), (x, y), 25, 0)
        if y<0 or y>=490 or x<=0 or x>=650:
            pygame.draw.circle(screen, (255,0,0), (x, y), 25, 0)    




        
        pygame.display.flip()
        clock.tick(60)

main()