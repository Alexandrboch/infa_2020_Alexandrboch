import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS=30
screen = pygame.display.set_mode((840, 1080))

#фон
rect(screen, (0, 102, 128), (0, 0, 840, 1080))
rect(screen, (33, 33, 120), (0, 0, 840, 110))
rect(screen, (141, 95, 211), (0, 110, 840, 57))
rect(screen, (205, 135, 222), (0, 167, 840, 97))
rect(screen, (222, 135, 170), (0, 264, 840, 138))
rect(screen, (255, 153, 85), (0, 402, 840, 118))


def chaika(angle,size): #чайка входные параметры - угол, размер
    surface = pygame.Surface((840, 1080), pygame.SRCALPHA)
    arc(surface, (255, 255, 255), (10, 100, 180, 120), np.pi / 10, 3 * np.pi / 4, 3)
    arc(surface, (255, 255, 255), (180, 100, 180, 120), np.pi / 4, 9 * np.pi / 10, 3)
    surface = pygame.transform.rotozoom(surface, angle, size)
    rect = surface.get_rect()
    rotated_surface = pygame.transform.rotate(surface, 0)
    screen.blit(rotated_surface, rect)

def fish(angle,size): #рыба входные параметры - угол, размер
    surface = pygame.Surface((840, 1080), pygame.SRCALPHA)
    ellipse(surface, (71, 136, 147), (500, 759, 180, 60))
    arc(surface, (0, 0, 0), (500, 759, 180, 60), 0, 2 * np.pi, 1)
    circle(surface, (0, 53, 189), (655, 789), 12)
    circle(surface, (0, 0, 0), (657, 790), 5)
    polygon(surface, (71, 136, 147), [(509, 789), (470, 819), (470, 759), (509, 789)])
    polygon(surface, (0, 0, 0), [(509, 789), (470, 819), (470, 759), (509, 789)], 1)
    polygon(surface, (102, 99, 112), [(515, 740), (595, 740), (615, 760), (555, 760), (515, 740)])
    polygon(surface, (0, 0, 0), [(515, 740), (595, 740), (615, 760), (555, 760), (515, 740)], 1)
    polygon(surface, (102, 99, 112), [(515, 835), (545, 835), (550, 814), (530, 810), (515, 835)])
    polygon(surface, (0, 0, 0), [(515, 835), (545, 835), (550, 814), (530, 810), (515, 835)], 1)
    polygon(surface, (102, 99, 112), [(595, 839), (630, 834), (615, 816), (600, 816), (595, 839)])
    polygon(surface, (0, 0, 0), [(595, 839), (630, 834), (615, 816), (600, 816), (595, 839)], 1)
    surface = pygame.transform.rotozoom(surface, angle, size)
    rect = surface.get_rect()
    rotated_surface = pygame.transform.rotate(surface, 0)
    screen.blit(rotated_surface, rect)

def ytka(angle,size): #утка входные параметры - угол, размер
    surface = pygame.Surface((840, 1080), pygame.SRCALPHA)
    # задняя лапа
    polygon(surface, (255, 255, 255), [(340, 530), (370, 610), (395, 600), (385, 500), (340, 530)])
    polygon(surface, (255, 255, 255), [(370, 610), (420, 620), (425, 610), (390, 599), (370, 610)])
    polygon(surface, (255, 211, 85), [(445, 615), (465, 620), (445, 625), (445, 640), (435, 630), (435, 640), (425, 620), (415, 630), (425, 610), (445, 615)])
    polygon(surface, (0, 0, 0), [(445, 615), (465, 620), (445, 625), (445, 640), (435, 630), (435, 640), (425, 620), (415, 630), (425, 610), (445, 615)], 1)
    # заднее крыло
    polygon(surface, (255, 255, 255), [(390, 460), (380, 420), (350, 390), (140, 340), (105, 330), (130, 360), (145, 370), (160, 380), (190, 390), (240, 405), (270, 420), (280, 480), (390, 460)])
    polygon(surface, (0, 0, 0), [(390, 460), (380, 420), (350, 390), (140, 340), (105, 330), (130, 360), (145, 370), (160, 380), (190, 390), (240, 405), (270, 420), (280, 480), (390, 460)], 1)
    # тело
    ellipse(surface, (255, 255, 255), (200, 450, 250, 125))
    ellipse(surface, (255, 255, 255), (400, 465, 130, 50))
    # голова
    ellipse(surface, (255, 255, 255), (500, 450, 85, 60))
    ellipse(surface, (0, 0, 0), (557, 470, 15, 9))
    # клюв
    polygon(surface, (255, 221, 85), [(580, 477), (580, 472), (630, 463), (645, 477), (580, 477)])
    polygon(surface, (255, 221, 85), [(580, 477), (580, 482), (630, 491), (645, 477), (580, 477)])
    polygon(surface, (0, 0, 0), [(580, 477), (580, 472), (630, 463), (645, 477), (580, 477)], 1)
    polygon(surface, (0, 0, 0), [(580, 477), (580, 482), (630, 491), (645, 477), (580, 477)], 1)
    # передняя лапа
    polygon(surface, (255, 255, 255), [(290, 550), (320, 630), (355, 620), (345, 520), (290, 550)])
    polygon(surface, (255, 255, 255), [(320, 630), (390, 640), (395, 630), (350, 615), (320, 630)])
    polygon(surface, (255, 211, 85), [(415, 635), (435, 640), (415, 645), (415, 660), (405, 650), (405, 660), (395, 640), (385, 650), (395, 630), (415, 635)])
    polygon(surface, (0, 0, 0), [(415, 635), (435, 640), (415, 645), (415, 660), (405, 650), (405, 660), (395, 640), (385, 650), (395, 630), (415, 635)], 1)
    # хвост
    polygon(surface, (255, 255, 255), [(230, 540), (205, 539), (170, 530), (180, 440), (215, 480), (240, 500), (230, 540)])
    polygon(surface, (0, 0, 0), [(230, 540), (205, 539), (170, 530), (180, 440), (215, 480), (240, 500), (230, 540)], 1)
    # переднее крыло
    polygon(surface, (255, 255, 255), [(380, 500), (370, 460), (340, 430), (130, 400), (95, 390), (120, 420), (135, 430), (150, 440), (180, 450), (230, 465), (260, 480), (270, 520), (380, 500)])
    polygon(surface, (0, 0, 0), [(380, 500), (370, 460), (340, 430), (130, 400), (95, 390), (120, 420), (135, 430), (150, 440), (180, 450), (230, 465), (260, 480), (270, 520), (380, 500)], 1)
    surface = pygame.transform.rotozoom(surface, angle, size)
    rect = surface.get_rect()
    rotated_surface = pygame.transform.rotate(surface, 0)
    screen.blit(rotated_surface, rect)

fish(0, 1)
fish(360, 0.8)
chaika(0, 1)
chaika(10, 0.5)
chaika(-30, 1)
chaika(-25, 0.8)
chaika(0, 1)
ytka(360, 0.4)
ytka(0, 0.9)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True



pygame.quit()