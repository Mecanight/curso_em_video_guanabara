import pygame
pygame.init()
pygame.mixer.init('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
