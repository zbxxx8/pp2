import pygame
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    clock = pygame.time.Clock()
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
        
        screen.fill((0, 0, 0))
        mickey = pygame.image.load('mickey.jpeg')
        mickeyr = mickey.get_rect(bottomright=(1150, 975))
        screen.blit(mickey, mickeyr)
 
        pygame.display.update()


        sec = pygame.image.load('sec2.png')  
        secr = sec.get_rect(bottomright=(682, 601))
        screen.blit(sec, secr)
        pygame.display.update()

#       angle = 15
#       def blitRotateCenter(surf, image, topleft, angle):
#
#            rotated_sec = pygame.transform.rotate(sec, angle)
#            new_rect = rotated_sec.get_rect(center = sec.get_rect(topleft = topleft).center)
#
#            surf.blit(rotated_sec, new_rect)
           



        clock.tick(60)



main()