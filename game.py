#import libraries
import sys
import random
import pygame 
from pygame.locals import *

#declare variables
window_height=499
window_width=600

window=pygame.display.set_mode((window_width,window_height))
elevation=window_height*0.8
get_images={}
framepersecond=32
bpipeimage = 'images/pipe.png'
background_image = 'images/background.jpg'
birdplayer_image = '/images/bird.png'
sealevel_image = '/images/base.jfif'

#intializing and importing images
if __name__ == "__main__":    
    pygame.init()
    framepersecond_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    get_images['scoreimages']=(
        pygame.image.load('images/0.png').convert_alpha(), 
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )
    get_images['flappybird']=(pygame.image.load(birdplayer_image).convert_alpha())
    get_images['background']=(pygame.image.load(background_image).convert_alpha())
    get_images['sea_level']=(pygame.image.load(sealevel_image).convert_alpha())
    get_images['pipeimage']=(pygame.transform.rotate(pygame.image.load(bpipeimage).convert_alpha()),180)

print('Welcome to the Flappy Bird Game')
print('Press space to start')

