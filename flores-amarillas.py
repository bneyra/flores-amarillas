# Copyright (c) 2024 Benjamin Neyra
# This software is licensed under the MIT License.

import pygame
import time
from turtle import *

# Inicializa el mezclador de pygame
pygame.mixer.init()

# Carga el archivo de audio
pygame.mixer.music.load("music-flow/flores-amarillas.mp3")

# Reproduce el archivo de audio
pygame.mixer.music.play()


# Configura la ventana de turtle
speed(20)
bgcolor("black")

# Agregar el texto en la cabecera
header_text = " para la mas linda de todas <3 "
color("red")  # Color del texto
penup()
goto(-180, 250)  # Posición del texto
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

h = 0
# Dibujar el tallo verde del girasol
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# Dibujar el girasol
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Colorear el centro de marrón
penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)  # Ajustar el radio del centro
end_fill()

done()
