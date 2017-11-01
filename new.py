import pygame
from object import Car
 
#Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (210, 210 ,210)

#Initialize pygame
pygame.init()

#Set the screen dimension [width,height]
size = [1080, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ROVER")

all_sprites_list = pygame.sprite.Group()

playerCar = Car(GREY, 40, 50)
playerCar.rect.x = 200
playerCar.rect.y = 300

#List that contains all sprites
all_sprites_list.add(playerCar)

#Bool value that allows the user to close the window
carryOn = True
clock = pygame.time.Clock()
 
#For counting jJoystick
joystick_count = pygame.joystick.get_count()
if joystick_count != 0:
    #Initialize Joystick
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
 
while carryOn:
 
    #Events in Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            #Exit by using X key
            if event.key==pygame.K_x:
                carryOn = False
                
    #Including Joystick
    if joystick_count != 0:
 
        # This gets the position of the axis on the game controller.
        horiz_axis_pos = gamepad.get_axis(0)
        vert_axis_pos = gamepad.get_axis(1)

        #Movement Logic
        
        #Movement of X and Y axis from the current location.
        #Multiply the position of the joystick by 1.5 to speed up the sprite
        playerCar.rect.x = playerCar.rect.x + int(horiz_axis_pos * 1.5)
        playerCar.rect.y = playerCar.rect.y + int(vert_axis_pos * 1.5)

    #Including Keyboard
        '''
        keys = pygame.key.get_pressed()

        #Movement [Left, Right, Up, Down]
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            playerCar.moveUp(5)
        if keys[pygame.K_DOWN]:
            playerCar.moveDown(5)
        '''

    all_sprites_list.update()
    #Game Logic

    #Drawing on Screen
    screen.fill(BLACK)
 
    # Draw the item at the proper coordinates
    all_sprites_list.draw(screen)
 
    #Refresh Screen
    pygame.display.flip()

    #No. of Frames per sec.
    clock.tick(60)
 
pygame.quit()
