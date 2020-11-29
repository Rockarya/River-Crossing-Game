import pygame
pygame.init()
import math
from pygame import mixer

# creating the screen
screen=pygame.display.set_mode((1700,1000))

# Title and icon
pygame.display.set_caption("River Crossing Challenge")
icon=pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#Setting up clock variable
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',25)
frame_count = 0
frame_rate = 60

#Background Sound
mixer.music.load('bensound-energy-1.mp3')
mixer.music.play(-1)

#Player
playerImg = pygame.image.load('diver.png')
playerX = 825
playerY = 1000
playerX_change = 0 
playerY_change = 0

#creating all the dynamic enemies
enemyImg=pygame.image.load('enemy.png')
crocodileImg=pygame.image.load('shark.png')
startImg=pygame.image.load('start.png')
endImg=pygame.image.load('end.png')
obsImg=pygame.image.load('skull.png')

#Enemy1
enemy1X = 0
enemy1Y = 70
enemy1X_change = 2
enemy1Y_change = 0

#Enemy2
enemy2X = 860
enemy2Y = 110
enemy2X_change = 2
enemy2Y_change = 0

#Enemy3
enemy3X = 0
enemy3Y = 250
enemy3X_change = 2.2
enemy3Y_change = 0

#Enemy4
enemy4X = 1700
enemy4Y = 310
enemy4X_change = 2.2
enemy4Y_change = 0

#Crocodile1
croc1X = 1700
croc1Y = 500
croc1X_change = 1
croc1Y_change = 0

#Enemy5
enemy5X = 0
enemy5Y = 450
enemy5X_change = 1
enemy5Y_change = 0
 
#Enemy6
enemy6X = 0 
enemy6Y = 660
enemy6X_change = 2.5
enemy6Y_change = 0

#Crocodile2
croc2X = 1700
croc2Y = 870
croc2X_change = 2
croc2Y_change = 0

#Static Obstacles

#obs1
obs1X=625
obs1Y=-3

#obs2
obs2X=825+200
obs2Y=-3

#obs3
obs3X=525
obs3Y=-3+194

#obs4
obs4X=1125
obs4Y=-3+194

#obs5
obs5X=125
obs5Y=-3+194*2

#obs6
obs6X=825
obs6Y=-3+194*2

#obs7
obs7X=1525
obs7Y=-3+194*2

#obs8
obs8X=425
obs8Y=-3+194*3

#obs9
obs9X=1225
obs9Y=-3+194*3

#obs10
obs10X=125
obs10Y=-3+194*4

#obs11
obs11X=825
obs11Y=-3+194*4

#obs12
obs12X=1525
obs12Y=-3+194*4

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text1X = 10
text1Y = 10
text2X=10
text2Y=60
i=0
j=0
p=0
q=0

#Time
minutes1=0
seconds1=0
minutes2=0
seconds2=0



