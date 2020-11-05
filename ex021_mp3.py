# Desafio021
# ----------
# Faça um programa em Python que abra e reproduza
# o áudio de um arquivo mp3

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

import pygame 

pygame.init()
pygame.mixer.music.load('confirm_delivery.mp3')
pygame.mixer.music.play()
pygame.event.wait()