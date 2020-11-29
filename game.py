import pygame 
pygame.init()
import math
from pygame import mixer

from config import *

def show_score1(x1,y1,x2,y2,minutes1,seconds1,minutes2,seconds2):
    global i
    global p
    global playerY
    global playerX
    global enemy1X_change
    global enemy2X_change
    global enemy3X_change
    global enemy4X_change
    global enemy5X_change
    global enemy6X_change
    global croc1X_change
    global croc2X_change
    global enemy1X
    global enemy2X
    global enemy3X
    global enemy4X
    global enemy5X
    global enemy6X
    global croc1X
    global croc2X

    if playerY < -3 +15 and playerY > -3 :
        i += 1
        enemy1X_change=2+i
        enemy2X_change=2+i
        enemy3X_change=2.2+i
        enemy4X_change=2.2+i
        enemy5X_change=1+i
        enemy6X_change=2.5+i
        croc1X_change=1+i
        croc2X_change=2+i
        enemy1X=0
        enemy2X=860
        enemy3X=0
        enemy4X=1700
        enemy5X=0
        enemy6X=0
        croc1X=1700
        croc2X=1700
        pygame.time.delay(1000)
        playerY=1000
        playerX=840
    p=score_value + 70*i
    score1=font.render("Score of Player 1:  " +str(score_value + 70*i),True,(255,255,255))
    score2=font.render("Score of Player 2:  " +str(0),True,(255,255,255))
    screen.blit(score1,(x1,y1))
    screen.blit(score2,(x2,y2))

    output_string1 = "Time for player 1: {0:02}:{1:02}".format(minutes1, seconds1)
    text = font.render(output_string1, True, (255,255,255))
    screen.blit(text, [1320,10 ])

    output_string2 = "Time for player 2: {0:02}:{1:02}".format(minutes2, seconds2)
    text = font.render(output_string2, True, (255,255,255))
    screen.blit(text, [1320,60 ])


def show_score2(x1,y1,x2,y2,minutes1,seconds1,minutes2,seconds2):
    global j
    global q
    global playerY
    global playerX
    global enemy1X_change
    global enemy2X_change
    global enemy3X_change
    global enemy4X_change
    global enemy5X_change
    global enemy6X_change
    global croc1X_change
    global croc2X_change
    global enemy1X
    global enemy2X
    global enemy3X
    global enemy4X
    global enemy5X
    global enemy6X
    global croc1X
    global croc2X

    if playerY > -3 +194*4 +150:
        j += 1
        enemy1X_change=2+j  
        enemy2X_change=2+j
        enemy3X_change=2.2+j
        enemy4X_change=2.2+j
        enemy5X_change=1+j
        enemy6X_change=2.5+j
        croc1X_change=1+j
        croc2X_change=2+j
        enemy1X=0
        enemy2X=860
        enemy3X=0
        enemy4X=1700
        enemy5X=0
        enemy6X=0
        croc1X=1700
        croc2X=1700

        pygame.time.delay(1000)
        playerY=0
        playerX=840
    q=score_value + 70*j
    score1=font.render("Score of Player 1:  " +str(p),True,(255,255,255))
    score2=font.render("Score of Player 2:  " +str(score_value + 70*j),True,(255,255,255))
    screen.blit(score1,(x1,y1))
    screen.blit(score2,(x2,y2))

    output_string1 = "Time for player 1: {0:02}:{1:02}".format(minutes1, seconds1)
    text = font.render(output_string1, True, (255,255,255))
    screen.blit(text, [1320,10 ])

    output_string2 = "Time for player 2: {0:02}:{1:02}".format(minutes2, seconds2)
    text = font.render(output_string2, True, (255,255,255))
    screen.blit(text, [1320,60 ])

def isCollision(enemyX,enemyY,playerX,playerY):
    distance=math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2)))
    if distance < 60:
        mixer.music.load('Gameover.mp3')
        mixer.music.play()
        pygame.time.delay(4000)
        return True
    else:
        return False

