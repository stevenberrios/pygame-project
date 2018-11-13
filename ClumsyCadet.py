from itertools import cycle
import random, sys, pygame

GAMECAPTION = "Clumsy Cadet"
SCREENWIDTH = 288
SCREENHEIGHT = 512
BASEY = SCREENHEIGHT * 0.79

# GLOBAL CONSTANTS color definitions
           #R    G    B
ORANGE =   (255, 128, 0)
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)

#images
PLAYER = ()
BACKGROUND = ()
PIPE = ()

def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)

def move_cadet(cadet, event, dist, display_surf):
    pass

def check_collapse(cadet, upperPipe, lowerPipe):
    pass

def getRandomPipe():
    """ Return randomly generated pipe """
    # y gap between upper and lower pipe
    gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = PIPE.get_height()
    pipeX = SCREENWIDTH + 10

    return[
    {'x': pipeX, 'y': gapY - pipeHeight}, #upper pipe
    {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, #lower pipe
    ]

def draw_text(text, font, display_surf, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    display_surf.blit(textobj, textrect)


def play_game():

    DISPLAY = init_main_window((SCREENWIDTH, SCREENHEIGHT), GAMECAPTION)

    FPS = 30
    fps_clock = pygame.time.Clock()

    score = 0
    font = pygame.font.SysFont(None, 20)

    #event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # draw a clean background
        DISPLAY.fill(BLUE)

        draw_text(str(score), font, DISPLAY, 10, 0)

    pygame.display.update()
    fps_clock.tick(FPS)

if __name__ == '__main__':
    play_game()

