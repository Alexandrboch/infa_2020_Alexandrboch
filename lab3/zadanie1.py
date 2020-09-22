#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (265, 170), 12)
circle(screen, (0, 0, 0), (135, 170), 12)
circle(screen, (255, 0, 0), (265, 170), 27, 16)
circle(screen, (255, 0, 0), (135, 170), 33, 22)
circle(screen, (0, 0, 0), (265, 170), 28, 2)
circle(screen, (0, 0, 0), (135, 170), 34, 2)
rect(screen, (0, 0, 0), (140, 290, 120, 20))
polygon(screen, (0, 0, 0), [(170,160), (180,150), (110,110), (100,120), (170,160)])
polygon(screen, (0, 0, 0), [(230,160), (220,150), (290,110), (300,120), (230,160)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


# In[1]:


import pygame


# In[ ]:





# In[ ]:





# In[ ]:




