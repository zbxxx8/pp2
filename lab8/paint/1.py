import pygame
pygame.init()
black,white,yellow,red,blue,green=(0,0,0),(255,255,255),(255,255,0),(255,0,0),(0,0,255),(0,255,0)
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
game_over = False
prev, cur = None, None
mode='pen'
color=black
thickness=5
screen.fill(white)
def drawRectangle(screen, start, end, thickness, color):
    x1,y1= start[0],start[1]
    x2,y2 = end[0],end[1]
    width = abs(x1-x2)
    height = abs(y1-y2)
    pygame.draw.rect(screen, color, (x1, y1, width, height), thickness)
def drawCircle(screen, start, end, thickness, color):
    x1,y1= start[0],start[1]
    x2,y2 = end[0],end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2 
    #x and y here are the center of the circle
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, thickness)
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.QUIT:
            exit()
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode='rectangle'
            if event.key == pygame.K_2:
                mode='circle'
            if event.key == pygame.K_p:
                mode='pen'
            if event.key == pygame.K_e: #white is used for eraser
                mode='pen'
                color=white
            if event.key == pygame.K_g:
                color =green
            if event.key == pygame.K_b:
                color =black
            if event.key == pygame.K_r:
                color =red
    if mode=='pen':       
      if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
        cur = pygame.mouse.get_pos()
        if prev:
          pygame.draw.line(screen, color, prev, cur, thickness)
          prev = cur
      if event.type == pygame.MOUSEBUTTONUP:
        prev = None
    else:
        if event.type==pygame.MOUSEBUTTONDOWN:
            draw=True
            previousPos=event.pos
        if event.type==pygame.MOUSEBUTTONUP:
            if mode=='rectangle':
                drawRectangle(screen,previousPos,event.pos,thickness,color)
            elif mode=='circle':
                drawCircle(screen,previousPos,event.pos,thickness,color)
            else:
                draw=False
        if event.type == pygame.MOUSEBUTTONUP:
            previousPos = None
  pygame.display.flip()
  clock.tick(60) # 60 is the normal fps
pygame.quit()
'''
pygame.mouse.get_pos() returns a Tuple and event.pos is a Tuple. Both give you the position of the mouse pointer as a tuple with 2 components

'''