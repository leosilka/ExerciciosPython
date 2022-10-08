import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musicpython.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('======== EXERCICIO 021 ========')
print('A musica esta tocando =D')
print('='*31)

# Exercícios proposto pelo Professor Gustavo Guanabara do Curso em Video #