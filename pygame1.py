import pygame
pygame.init()

display_width = 800
display_height = 600
size = [display_width, display_height]

black = (0,0,0)
white = (255,255,255)
red = (255, 0,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode(size) #what is a tuple?
'''
Answer: A tuple is a sequence of immutable Python objects. Tuples are sequences,
just like lists. The differences between tuples and lists are, the tuples cannot
be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

A useful site for tuple knowledge:
http://www.tutorialspoint.com/python/python_tuples.htm
'''

pygame.display.set_caption('Racing Game')

clock = pygame.time.Clock()

##headimg = pygame.image.load('Headshot_left_cam_Num1.png')

def piecepos(x,y):
    pygame.draw.circle(gameDisplay,red,[x,y],30)   
##    gameDisplay.blit(headimg,(x,y))

x = int((display_width * 0.45))
y = int((display_height * 0.8))

x_change = 0
y_change = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pygame function that occurs when user hits X
            crashed = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x: #pygame function that occurs when user hits X
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    print(event)
    x += x_change
    gameDisplay.fill(white)
    piecepos(x,y)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
