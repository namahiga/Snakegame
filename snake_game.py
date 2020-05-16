import pygame
import random
import os
pygame.init()
pygame.mixer.init()
'''sounds'''
game =pygame.mixer.music.load('game.wav')
bite =pygame.mixer.Sound('bite.wav')
gameover =pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.set_volume(0.1)

'''colors'''
black=(0,0,0); white=(255,255,255); red =(255,0,0); green = (0,255,0); cyan = (0,255,255);
'''creating game window'''
width = 1280; height = 720;gamewindow = pygame.display.set_mode((width, height))
pygame .display.set_caption('snake game'); font = pygame.font.SysFont(None, 40)
'''welcome screen'''
def welcome():
    exitgame = False
    while not exitgame:
        gamewindow.fill(black)
        scoretext('WELCOME!', red, width / 4, height -600)
        scoretext('Press Any Key To Start', red, width/4,height-550)
        scoretext('Use Arrow Keys To Move', red, width / 4, height-500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                GameLoop()
            pygame.display.update()
'''score'''
def scoretext(text,colour,x,y):
    showcase =font.render(text, True, colour)
    gamewindow.blit(showcase, (x, y))
'''snake size increment'''
def snakesize(gamewindow,colour,snakelist,size):
    for x,y in snakelist:
        pygame.draw.rect(gamewindow, colour, (x, y, size, size))
'''GAME LOOP---------------------------------------------------------------------------------------------GAME LOOP'''
def GameLoop():
    pygame.mixer.music.play(-1)

    '''game variables'''
    GameExit = False ; GameOver = False
    snakex = 10; snakey = 30; size = 30
    clock = pygame.time.Clock() ; fps = 60
    velocityx = 0; velocityy = 0; initialvelocity = 5
    foodx = random.randint(0, width - size); foody = random.randint(0, height - size)
    score = 0
    snakelist = [];  snakelength = 1
    ggimage = pygame.image.load('gg.jpg')


    if (not os.path.exists('highscore.txt')):
        with open('highscore.txt','w') as h:
            h.write('0')
    '''high score track'''
    with open('highscore.txt', 'r') as h:
        highscore = h.read()
    while not GameExit:

        if GameOver:
            gamewindow.blit((ggimage),(0,0))
            with open ('highscore.txt','w') as h:
                h.write(str(highscore))
            scoretext('Press Enter To Restart',red,width/4,height-325)
            scoretext("Final Score:" + str(score), cyan, width/4, height-350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    GameExit = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    GameLoop()


        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    GameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityx = initialvelocity
                        velocityy = 0

                    if event.key == pygame.K_LEFT:
                        velocityx = -initialvelocity
                        velocityy = 0
                    if event.key == pygame.K_UP:
                        velocityy = -initialvelocity
                        velocityx = 0
                    if event.key == pygame.K_DOWN:
                        velocityy = initialvelocity
                        velocityx = 0
            snakex += velocityx
            snakey += velocityy
            if abs(snakex - foodx) < size and abs(snakey - foody) < size:
                score += 10
                foodx = random.randint(0, width-size)
                foody = random.randint(0, height-size)
                snakelength += 2
                initialvelocity +=1
                pygame.mixer.music.pause()
                pygame.mixer.Sound.play(bite)
                pygame.mixer.music.unpause()


                if score >int(highscore):
                    highscore = score


            gamewindow.fill(black)
            scoretext("Score:" + str(score), cyan, 5, 5)
            scoretext("HighScore:" + str(highscore), cyan, 1000, 5)
            pygame.draw.rect(gamewindow, green, (snakex,snakey,size,size))
            head =[]
            head.append(snakex)
            head.append(snakey)
            snakelist.append(head)
            if len(snakelist)>snakelength:
                del snakelist[0]
            if snakex< 0 or snakex>width or snakey<0 or snakey>height or head in snakelist[:-1]:
                GameOver = True
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(gameover)


            pygame.draw.rect(gamewindow, red, (foodx, foody, size, size))
            snakesize(gamewindow, green, snakelist, size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()