def konjeeta():
    screen.fill((255,255,0))
    if p > q:
        wi = font.render('Winner is Player 1 !!!',True,(0,0,255))
        screen.blit(wi,(550,300))
    elif q > p:
        wi = font.render('Winner is Player 2 !!!',True,(0,0,255))
        screen.blit(wi,(550,300))
    else:
        if seconds1 > seconds2 and q!=0:
            wi = font.render('Winner is Player 2 !! because time taken by Player2 is less',True,(0,0,255))
            screen.blit(wi,(550,300))
        elif seconds1 < seconds2 and p!=0:
            wi = font.render('Winner is Player 1 !! because time taken by Player1 is less',True,(0,0,255))
            screen.blit(wi,(550,300))
        else:
            wi = font.render('Draw Game',True,(0,0,255))
            screen.blit(wi,(550,300))

    score1=font.render("Score of Player 1:  " +str(p),True,(255,0,0))
    score2=font.render("Score of Player 2:  " +str(q),True,(255,0,0))
    screen.blit(score1,(300,600))
    screen.blit(score2,(800,600))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.init()
    from pygame import mixer
    pygame.display.update()



def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def crocodile(x,y):
    screen.blit(crocodileImg,(x,y))

def obstacle(x,y):
    screen.blit(obsImg,(x,y))

def start(x,y):
    screen.blit(startImg,(x,y))

def end(x,y):
    screen.blit(endImg,(x,y))



running=True

