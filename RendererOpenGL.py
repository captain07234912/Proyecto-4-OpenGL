import pygame
from pygame.locals import *
from pygame import mixer
from gl import Renderer, Model
import shaders

"""
Universidad del Valle de Guatemala
Graficas por computadora
OpenGL
Jorge Suchite Carnet 15293
29/11/2020

Renderer 

"""
# pip install mixer
pygame.mixer.init()
pygame.mixer.music.load('Donkey.mp3')
pygame.mixer.music.play(5000000)
deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 15
r.pointLight.x = 10

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

r.modeloLista.append(Model('patrick.obj', 'Char_Patrick.bmp'))
r.modeloLista.append(Model(fileName ='Charizard.obj', textureName='lizardtext.bmp'))
r.modeloLista.append(Model(fileName ='Astronaut.obj', textureName='space.bmp'))
r.modeloLista.append(Model(fileName ='narutokun.obj', textureName='Body.bmp'))

isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Move cam
    if keys[K_d]:
        r.camPosition.x += 10 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 10 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 10 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 10 * deltaTime
 # CERCA  CON Q Y LEJOS CON E
    if keys[pygame.K_q]:
        if r.camPosition.z < 150:
            r.camPosition.z += 50 * deltaTime
    if keys[pygame.K_e]:
        if r.camPosition.z > 5:
            r.camPosition.z -= 50 * deltaTime


    # luz del objeto
    if keys[pygame.K_LEFT]:
        r.pointLight.x -= 30 * deltaTime
    if keys[pygame.K_RIGHT]:
        r.pointLight.x += 30 * deltaTime
    if keys[pygame.K_UP]:
        r.pointLight.y += 30 * deltaTime
    if keys[pygame.K_DOWN]:
        r.pointLight.y -= 30 * deltaTime
    if keys[pygame.K_k]:
        r.pointLight.z += 30 * deltaTime
    if keys[pygame.K_l]:
        r.pointLight.z -= 30 * deltaTime

        # rotar
        if keys[pygame.K_b]:  # Pitch
            r.rotation.x -= 30 * deltaTime
        if keys[pygame.K_n]:
            r.rotation.x += 30 * deltaTime
        if keys[pygame.K_m]:  # Yaw
            r.rotation.y -= 30 * deltaTime
        if keys[pygame.K_c]:
            r.rotation.y += 30 * deltaTime
        if keys[pygame.K_v]:  # Roll
            r.rotation.z += 30 * deltaTime
        if keys[pygame.K_x]:
            r.rotation.z -= 30 * deltaTime
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_t:  # Cambiar
                r.coronamodelo = (r.coronamodelo + 1) % len(r.modeloLista)

## uso del mouse
        elif ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                r.camPosition.x += 55 * deltaTime
            if ev.button == 2:
                r.camPosition.x = 5
                r.camPosition.y = 10
                r.camPosition.z = 55

            if ev.button == 3:
                r.camPosition.x -= 70 * deltaTime

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
