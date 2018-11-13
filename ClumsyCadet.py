import pygame, sys, random
from pygame.locals import *

def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)

def load_cadet_images():
    """
    file_names = [List of all cadet gifs needed for animation]
    cadet_images = []
    for file_name in file_names:
        cadet_img = pygame.image.load(file_name)
        cadet_images.append(cadet_img)
    return(cadet_images)
    """
    pass

def move_cadet():
    pass

def hit_pipe():
    pass

def draw_text(text, font, display, x, y):
    pass

def play_game():

    DISPLAY = init_main_window((400, 300), "Clumsy Cadet")

    FPS = 15
    fps_clock = pygame.time.Clock()

    score = 0
    font = pygame.font.SysFont(None, 20)

    #event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #draw a clean background
        DISPLAY.fill(BLUE)

        # update display
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == '__main__':
    play_game()
