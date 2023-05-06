import random, sys,pygame
pygame.init()
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE  = 0
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # установление экрана
pygame.display.set_caption("RACER GAME") #название экрана
clock = pygame.time.Clock()
global NUM_OF_COINS
NUM_OF_COINS = 0
score_font = pygame.font.SysFont("Verdana", 20) #шрифт для счетчиков
bg = pygame.image.load("AnimatedStreet.png") #background

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
        #положение энеми по иксу задается рандомно учитывая ширину машинки
    def update(self):
        global SCORE,ENEMY_STEP
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1 # если энеми проехал всю высоту экрана, это плюс к скору
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
            #setting the new position after enemy passes the player
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        #the player always spawns on one position

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('coin1.png')
        self.image=pygame.transform.scale(self.image,(25,25))
        #задаем определенный размер картинке монетки
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)


P1 = Player()
E1 = Enemy()
C1=Coin()


enemies = pygame.sprite.Group()
enemies.add(E1)
#adding coins to the sprite group
coins=pygame.sprite.Group()
coins.add(C1)


k = 1
#Каждые 15 новых собранных коинов
#скорость врага увеличивается на 1 единицу
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()
   
    if pygame.sprite.spritecollideany(P1, coins):
       NUM_OF_COINS += 1
       if NUM_OF_COINS >= k * 2:
           ENEMY_STEP += 1
           k += 1
       C1.spawn() #как только игрок тронул монету, нужно создать новую
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
    SURF.blit(bg, (0, 0))
    score_img = score_font.render('Number of passing cars: '+str(SCORE), True, BLACK)
    coin_score_img=score_font.render('Number of collected coins: '+str(NUM_OF_COINS),True,BLACK)
    speed_img=score_font.render('Enemy speed: '+ str(ENEMY_STEP),True,BLACK)
    SURF.blit(score_img, (10, 10)) #позиция счетчика машин
    SURF.blit(coin_score_img,(30,30)) #позиция счетчика монет
    SURF.blit(speed_img,(50,50))
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)

    pygame.display.update()
    clock.tick(FPS)