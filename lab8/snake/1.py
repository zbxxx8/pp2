from os import scandir
from select import select
import pygame, random
import time
from pygame.locals import *
import sys

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
SPEED = 5

BLOCK_SIZE = 20
MAX_LEVEL = 4


DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))

wall_list_x = []
wall_list_y = []

wlx = [range(0, 19)]
wly = [range(0, 19)]

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

INC_SPEED = pygame.USEREVENT + 1

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class gameover:
    def gameover(self):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

wallbody = []

class Wall:
    def __init__(self, level):

        f = open("level{}.txt".format(level), "r")

        #lines = content.split('\n')
        #print(len(lines[0]))
        wallbody.clear()
        wall_list_x.clear()
        wall_list_y.clear()
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    wallbody.append(Point(x, y))
                    wall_list_x.append(x)
                    wall_list_y.append(y)
                    

    def draw(self):
        for point in wallbody:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)
        
class Food:
    def __init__(self):
        self.location = Point(random.randint(0, 19), random.randint(0, 19))
  
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 0, 255), rect)

    def spawn(self):
        self.location = Point(random.randint(0, 19), random.randint(0, 19))
        sf = self.location

    def check(self):
        for i in range(len(wallbody)):
            if self.location.x == wall_list_x[i]:
                if self.location.y == wall_list_y[i]:
                    self.spawn()



class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH or self.body[0].y * BLOCK_SIZE > HEIGHT or self.body[0].x < 0 or self.body[0].y < 0:
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,150))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

    def draw(self):
        point = self.body[0]
        
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                food.spawn()
                

    def check_collision_wall(self, wall):
        for i in range(len(wallbody)):
            if self.body[0].x == wall_list_x[i]:
                if self.body[0].y == wall_list_y[i]:
                    DISPLAYSURF.fill(RED)
                    DISPLAYSURF.blit(game_over, (30,150))
                    pygame.display.update()
                    time.sleep(2)
                    pygame.quit()



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()
    wall = Wall(snake.level)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1


        snake.move()
        snake.check_collision(food)
        snake.check_collision_wall(wall)
        food.check()


        if len(snake.body) > 4:
            newLevel = (snake.level + 1) % MAX_LEVEL
            snake = Snake()
            snake.level = newLevel
            wall = Wall(snake.level)

            
            
       
        SCREEN.fill(BLACK)

        
        snake.draw()
        
        wall.draw()
        food.draw()

        drawGrid()

        pygame.display.update()
        CLOCK.tick(5)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()
