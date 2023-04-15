import pygame
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    clock = pygame.time.Clock()
    
    while True:
        
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        screen.fill((0, 0, 0))
        mickey = pygame.image.load('mickey.jpeg')
        mickeyr = mickey.get_rect(bottomright=(1150, 975))
        screen.blit(mickey, mickeyr)
 
        


        sec = pygame.image.load('sec2.png')  
        secr = sec.get_rect(bottomright=(682, 601))
        screen.blit(sec, secr)
        pygame.display.update()

        secrot = pygame.transform.rotate(secr, 20)

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