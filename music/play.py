import pygame
import time
path = ['result.mp3', 't.mp3']

pygame.mixer.pre_init(frequency=16000)
pygame.mixer.init()
pygame.mixer.music.load(path[0])
pygame.mixer.music.play()

