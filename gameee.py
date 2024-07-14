import pygame
import random

def main():
    pygame.init()
    SCREEN=pygame.display.set_mode((640,480))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        SCREEN.fill((0,255,255))
        pygame.display.flip()


        
pygame.init()

#game constants
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
WIDTH=450
HEIGHT=300

#game variables
score=0
player_x=50
player_y=200

screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('game!')

background=black
fps=60
font=pygame.font.Font('freesansbold.ttf',16)
timer=pygame.time.Clock()

running=True
while running:
    timer.tick(fps)
    screen.fill(background)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
pygame.quit()
    