while running:

    screen.fill((0,191,255))
    pygame.draw.rect(screen,(150,75,0),(0,6,1900,45))
    pygame.draw.rect(screen,(150,75,0),(0,194,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*2,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*3,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*4,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,968,1900,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #contols of keystokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_UP:
                playerY_change = -0.8
            if event.key == pygame.K_DOWN:
                playerY_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    #Checking for boundaries
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1636:
        playerX = 1636

    if playerY <= 0:
        playerY = 0
    elif playerY >= 936:
        playerY = 936
    
    #Enemies movement
    enemy1X += enemy1X_change
    if enemy1X <= 0:
        enemy1X_change = 2+i
    elif enemy1X >= 1636:
        enemy1X_change = -2-i

    enemy2X += enemy2X_change
    if enemy2X <= 0:
        enemy2X_change = 2+i
    elif enemy2X >= 1636:
        enemy2X_change = -2-i

    enemy3X += enemy3X_change
    if enemy3X <= 0:
        enemy3X_change = 2.2+i
    elif enemy3X >= 1636:
        enemy3X_change = -2.2-i

    enemy4X += enemy4X_change
    if enemy4X <= 0:
        enemy4X_change = 2.2+i
    elif enemy4X >= 1636:
        enemy4X_change = -2.2-i

    enemy5X += enemy5X_change
    if enemy5X <= 0:
        enemy5X_change = 1+i
    elif enemy5X >= 1636: 
        enemy5X_change = -1-i

    croc1X += croc1X_change
    if croc1X <= 0:
        croc1X_change = 1+i
    elif croc1X >= 1636:
        croc1X_change = -1-i

    enemy6X += enemy6X_change
    if enemy6X <= 0:
        enemy6X_change = 2.5+i
    elif enemy6X >= 1636:
        enemy6X_change = -2.5-i

    croc2X += croc2X_change
    if croc2X <= 0:
        croc2X_change = 2+i
    elif croc2X >= 1636:
        croc2X_change = -2-i


    #collision detection
    collision = isCollision(enemy1X,enemy1Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy2X,enemy2Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy3X,enemy3Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy4X,enemy4Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(enemy5X,enemy5Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(croc1X,croc1Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(enemy6X,enemy6Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(croc2X,croc2Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs1X,obs1Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(obs2X,obs2Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(obs3X,obs3Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs4X,obs4Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs5X,obs5Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs6X,obs6Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs7X,obs7Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs8X,obs8Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs9X,obs9Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs10X,obs10Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs11X,obs11Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs11X,obs11Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs12X,obs12Y,playerX,playerY)
    if collision:
        running=False


    player(playerX,playerY)
    enemy(enemy1X,enemy1Y)
    enemy(enemy2X,enemy2Y)
    enemy(enemy3X,enemy3Y)
    enemy(enemy4X,enemy4Y)
    enemy(enemy5X,enemy5Y)
    crocodile(croc1X,croc1Y)
    enemy(enemy6X,enemy6Y)
    crocodile(croc2X,croc2Y)

    #static obstacles
    obstacle(obs1X,obs1Y)
    obstacle(obs2X,obs2Y)
    obstacle(obs3X,obs3Y)
    obstacle(obs4X,obs4Y)
    obstacle(obs5X,obs5Y)
    obstacle(obs6X,obs6Y)
    obstacle(obs7X,obs7Y)
    obstacle(obs8X,obs8Y)
    obstacle(obs9X,obs9Y)
    obstacle(obs10X,obs10Y)
    obstacle(obs11X,obs11Y)
    obstacle(obs12X,obs12Y)


    start(840,950)
    end(840,0)

    #player score conditions

    if playerY > -3 +194*4 +50:
        score_value = 0
    if playerY < -3 + 194*4 + 50 and playerY > -3+194*4 :
        score_value = 10
    if  playerY < -3+194*4 and playerY > -3+194*3 + 50:
        score_value = 15
    if playerY < -3 +194*3 + 50 and playerY > -3 + 194*3 :
        score_value = 25
    if playerY < -3+194*3 and playerY > -3+194*2 + 50:
        score_value = 30
    if playerY < -3 +194*2 + 50 and playerY > -3 + 194*2 :
        score_value = 40
    if playerY < -3+194*2 and playerY > -3+194 + 50:
        score_value = 45
    if playerY <  -3 +194 +50 and playerY > -3 + 194 :
        score_value = 55
    if playerY < -3+194 and playerY > -3 + 50:
        score_value = 60
    if playerY < -3 +50 and playerY > -3 :
        score_value = 70

    #Showing up time and storing

    #Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes1 = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds1 = total_seconds % 60

    show_score1(text1X,text1Y,text2X,text2Y,minutes1,seconds1,minutes2,seconds2)

    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    pygame.display.update()

#Player 2's Turn

if running == False:
    running=True
    playerY=0
    playerX=840
    frame_count = 0
    frame_rate = 60
    mixer.music.load('bensound-energy-1.mp3')
    mixer.music.play(-1)
    pygame.time.delay(1000)


while running:
    
    screen.fill((0,191,255))
    pygame.draw.rect(screen,(150,75,0),(0,6,1900,45))
    pygame.draw.rect(screen,(150,75,0),(0,194,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*2,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*3,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,194*4,1900,40))
    pygame.draw.rect(screen,(150,75,0),(0,968,1900,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #contols of keystokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_change = 1
            if event.key == pygame.K_a:
                playerX_change = -1
            if event.key == pygame.K_w:
                playerY_change = -0.8
            if event.key == pygame.K_s:
                playerY_change = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                playerX_change = 0
                playerY_change = 0


    #Checking for boundaries
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1636:
        playerX = 1636

    if playerY <= 0:
        playerY = 0
    elif playerY >= 936:
        playerY = 936
    
    #Enemies movement
    enemy1X += enemy1X_change
    if enemy1X <= 0:
        enemy1X_change = 2+j
    elif enemy1X >= 1636:
        enemy1X_change = -2-j

    enemy2X += enemy2X_change
    if enemy2X <= 0:
        enemy2X_change = 2+j
    elif enemy2X >= 1636:
        enemy2X_change = -2-j

    enemy3X += enemy3X_change
    if enemy3X <= 0:
        enemy3X_change = 2.2+j
    elif enemy3X >= 1636:
        enemy3X_change = -2.2-j

    enemy4X += enemy4X_change
    if enemy4X <= 0:
        enemy4X_change = 2.2+j
    elif enemy4X >= 1636:
        enemy4X_change = -2.2-j

    enemy5X += enemy5X_change
    if enemy5X <= 0:
        enemy5X_change = 1+j
    elif enemy5X >= 1636: 
        enemy5X_change = -1-j

    croc1X += croc1X_change
    if croc1X <= 0:
        croc1X_change = 1+j
    elif croc1X >= 1636:
        croc1X_change = -1-j

    enemy6X += enemy6X_change
    if enemy6X <= 0:
        enemy6X_change = 2.5+j
    elif enemy6X >= 1636:
        enemy6X_change = -2.5-j

    croc2X += croc2X_change
    if croc2X <= 0:
        croc2X_change = 2+j
    elif croc2X >= 1636:
        croc2X_change = -2-j


    #collision detection
    collision = isCollision(enemy1X,enemy1Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy2X,enemy2Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy3X,enemy3Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(enemy4X,enemy4Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(enemy5X,enemy5Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(croc1X,croc1Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(enemy6X,enemy6Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(croc2X,croc2Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs1X,obs1Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(obs2X,obs2Y,playerX,playerY)
    if collision:
        running=False
    
    collision = isCollision(obs3X,obs3Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs4X,obs4Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs5X,obs5Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs6X,obs6Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs7X,obs7Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs8X,obs8Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs9X,obs9Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs10X,obs10Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs11X,obs11Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs11X,obs11Y,playerX,playerY)
    if collision:
        running=False

    collision = isCollision(obs12X,obs12Y,playerX,playerY)
    if collision:
        running=False


    player(playerX,playerY)
    enemy(enemy1X,enemy1Y)
    enemy(enemy2X,enemy2Y)
    enemy(enemy3X,enemy3Y)
    enemy(enemy4X,enemy4Y)
    enemy(enemy5X,enemy5Y)
    crocodile(croc1X,croc1Y)
    enemy(enemy6X,enemy6Y)
    crocodile(croc2X,croc2Y)

    #static obstacles
    obstacle(obs1X,obs1Y)
    obstacle(obs2X,obs2Y)
    obstacle(obs3X,obs3Y)
    obstacle(obs4X,obs4Y)
    obstacle(obs5X,obs5Y)
    obstacle(obs6X,obs6Y)
    obstacle(obs7X,obs7Y)
    obstacle(obs8X,obs8Y)
    obstacle(obs9X,obs9Y)
    obstacle(obs10X,obs10Y)
    obstacle(obs11X,obs11Y)
    obstacle(obs12X,obs12Y)


    start(840,950)
    end(840,0)

    #player score conditions

    if playerY > -3 +194*4 +50:
        score_value = 70
    if playerY < -3 + 194*4 + 50 and playerY > -3+194*4 :
        score_value = 60
    if  playerY < -3+194*4 and playerY > -3+194*3 + 50:
        score_value = 55
    if playerY < -3 +194*3 + 50 and playerY > -3 + 194*3 :
        score_value = 45
    if playerY < -3+194*3 and playerY > -3+194*2 + 50:
        score_value = 40
    if playerY < -3 +194*2 + 50 and playerY > -3 + 194*2 :
        score_value = 30
    if playerY < -3+194*2 and playerY > -3+194 + 50:
        score_value = 25
    if playerY <  -3 +194 +50 and playerY > -3 + 194 :
        score_value = 15
    if playerY < -3+194 and playerY > -3 + 50:
        score_value = 10
    if playerY < -3 +50 and playerY > -3 :
        score_value = 0



    #Showing up time and storing

    #Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes2 = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds2 = total_seconds % 60


    show_score2(text1X,text1Y,text2X,text2Y,minutes1,seconds1,minutes2,seconds2)

    frame_count += 1

    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    pygame.display.update()

if running == False:
    running=True
    while running:
        konjeeta()






