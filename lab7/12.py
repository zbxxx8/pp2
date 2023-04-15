import pygame, time


#defining main properties for arrows
class Arrows(pygame.sprite.Sprite):
    #initializing arrow
    def __init__(self, pos, img, freq):
        super().__init__()
        self.img, self.image = img, img
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.last_rotation = pygame.time.get_ticks()
        self.freq, self.angle, self.rev = freq, 0, 0
        all_sprites.add(self)
    
    #rotating arrows each second(here it is only used with second's arrow)
    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_rotation) // 1000 >= self.freq:
            self.last_rotation = now 
            new_image = pygame.transform.rotate(self.img, self.angle)
            if self.angle == 0:
                self.rev += 1
            self.angle = (self.angle - 6) % 360
            x, y = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)


#updated arrow class for minute arrow
class MinuteArrow(Arrows):
    def __init__(self, pos, img, freq):
        super().__init__(pos, img, freq)
    
    #minute arrow rotates only when second arrow is on the 12
    def update(self):
        if self.rev < seconds.rev:
            new_image = pygame.transform.rotate(self.img, self.angle)
            self.angle = (self.angle - 6) % 360
            x, y = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.rev += 1


#loading images and turning them on vertical position
second_hand = pygame.image.load('sec2.png')
second_hand = pygame.transform.rotate(second_hand, 60)
minute_hand = pygame.image.load('min2.png')
minute_hand = pygame.transform.rotate(minute_hand, -48)
background = pygame.image.load('mickey.jpeg')


#initializing main settings
pygame.init()
screen = pygame.display.set_mode((1300, 960))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
app = True


#creating second and minute arrows
minutes = MinuteArrow((650, 520), minute_hand, 60)
seconds = Arrows((660, 510), second_hand, 1)


#getting initial time in minutes and seconds
now = int(time.time())
start_minutes = ((now) // 60) % 60
start_seconds = (now ) % 60


#setting arrows in the right initial position
seconds.angle = -6 * start_seconds
minutes.angle = -6 * start_minutes
seconds.rev += 1


#main loop
while app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    app = False
    
    screen.fill('WHITE')
    screen.blit(background, (-40, -20))
    
    
    all_sprites.update()
    all_sprites.draw(screen)
    
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()