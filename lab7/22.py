import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))

    clock = pg.time.Clock()

    font = pg.font.SysFont("comicsansms", 72)
    text1 = font.render("music 1", True, (0, 128, 0))
    text2 = font.render("music 2", True, (0, 128, 0))
    
 


    pg.mixer.music.load('m1.mp3')
    pg.mixer.music.play()

    screen.fill((255, 255, 255))
    screen.blit(text1,
        (320 - text1.get_width() // 2, 240 - text1.get_height() // 2))
    
    pg.display.flip()

    while True:
        
        pressed = pg.key.get_pressed()
        
        alt_held = pressed[pg.K_LALT] or pressed[pg.K_RALT]
        ctrl_held = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
                if event.key==pg.K_p:
                    pg.mixer.music.play(0)
                if event.key == pg.K_s:
                    pg.mixer.music.stop()
                if event.key==pg.K_RIGHT:
                    pg.mixer.music.stop()
                    pg.mixer.music.load('m2.mp3')
                    pg.mixer.music.play(0)
                    screen.fill((255, 255, 255))
                    screen.blit(text2,
                        (320 - text2.get_width() // 2, 240 - text2.get_height() // 2))
                    pg.display.flip()
                if event.key==pg.K_LEFT:
                    pg.mixer.music.stop()
                    pg.mixer.music.load('m1.mp3')
                    pg.mixer.music.play(0)
                    screen.fill((255, 255, 255))
                    screen.blit(text1,
                        (320 - text1.get_width() // 2, 240 - text1.get_height() // 2))
                    pg.display.flip()






main()