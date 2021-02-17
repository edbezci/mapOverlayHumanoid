# from src import display
# importing discplay object from the src
import pygame
import os
import src

# defining RGB colour choices
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
button_colour = pygame.Color(75, 0, 130)
hover_colour = pygame.Color(255, 105, 180)


'''
compiling all helper functions in this module
'''


def Button(name, x, y, w, dist, action=None):
    '''
    this function creates the button on the screen.
    it takes the positions, fonts, colours and sizes and what to do when clicked
    '''

    pos = pygame.mouse.get_pos()  # pygame methods to recognize that the mouse is clicked
    # pygame methods to recognize that the mouse is clicked
    click = pygame.mouse.get_pressed()
    if x < pos[0] < x + w and y < pos[1] < y + 40:  # it is the x and y positions of the mouse
        # the pygame.draw.rect x,y,w, and 40 are the dimensions.
        pygame.draw.rect(src.display, hover_colour, [
                         x, y, w, 40])  # change the hover colour
        # if someone clicked and there is an action associated with that button
        if click[0] == 1 and action != None:
            action()  # do that action
    else:  # or
        pygame.draw.rect(src.display, button_colour, [
                         x, y, w, 40])  # just draw and hold it
    font = pygame.font.Font(src.bitterfont, 15)  # font object
    # renders the text on the secreen
    text = font.render(name, True, white)
    text_rect = text.get_rect(center=((x + (x + w)) / 2, (y + (y + 40)) / 2))
    src.display.blit(text, text_rect)


def ButtonWithReturn(name, x, y, w, dist, val=None):
    '''
    this function creates the button on the screen but with a return value
    same as the function above essentially
    '''

    # pygame method for mouse. it gets the mouse's position (x,y) on the screen
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()  # pygame method to see if it is pressed
    if x < pos[0] < x + w and y < pos[1] < y + 40:  # if mouse is on the button
        pygame.draw.rect(src.display, hover_colour, [
                         x, y, w, 40])  # change the hover colour
        if click[0] == 1:  # if clicked while it is on
            return val  # do what the button calls for
    else:  # if not
        pygame.draw.rect(src.display, button_colour, [
                         x, y, w, 40])  # just draw it
    font = pygame.font.Font(src.bitterfont, 14)  # font object
    # renders the text on the secreen
    text = font.render(name, True, white)
    text_rect = text.get_rect(center=((x + (x + w)) / 2, (y + (y + 40)) / 2))
    src.display.blit(text, text_rect)  # shows the text
    return 0  # return 0 from the button function


def Description(description):
    '''
    this function displays the descriptions of the algorithms
    it takes a string object and displays it on the screen
    it also adds the back button in case the user needs to go back
    '''

    show = True
    while show:
        src.display.fill(black)  # fills with black
        # src.display.blit(dscbg,(0,0))  ## this is a pygame method allowing us to paste objects into the screen. it takes pixel location and the object as arguments
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():  # setting the initial exit from the loop
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # tells the computer to recognise if a keybord key is pressed
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.
        AddDesc(description, (5, 5), white)  # displays the text
        back = ButtonWithReturn("Back", 650, 500, 100, 30, 1)  # back button
        if back > 0:  # if back is clicked
            show = False  # do not show
        pygame.display.flip()  # updates the screen every turn
        src.clock.tick(60)  # will not run more than frames per second


def AddDesc(text, pos, color=white):
    '''
    created a new modified addtext function for the descriptions
    this is because pygame does not support multiple line string objects
    '''

    subheads = [
        "Brute-Force Algorithm:", "Summary:", "Order List:", "Efficiency:",
        "Bentley-Ottmann Algorithm:", "Shamos-Hoey Algorithm:", "Event Queue:"]
    font = pygame.font.Font(src.bitterfont, 11)  # creating font with size
    # creating font pygame text object with size, colour and text
    # fixing the subheading font size
    font2 = pygame.font.Font(src.bitterfont, 12)
    font2.set_underline(1)  # making subheadings underlined
    desrbt = []  # creating a placeholder to see hold every line in a list
    for line in text:
        if line in subheads:
            # need to save each line so that they can be literated later on for the purple lines
            desrbt.append(font2.render(line, True, button_colour))
        else:
            # need to save each line so that they can be literated later on
            desrbt.append(font.render(line, True, color))
    # displaying text on the screen, pos is the position of where it should appear
    # this is an iterative algorithm which will allow me to display each line
    for i in range(len(desrbt)):
        src.display.blit(desrbt[i], (pos[0], pos[1] + (i * 11) + (11 * i)))


def AddText(text, pos, color=white):
    '''
    add texts to the screen
    takes text which is a string object as an argument
    '''

    font = pygame.font.Font(src.bitterfont, 16)  # creating font with size
    # creating font pygame text object with size, colour and text
    renderedText = font.render(text, True, color)
    # displaying text on the screen, pos is the position of where it should appear
    src.display.blit(renderedText, pos)


def InsertNumber(text):
    '''
    this function takes an input of string for the algorithm efficieny function
    '''

    pygame.display.set_caption(text)
    inpText = ""  # empty placeholder
    enter = True  # enable enter
    while enter:  # starting the algorithm
        # pygame method to fill the screen, takes colours and a display object
        src.display.fill(black)
        # src.display.blit(dscbg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():  # again iterating as an important pygame method to set the features
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            if event.type == pygame.KEYUP:  # Here is to tell the computer to recognise if a keybord key is pressed
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.
            if event.type == pygame.KEYDOWN:  # if a key is pressed
                if event.key == pygame.K_RETURN:  # and if this key is enter
                    enter = False  # enter changes the status of true to false and ends the loop, you entered what you wanted
                elif event.key == pygame.K_BACKSPACE:  # if backspace is pressed
                    # backspace deletes the last letter of the input. this [:-1] called slicing
                    inpText = inpText[:-1]
                else:  # if none of this happened
                    inpText += event.unicode  # takes care of capslocks and shiftkeys
        AddText(text, (128, 220), white)  # displaying the text
        # displaying the text
        pygame.draw.rect(src.display, white, (290, 215, 250, 40))
        AddText(inpText, (295, 225), black)  # displaying the text
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 15 frames per second
        src.clock.tick(60)  # 15 frames per second
    return inpText
