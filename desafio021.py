import pygame
pygame.init()
pygame.mixer.music.load('musicateste.mp3')
pygame.mixer.music.play()
pygame.event.wait(60)