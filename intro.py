
import pygame
import src  # our source module with the algorithms
import sys  # another python library, here enables us to
import hlp  # module with the helper functions

'''
in python, you can  seperate one script into several files and the main way to do this is with python's import statement
we can use import both for importing existing python libraries and also for importing objects, functions and variables from the other python scripts i created
if my script is in current working directions and its sub directories i can use import to do so

i import everyting from sys to prevent possible clashes since some of the functions here depend on the variables in the main simulation
__init__.py is a special empty file telling python that it should look into this folder as a package
__main__ is another method telling the script where to start the program
'''

# activate flag for algorithm list menu
intro2 = False
# introduction menu
pygame.init()


def StartIntro2():
    global intro2  # access the global variable
    intro2 = True  # turn it true, these are all helper functions


def Introduction():
    '''
    setting the intro menu
    '''
    global intro2  # accessing global variable
    pygame.display.set_caption("Line Segment Intersection Visualisation Tool")
    while intro2 == False:  # initial loop and setting the exit
        src.display.fill((0, 0, 0))  # setting the display colour
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.
        font = pygame.font.Font(src.bitterfont, 21)  # creating font with size
    # creating font pygame text object with size, colour and text
        renderedText = font.render(
            "Welcome to the Line Segment Intersection Visualisation Tool", True, (255, 255, 255))

    # displaying text on the screen, pos is the position of where it should appear
        surface = pygame.display.get_surface()
        xwidth = (surface.get_width() / 2) - 60
        twidth = surface.get_width() / 2 - renderedText.get_width() / 2
        src.display.blit(renderedText, (twidth, 140))
        hlp.Button("Continue", xwidth, 200, 120, 30,
                   StartIntro2)  # continue button
        hlp.Button("Exit", xwidth, 250, 120,
                   30, sys.exit)
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 10 frames per second
        src.clock.tick(60)
    Introduction2()  # calls back the introduction function

# algorithm list menu


def Introduction2():
    '''
    Setting the algorithms menu
    '''
    display = pygame.display.set_mode(
        (1280, 550), pygame.FULLSCREEN | pygame.DOUBLEBUF)  # seting the display
    # pygame method for captioning
    pygame.display.set_caption("Line Segment Intersection Visualisation Tool")
    src.ChangeColour()  # calling change colour function
    while True:  # stating the loop
        display.fill((0, 0, 0))  # setting the display colour
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function
        surface = pygame.display.get_surface()
        xwidth = (surface.get_width() / 2) - 125
        pygame.draw.rect(display, hlp.button_colour,
                         (xwidth - 7, 85, 264, 450), 3)
        v1 = hlp.ButtonWithReturn("Brute-Force Algorithm", xwidth, 90, 250,
                                  30, 1)  # positioning function buttons
        v2 = hlp.ButtonWithReturn("Bentley-Ottmann Algorithm", xwidth, 190,
                                  250, 30, 2)  # positioning function buttons
        v3 = hlp.ButtonWithReturn("Shamos-Hoey Algorithm", xwidth, 290, 250,
                                  30, 3)  # positioning function buttons
        v4 = hlp.ButtonWithReturn("Efficiency Comparison", xwidth, 390, 250,
                                  30, 4)  # positioning function buttons
        v5 = hlp.ButtonWithReturn("Efficiency Comparison 2", xwidth, 490, 250,
                                  30, 5)  # positioning function buttons
        hlp.Button("Exit to Desktop", xwidth, 590, 250,
                   30, sys.exit)  # adding an exit button
        # if any is chosen, break the loop and go to the choice
        if v1 > 0 or v2 > 0 or v3 > 0 or v4 > 0 or v5 > 0:
            break
        pygame.display.flip()  # updates the screen every turn
        src.clock.tick(60)  # will not run more than 10 frames per second
    if v1 > 0:  # calling for choice functions to go for
        src.BruteForceMain()  # calling for choice functions to go for
    elif v2 > 0:  # calling for choice functions to go for
        src.BentleyMain()  # calling for choice functions to go for
    elif v3 > 0:  # calling for choice functions to go for
        src.ShamosHoeyMain()  # calling for choice functions to go for
    elif v4 > 0:  # calling for choice functions to go for
        src.Efficiency()  # calling for choice functions to go for
    elif v5 > 0:
        src.Efficiency2()
