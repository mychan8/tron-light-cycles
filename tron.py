import pygame

#initialize the game engine
pygame.init()

#general definitions
#x and y size board
tamanioxy = 800

#colour definitions
black = (0,0,0)
white = (140,140,140)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
random = (100,250,50)

#sets up the window
x = tamanioxy
y = tamanioxy
size=[x,y]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tron")


#sets the initial map
screen.fill(black)
for i in xrange(0,x,16):
	pygame.draw.line(screen,white,[i,0],[i,x],1)
	pygame.draw.line(screen,white,[0,i],[y,i],1)
pygame.display.flip()
#Variables for the first player
p1x = x/5
p1y = y/5
p1alive = True
p1colour = blue
p1score = 0

#speed cycle
speed = 5

#Variables for the second player
p2x = (x*3)/5
p2y = (y*3)/5
p2alive = True
p2colour = yellow
p2score = 0

#Variables for the thirt player
p3x = (x*2)/5
p3y = (x*2)/5
p3alive = True
p3colour = green
p3score = 0

#Stores a bool as to whether or not the square has been traveled already
grid = [[False for temp in xrange(x/16)] for temp in xrange(y/16)]

#Sets up the loop for the game
done = False

#Sets the players initial directions
p1direction = "right"
p2direction = "left"

#Set the 3rd player initial direction
p3direction = "down"

clock = pygame.time.Clock()
while not done:
    #Event handling
    for event in pygame.event.get():
        #Allows the loop to terminate when the user closes the window
        if event.type == pygame.QUIT:
            done = True

        #Handles keyboard input    
        elif event.type == pygame.KEYDOWN:

            #Alternative exit game
            if event.key == pygame.K_0:
                done = True
            #Changes Player 1's direction based off the key the player pressed
            if event.key == pygame.K_a:
                if p1direction != "right":
                    p1direction = "left"
            elif event.key == pygame.K_d:
                if p1direction != "left":
                    p1direction = "right"
            elif event.key == pygame.K_w:
                if p1direction !="down":
                    p1direction = "up"
            elif event.key==pygame.K_s:
                if p1direction !="up":
                    p1direction="down"

            #Changes Player 2's direction based off the key the player pressed
            elif event.key == pygame.K_RIGHT:
                if p2direction !="left":
                    p2direction = "right"
            elif event.key == pygame.K_UP:
                if p2direction !="down":
                    p2direction = "up"
            elif event.key==pygame.K_DOWN:
                if p2direction != "up":
                    p2direction="down"
            elif event.key==pygame.K_LEFT:
                if p2direction !="right":
                    p2direction="left"

            #Changes Player 3s direction based off the key the player pressed
            elif event.key == pygame.K_KP2:
                if p3direction != "up":
                    p3direction = "down"
            elif event.key == pygame.K_KP4:
                if p3direction != "right":
                    p3direction = "left"
            elif event.key == pygame.K_KP6:
                if p3direction != "left":
                    p3direction = "right"
            elif event.key == pygame.K_KP8:
                if p3direction != "down":
                    p3direction = "up"

            #Allows the user to reset the game if the space bar is hit
            elif event.key == pygame.K_SPACE:
                speed = 5
                screen.fill(black)
                for i in range(0,x,16):
                    pygame.draw.line(screen,white,[i,0],[i,x],1)
                    pygame.draw.line(screen,white,[0,i],[y,i],1)
                #Reset for 1P    
                p1x = x/5
                p1y = y/5
                p1colour = blue
                #Reset for 2P
                p2x = (x*3)/5
                p2y = (y*3)/5
                p2colour = yellow
                #Reset for 3P
                p3x = (x*2)/5
                p3y = (y*2)/5
                p3colour = green
                #Set figures for players
                grid = [[False for temp in xrange(x/16)] for temp in xrange(y/16)]
                pygame.draw.rect(screen,p1colour,[p1x + 1,p1y + 1,(x/50) -1,(x/50)-1])
                pygame.draw.rect(screen,p2colour,[p2x + 1,p2y + 1,(x/50) -1,(x/50)-1])
                pygame.draw.rect(screen,p3colour,[p3x + 1,p3y + 1,(x/50) -1,(x/50)-1])
                pygame.display.flip()
                p1alive = True
                p2alive = True
                p3alive = True





    #Redraws the players based of their movement direction
    if p1alive or p2alive or p3alive:
        pygame.draw.rect(screen,p1colour,[p1x + 1,p1y + 1,(x/50) -1,(x/50)-1])
        pygame.draw.rect(screen,p2colour,[p2x + 1,p2y + 1,(x/50) -1,(x/50)-1])
        pygame.draw.rect(screen,p3colour,[p3x + 1,p3y + 1,(x/50) -1,(x/50)-1])
        pygame.display.flip()

    #checks player 1 will travel off the map
    if p1x >= tamanioxy:
        p1x = -16
    elif p1x < 0:
        p1x = 800
    elif p1y >= tamanioxy:
        p1y = -16
    elif p1y < 0:
        p1y = 800
    #checks if player 1 will collide with another square
    else:
        if grid[p1x/16 -1][p1y/16 -1]:      
            p1alive = False
        #sets the sqarse p1 is on to true
        grid[p1x/16 -1][p1y/16 -1] = True

    #checks player 2 will travel off the map
    if p2x >= tamanioxy:
        p2x = -16
    elif p2x < 0:
        p2x = 800
    elif p2y >= tamanioxy:
        p2y = -16
    elif p2y < 0:
        p2y = 800
    #checks if player 2 will collide with another square
    else:
        if grid[p2x/16 -1][p2y/16 -1]:      
            p2alive = False
            p2colour = red
        #sets the sqare p1 is on to true
        grid[p2x/16 -1][p2y/16 -1] = True
    #checks player 3 will travel off the map
    if p3x >= tamanioxy:
        p3x = -16
    elif p3x < 0:
        p3x = 800
    elif p3y >= tamanioxy:
        p3y = -16
    elif p3y < 0:
        p3y = 800
    #checks if player 3 will collide with another square
    else:
        if grid[p3x/16 -1][p3y/16 -1]:
            p3alive = False
            p3colour = red
        #sets the sqarse p3 is on to true
        grid[p3x/16 -1][p3y/16 -1] = True
    #Updates player 1's position if they have not collided
    #after: if p1alive and p2alive and p3alive:...
    if p1alive:
            if p1direction == "left":
                p1x -=16
            elif p1direction == "right":
                p1x += 16
            elif p1direction == "up":
                p1y -= 16
            elif p1direction == "down":
                p1y +=16
    #Updates player 2's position if they have not collided
    if p2alive:
        if p2direction == "left":
            p2x -=16
        elif p2direction == "right":
            p2x += 16
        elif p2direction == "up":
            p2y -= 16
        elif p2direction == "down":
            p2y +=16
    #Updates player 3's position if they have not collided
    if p3alive:
        if p3direction == "left":
            p3x -=16
        elif p3direction == "right":
            p3x += 16
        elif p3direction == "up":
            p3y -= 16
        elif p3direction == "down":
            p3y +=16
    #Changes the player's current square to red if a collision occured
    if p1alive == False:
        p1colour = red
    if p2alive == False:
        p2colour = red
    if p3alive == False:
        p3colour = red
    #speed cycle
    speed += 1
    if(speed < 20):
        clock.tick(speed)
    else:
        clock.tick(15)
pygame.quit()
