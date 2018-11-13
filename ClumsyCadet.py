import sys
import pygame

def playgame():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Clumsy Cadet")
    bgcolor = (200,200,200)
    #create background
    while True:
        for i in pygame.event.get()
            if i.type == pygame.QUIT:
                sys.exit()
        screen.fill(bgcolor)
        pygame.display.flip()
playgame()            
    #https://stackoverflow.com/questions/41189928/pygame-how-to-change-background-color
    #https://www.pygame.org/docs/ref/key.html

#input image of the background, cadet, obstacles and music(if we can)

#keyboard link (K_UP if not push any key auto drop)

#fix if the user pressing moving bottom it can keep moving (not stop)

#scorerecord by pixels(maybe?????)
def scorerecord():

#showscore
def showscore():
    scoredigits= #index???

#checkcollapse

#creatpipe in the background

#random apply pipes in background


#mainfuction

#set the center picture of the cadet touch the pipe will cause collapse instead of the margin

#when collapse life -= 1 and reborn (3 lifes) 

#after 3 lifes collapse return gameover screen

#include the quit loop in every function so that user can stop game if they want 

#write an pause function so that it can stop in the middle

#(optional) count the time if it over 3 minutes return "YOU ARE THE CHAMP"

#need to consider the background moving speed 
