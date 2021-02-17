# lines 1-4 imports the necessary libraries
import pygame
import os
import random
import math
import sys

import hlp
import intro
import dsb  # this is the last module with the description files


'''
declaring some global variables beacause in Python, we can set global variables that can be used in future functions
setting the variables false allows us to activate them in the game loop, or vice versa
creating empty lists as global variables allows us to access them outside of the functions they are being used
'''

cursor = False
randomLine = False
randomTimer = True
run = False
stop = False
start = False
clear = False
lines = []
colours = []
brutecolours = []
points = []
line_name = []
intersect_name = []
orderList = []

# initialise Pygame library, it is necessary in Programs using Pygame
pygame.init()

line_colour = pygame.Color(50, 50, 120)

# initialise window size at 800 * 550 with a caption
display = pygame.display.set_mode((1280, 550), pygame.FULLSCREEN |
                                  pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Line Segment Intersection Visualisation Tool")
# frames per second determines how many frames should be refreshed per second
clock = pygame.time.Clock()
# load cursor image for inserting line, os.path method points to the path of the cursor image file
pointer = pygame.image.load(os.path.join("resources", "pointer.png"))

# BitterFont text used throughout the program
bitterfont = os.path.abspath("resources/bitterfont.otf")


def AddPoints(p):
    '''
    this function takes a point as an argument, then append the 'points' list by using iteration over every item in the points list
    if that point is already in the list, the function does nothing
    if not, the function appends the points list object with the argument p.
    '''

    # make sure we're referring to the points object outside of this function
    global points
    # step through all the current items in points list
    for point in points:
        # is p the same as the current item
        if point == p:
            # if so, stop stepping through and drop out of this function without doing anything
            return
    # if we get here, we've gone through the whole list without a match
    # add the new point to the list
    points.append(p)


def TransValue(OldValue, oldMax, oldMin):
    '''
    scales the data
    '''
    newMax = 350
    newMin = 0
    OldRange = (oldMax - oldMin)
    NewRange = (newMax - newMin)
    NewValue = int((((OldValue - oldMin) * NewRange) / OldRange) + newMin)
    return NewValue


def GenerateRandomLine():
    '''
    generates random lines
    '''

    x1 = random.randrange(51, 450)  # randomly choses between 51 and 450
    y1 = random.randrange(50, 450)  # randomly choses between 50 and 450
    x2 = random.randrange(51, 450)  # randomly choses between 51 and 450
    y2 = random.randrange(50, 450)  # randomly choses between 50 and 450
    # calls for the AddNewLine function to create new lines
    AddNewLine([(x1, y1), (x2, y2)])


def CheckIntersect(p1, p2, q1, q2):
    '''
    this function determines if two lines intersect
    p1,p2, q1, q2 are start and end points of the lines
    it uses Cramer's rule of linear algebra to determine whether lines intersect
    '''

    # getting the distance between end points by accessing the second index of the p1 and p2 list items and appointing it to variable a1
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]  # same as above but accessing to the first index
    c1 = a1 * p1[0] + b1 * p1[1]
    a2 = q2[1] - q1[1]  # same as a1 but for q instead of p
    b2 = q1[0] - q2[0]  # same as b1 but for q instead of p
    c2 = a2 * q1[0] + b2 * q1[1]
    d = (a1 * b2 - a2 * b1)  # finding the determinant
    if d == 0:  # paralel or same line, determinant is zero
        return
    x = int((c1 * b2 - c2 * b1) / d)  # solving for x
    y = int((a1 * c2 - a2 * c1) / d)  # solving for y
    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
        if min(q1[0], q2[0]) <= x <= max(q1[0], q2[0]) and min(q1[1], q2[1]) <= y <= max(q1[1], q2[1]):
            # found the intersection by checking solution of x and y for existing points
            AddPoints((x, y))
            return True  # returns true
    return False


def BruteForceMain():
    '''
    this function is the Brute-Force Algorithm function with main display loop
    '''

    # acessing the global variables
    global cursor, lines, brutecolours, points, randomLine, randomTimer, run, stop, clear, intersect_name
    # first the lines are accessing necessary global variables
    global display, line_name, orderList
    pygame.display.set_caption("Brute-Force Algorithm")  # adding a caption
    # setting the display for the algorithm
    display = pygame.display.set_mode((1280, 550), pygame.FULLSCREEN)
    cursor = False  # until while true line, which is the main loop, lines below creating the default values
    randomLine = False  # again the default placeholder for the randomline
    clickedPos = []  # default place holder value for position
    orderList = []  # same for the order list, empty now all these values will be appended during the game loop
    efficiency = 0  # default place holder value for algorithm efficieny
    eventQueue = []  # event queue place holder, empty now
    back = 0  # if this becomes one, you go back
    while True:  # starting the game loop
        # pygame method to fill the screen, takes colours and a display object
        display.fill((0, 0, 0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            # Here is to tell the computer to recognise if a keybord key is pressed.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.

            '''
            if mouse clicked on the below coordinates, create a line
            pygame GUI property detecting when mouse click is on
            MOUSEBUTTONDOWN and MOUSEBUTTONUP should be used as a small loops so that the computer can understand when that instance of the mouse movement is over
            '''

            if cursor == True and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # pygame method defining the button in the GUI
                    mouse_pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # pygame property pos[0] is the mouse cursor in the X axis and pos[1] is the Y axis
                    if 50 < pos[0] < 450 and 50 < pos[1] < 450:
                        # here it adds the clicked postion corresponding to the positon of the mouse
                        clickedPos.append(pos)
            if event.type == pygame.MOUSEBUTTONUP:
                randomTimer = True  # turning the random from false to true so the timer can activate
        for i in range(0, 41):  # choosing coordinates for drawing, exiting the previous iteration, range (0,41) goes between 0 and 40
            # for the pygame method of drawing below, we need to determine the position on the screen as a tuple object
            pos = i * 10 + 50
            # pygame method, takes display, colour, and positions of where the lines start and end. i.e, starts in (50,pos) ends in (450,pos), 1 at the end is the width of the line
            pygame.draw.line(display, line_colour, (50, pos), (450, pos), 1)
            # same as above but takes pos as y, by doing so and iterating through the range, you cover all the plane
            pygame.draw.line(display, line_colour, (pos, 50), (pos, 450), 1)
        i = 0  # index determining for data structure, taking it back to zero
        for line in lines:  # iterating through lines which is a global variable for the priority queue aka eventQueue

            '''
            having [i] next to colour allows me to colour each line differently
            each line has tuple object in the global variable
            line[0] accesses the nth item's first coordinates in the iteration and drawing ends in the line[1], nth item's second object
            '''

            pygame.draw.line(display, brutecolours[i], line[0], line[1], 1)
            # calling the hlp.AddText function that was created before in the script
            hlp.AddText(line_name[i], line[0])
            i += 1  # remember, need to increase the index.
        orderList = []  # creating the placeholder list object to secure future items
        i = 50
        while i < 450:  # this is the start of the brute force algorithm, it uses a try and error methods by iterating through all existing points
            j = 0  # that's why it enumarates through all possible points on the screen to go through, thus, I have the second while loop here
            for point in points:  # 450 is the max number of points on the display, therefore, indexing goes until 450 i < 450
                if point[0] == i:  # while trying all the points, if the x value of the selected point intersects with the given index
                    # then add it to the orderList
                    orderList.append(intersect_name[j])
                j += 1  # as before, increse indexing values by one
            i += 1  # as before in the previous function, increase the index by one
        n = len(lines)  # finding out how many lines are drawn already
        for point in points:  # iterating over the points
            # use this pygame method to draw a small circle where the lines intersect
            pygame.draw.circle(display, hlp.red, point, 3)
        efficiency = n * n  # this is the efficieny formula for the brute-force algorithm
        if cursor == True:  # arrange the mouse cursors
            pygame.mouse.set_visible(False)
            pos = pygame.mouse.get_pos()  # this is a pygame method for mouse cursor
            # the cursor with the existing pointer image, pygame method called display.blit which adds a spirit to the screen
            display.blit(pointer, pos)
            # if you clicked on the screen, this checks the number of clicks and starts drawing
            if len(clickedPos) > 0:
                # again pygame method to draw, if clicked then draw this
                pygame.draw.circle(display, hlp.white, clickedPos[0], 2)
                # if clicked then draw this
                pygame.draw.line(display, hlp.white, clickedPos[0], pos, 1)
            if len(clickedPos) >= 2:  # if the cursor is in a positon which is longer than 2 that can draw lines, if you clicked on more or equal to 2 times, which means begining and end for the lines
                # then add lines according to the points saved in the clickedPos object. [0] is the begining index and clickedPos[1] is the ending index.
                AddNewLine([clickedPos[0], clickedPos[1]])
                cursor = False  # disable the cursor after drawing
                clickedPos = []  # empty the placeholder after drawing the line
        else:  # now you are entering into the scene of mouse action
            # again pygame GUI method enabling mouse action on the screen to interact
            pygame.mouse.set_visible(True)
        if randomLine == True:  # if mouse clicked on the randomline
            GenerateRandomLine()  # then create a random line, calling the existing function
            randomLine = False  # turn it off after drawing so it would not keep drawing forever
            randomTimer = False  # and stop the timer so it won't go forever
        if clear == True:  # clear action is enabled, clear back all the placeholders to default
            lines = []  # everything is back to the default value
            colours = []  # everything is back to the default value
            brutecolours = []  # everything is back to the default value
            points = []  # everything is back to the default value
            orderList = []  # everything is back to the default value
            efficiency = 0  # everything is back to the default value
            eventQueue = []  # everything is back to the default value
            intersect_name = []  # everything is back to the default value
            line_name = []  # everything is back to the default value
            clear = False

            '''
            adding text positions and texts for the frame
            calling existing functions, giving text, position and when applicable the action
            my helper functions are button and addtext that help me in my larger script.
            '''

        # adding the texts and buttons as above function
        hlp.AddText("(0,0)", (30, 25))
        hlp.AddText("(50,0)", (430, 25))
        hlp.AddText("(0,50)", (30, 450))
        hlp.AddText("(50,50)", (430, 450))
        hlp.Button("Clear", 200, 5, 100, 30, ClearActive)
        hlp.Button("Random Segment", 50, 500, 180, 30, RandomActive)
        hlp.Button("Insert Segment", 280, 500, 180, 35, CursorActive)
        hlp.Button("Exit", 500, 5, 100,
                   30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break
        # calls the helper function
        nxt = hlp.ButtonWithReturn("Next", 700, 5, 100, 30, 1)
        if nxt > 0:  # so if the next button is clicked
            # calls for the description function
            hlp.Description(dsb.bf_desc)
        # pygame method to draw an object
        pygame.draw.rect(display, line_colour, [500, 50, 750, 490], 2)
        # adding the text on the given location
        hlp.AddText("Brute-Force Algorithm", (520, 70))
        # adding the text on the given location.
        hlp.AddText("Order List:", (520, 120))
        # creating indexing i and x, y positions to display on the GUI, this is an important way to assign values to a tuplae object
        i, o_x, o_y = 0, 540, 150

        '''
        iterating through the existing values in the orderList.
        because we don't want the texts to overlap on the screen
        most of the numbers below are finetuning to prevent overlapping of the texts for the order list and the eventqueue list.
        '''

        for val in orderList:  # going through the items in the orderList
            # calling the helper function to add the text of the values in the orderList
            hlp.AddText(val, (o_x, o_y), (255, 255, 255))
            o_x += 50  # moving 50 pix on the x axis for each item
            i += 1  # going to next item by increasing the index
            if i % 14 == 0:  # check if the line ends
                o_x = 540  # text is on the edge, there no more horizontol space
                o_y += 20  # # go to the next line by adding 20 to the y axis
        # adding the text on the given location
        hlp.AddText("Efficiency O(n*n):", (520, 480))
        # adding the text on the given location
        hlp.AddText(str(efficiency), (540, 505), (255, 255, 255))
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(90)
    intro.Introduction2()  # calls back the introduction function


def BentleyMain():
    '''
    this function is the Bentley-Ottmann Algorithm function with main display loop
    '''

    global cursor, lines, colours, points, randomLine, randomTimer, run, stop, clear, intersect_name
    # first the lines are accessing necessary global variables
    global display, line_name, orderList
    pygame.display.set_caption("Bentley-Ottmann Algorithm")  # adding a caption
    # setting the display for the algorithm
    display = pygame.display.set_mode((1280, 550), pygame.FULLSCREEN)
    cursor = False    # until while true line, which is the main loop, lines below creating the default values
    randomLine = False  # again the default placeholder for the randomline
    clickedPos = []  # default place holder value for position
    efficiency = 0  # default place holder value for algorithm efficieny
    eventQueue = []  # event queue place holder, empty now
    orderList = []  # same for the order list, empty now all these values will be appended during the game loop
    x = 50  # location of the x value on the screen
    back = 0  # if this becomes one, you go back
    while True:  # starting the game loop
        # pygame method to fill the screen. takes colours and a display object
        display.fill((0, 0, 0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            # Here is to tell the computer to recognise if a keybord key is pressed.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.

            '''
            if mouse clicked on the below coordinates, create a line
            pygame GUI property detecting when mouse click is on
            MOUSEBUTTONDOWN and MOUSEBUTTONUP should be used as a small loops so that the computer can understand when that instance of the mouse movement is over
            '''

            if cursor == True and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # pygame method defining the button in the GUI
                    mouse_pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # pygame property pos[0] is the mouse cursor in the X axis and pos[1] is the Y axis
                    if 50 < pos[0] < 450 and 50 < pos[1] < 450:
                        # here it adds the clicked postion corresponding to the positon of the mouse
                        clickedPos.append(pos)
            if event.type == pygame.MOUSEBUTTONUP:
                randomTimer = True  # turning the random from false to true so the timer can activate
        for i in range(0, 41):  # choosing coordinates for drawing, exiting the previous iteration, range (0,41) goes between 0 and 40
            # for the pygame method of drawing below, we need to determine the position on the screen as a tuple object
            pos = i * 10 + 50
            # pygame method, takes display, colour, and positions of where the lines start and end. i.e, starts in (50,pos) ends in (450,pos), 1 at the end is the width of the line
            pygame.draw.line(display, line_colour, (50, pos), (450, pos), 1)
            # same as above but takes pos as y, by doing so and iterating through the range, you cover all the plane
            pygame.draw.line(display, line_colour, (pos, 50), (pos, 450), 1)
        i = 0  # index determining for data structure, taking it back to zero
        for line in lines:  # iterating through lines which is a global variable for the priority queue aka eventQueue

            '''
            having [i] next to colour allows me to colour each line differently
            each line has tuple object in the global variable
            line[0] accesses the nth item's first coordinates in the iteration and drawing ends in the line[1], nth item's second object
            '''

            pygame.draw.line(display, colours[i], line[0], line[1], 1)
            # calling the addText function that was created before in the script
            hlp.AddText(line_name[i], line[0])

            '''
            nested indexing, as I am accessing the first item of the first item in the line object which is in the lines global variable
            result of this nested indexing should access a point of  x- coordinated saved in a tuple
            '''

            if x == line[0][0]:
                # if that begining point of the line's x coordinates equals to the preset x, then append the queue list with the name of this line
                eventQueue.append(line_name[i])
            if x == line[1][0]:  # again the nested indexing
                # removes the line from the queue if the end of the line's x coordinates equals to x variable
                eventQueue.remove(line_name[i])
            # increasing the index number at the end of the iteration loop so I can access the other items saved
            i += 1
        if stop == True:  # tells to stop if stop is clicked
            run = False  # turns off the run, if it is stop, then run must be false
            x = 50  # set x to default
            # if I don't make the stop false at the end of this clause, there would be a logic error as stop must be false after it was used otherwise, it will be true forever
            stop = False
        if run == True:  # tells it to start if run is clicked
            cursor = False  # when it is running cursor can't draw any newlines
            randomLine = False  # again no new random lines too
            x += 1  # since I am scanning, the x value should scan the screen pixel after pixel, thus, adding 1 to the x value
            # this draws the scan line on the screen
            pygame.draw.line(display, hlp.red, (x, 50), (x, 450), 1)
            # j and k are placeholders to keep track of the index
            j = 0
            k = 0
            # iterating through points to draw the intersection circle in the run
            for point in points:
                # if the first item's x value is smaller or equal to the present x variable
                if point[0] <= x:
                    # use this pygame method to draw a small circle where the lines intersect
                    pygame.draw.circle(display, hlp.white, point, 3)
                    k += 1  # increase the placeholders value
                if point[0] == x:  # if x value is already equal to the preset x
                    # then append the orderList with the name of the intersection
                    orderList.append(intersect_name[j])
                j += 1  # increase the j once more
            if k > 0:  # so it means there is already an intersection
                n = len(lines)  # check how many lines were drawn already
                if n > 0:  # if the number of lines are more than 0, it means that there are existing lines
                    # measure the algorithm's speed
                    efficiency = (n + k) * math.log10(n)

            '''
            since the display stars from 50th pixel, I substract 50 from that, and the script uses //8 as divide without remainers to convert the x values pixel to coordinates
            this is so it can be used to name the incident of intersection
            '''

            c = (x - 50) // 8
            # adding the text as well for the intersection
            hlp.AddText("(X, Y) = (" + str(c) + ", 0)",
                        (200, 470), (255, 255, 255))
        if cursor == True:  # arrange the mouse cursors
            pygame.mouse.set_visible(False)
            pos = pygame.mouse.get_pos()  # this is a pygame method for mouse cursor
            # the cursor with the existing pointer image, pygame method called display.blit which adds a spirit to the screen
            display.blit(pointer, pos)
            # if you clicked on the screen, this checks the number of clicks and starts drawing
            if len(clickedPos) > 0:
                # again pygame method to draw, if clicked then draw this
                pygame.draw.circle(display, hlp.white, clickedPos[0], 2)
                # if clicked then draw this
                pygame.draw.line(display, hlp.white, clickedPos[0], pos, 1)
            if len(clickedPos) >= 2:  # if the cursor is in a positon which is longer than 2 that can draw lines, if you clicked on more or equal to 2 times, which means begining and end for the lines
                # then add lines according to the points saved in the clickedPos object. [0] is the begining index and clickedPos[1] is the ending index.
                AddNewLine([clickedPos[0], clickedPos[1]])
                cursor = False  # disable the cursor after drawing
                clickedPos = []  # empty the placeholder after drawing the line
        else:  # now you are entering into the scene of mouse action
            # again pygame GUI method enabling mouse action on the screen to interact
            pygame.mouse.set_visible(True)
        if randomLine == True:  # if mouse clicked on the randomline
            GenerateRandomLine()  # then create a random line, calling the existing function
            randomLine = False  # turn it off after drawing so it would not keep drawing forever
            randomTimer = False  # and stop the timer so it won't go forever
        if run == True and x > 450:  # if run function is enabled however the x value is out of the screen
            x = 50  # put x back to the default of 50
            run = False  # and disable the run
        if clear == True:  # clear action is enabled, clear back all the placeholders to default
            lines = []  # everything is back to the default value
            colours = []  # everything is back to the default value
            points = []  # everything is back to the default value
            orderList = []  # everything is back to the default value
            efficiency = 0  # everything is back to the default value
            eventQueue = []  # everything is back to the default value
            intersect_name = []  # everything is back to the default value
            line_name = []  # everything is back to the default value
            x = 50  # everything is back to the default value
            run = False  # everything is back to the default value
            clear = False  # everything is back to the default value

            '''
            adding text positions and texts for the frame
            calling existing functions, giving text, position and when applicable the action
            my helper functions are button and addtext that help me in my larger script
            '''

        # adding text positions and texts for the frame
        hlp.AddText("(0,0)", (30, 25))
        hlp.AddText("(50,0)", (430, 25))
        hlp.AddText("(0,50)", (30, 450))
        hlp.AddText("(50,50)", (430, 450))
        # drawing buttons and determining positions
        hlp.Button("Run", 80, 5, 100, 35, RunActive)
        hlp.Button("Stop", 200, 5, 100, 35, StopActive)
        hlp.Button("Clear", 320, 5, 100, 30, ClearActive)
        hlp.Button("Random Segment", 50, 500, 180, 30, RandomActive)
        hlp.Button("Insert Segment", 280, 500, 180, 35, CursorActive)
        hlp.Button("Exit", 500, 5, 100,
                   30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break
        # calls the helper function
        nxt = hlp.ButtonWithReturn("Next", 700, 5, 100, 30, 1)
        if nxt > 0:  # so if the next button is clicked
            # calls for the description function
            hlp.Description(dsb.bo_desc)
            text = ["If you are learning to play, it is recommended",  # and displays this text
                    "you chose your own starting area."]
        # pygame method to draw an object
        pygame.draw.rect(display, line_colour, [500, 50, 750, 490], 2)
        # adding the text on the given location
        hlp.AddText("Bentley-Ottmann Algorithm", (520, 70))
        # adding the text on the given location
        hlp.AddText("Event Queue:", (520, 120))
        # creating indexing i and x, y positions to display on the GUI, this is an important way to assign values to a tuplae object
        i, o_x, o_y = 0, 540, 150

        '''
        iterating through the existing values in the eventQueue
        because we don't want the texts to overlap on the screen
        most of the numbers below are finetuning to prevent overlapping of the texts for the order list and the eventqueue list
        '''

        for val in eventQueue:
            # val is each text saved in the eventQueue, and these values are not to overlap on the screen
            hlp.AddText(val, (o_x, o_y), (255, 255, 255))
            o_x += 30  # therefore for each value, I'm adding +30 for each one
            i += 1  # adding one to the index to access to the next item
            if i % 23 == 0:  # 23rd item appears on the righest point on the screen so for the next one you need to go on the y axis
                o_x = 540  # text is on the edge, there no more horizontol space
                # text needs to appear on the next line, so adding 20 onto the y axis, vertical move
                o_y += 20
        hlp.AddText("Order List:", (520, 200))  # adding the text
        i, o_x, o_y = 0, 540, 230
        for val in orderList:  # same as above iteration but for the order list this time
            hlp.AddText(val, (o_x, o_y), (255, 255, 255))
            o_x += 50  # adding to x axis
            i += 1  # increasing the index
            if i % 14 == 0:  # this is 14, because the text has less horizontal space to appear.
                o_x = 540  # reached the end of the line
                o_y += 20  # go to the next line, move vertical, thus adding to the y value
        # adding the text on the given location
        hlp.AddText("Efficiency O((n+k)logn):", (520, 480))
        # adding the text on the given location
        hlp.AddText(str(efficiency), (540, 505), (255, 255, 255))
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(30)
    intro.Introduction2()  # calls back the introduction function


def ShamosHoeyMain():
    '''
    this function is the Shamos-Hoey Algorithm function with main display loop
    '''

    global cursor, lines, colours, points, randomLine, randomTimer, run, stop, clear, intersect_name
    global display, line_name  # first the lines are accessing necessary global variables
    pygame.display.set_caption("Shamos-Hoey Algorithm")  # adding a caption
    # setting the display for the algorithm
    display = pygame.display.set_mode((1280, 550), pygame.FULLSCREEN)
    cursor = False  # until while true line, which is the main loop, lines below creating the default values
    randomLine = False  # again the default placeholder for the randomline
    clickedPos = []  # default place holder value for position
    firstPoint = None  # first intersection point identified
    efficiency = 0  # default place holder value for algorithm efficieny
    eventQueue = []  # event queue place holder, empty now
    run = False
    x = 50  # location of the x value on the screen
    back = 0  # if this becomes one, you go back
    while True:  # starting the game loop
        # pygame method to fill the screen, takes colours and a display object
        display.fill((0, 0, 0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            # Here is to tell the computer to recognise if a keybord key is pressed.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.

                '''
                if mouse clicked on the below coordinates, create a line
                pygame GUI property detecting when mouse click is on
                MOUSEBUTTONDOWN and MOUSEBUTTONUP should be used as a small loops so that the computer can understand when that instance of the mouse movement is over
                '''

            if cursor == True and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # pygame method defining the button in the GUI
                    mouse_pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # pygame property pos[0] is the mouse cursor in the X axis and pos[1] is the Y axis
                    if 50 < pos[0] < 450 and 50 < pos[1] < 450:
                        # here it adds the clicked postion corresponding to the positon of the mouse
                        clickedPos.append(pos)
            if event.type == pygame.MOUSEBUTTONUP:
                randomTimer = True  # turning the random from false to true so the timer can activate
        for i in range(0, 41):  # choosing coordinates for drawing, exiting the previous iteration, range (0,41) goes between 0 and 40
            # for the pygame method of drawing below, we need to determine the position on the screen as a tuple object
            pos = i * 10 + 50
            # pygame method, takes display, colour, and positions of where the lines start and end. i.e, starts in (50,pos) ends in (450,pos), 1 at the end is the width of the line
            pygame.draw.line(display, line_colour, (50, pos), (450, pos), 1)
            # same as above but takes pos as y, by doing so and iterating through the range, you cover all the plane
            pygame.draw.line(display, line_colour, (pos, 50), (pos, 450), 1)
        i = 0  # index determining for data structure, taking it back to zero
        for line in lines:  # iterating through lines which is a global variable for the priority queue aka eventQueue

            '''
            having [i] next to colour allows me to colour each line differently
            each line has tuple object in the global variable
            line[0] accesses the nth item's first coordinates in the iteration and drawing ends in the line[1], nth item's second object
            '''

            pygame.draw.line(display, colours[i], line[0], line[1], 1)
            # calling the addText function that was created before in the script
            hlp.AddText(line_name[i], line[0])

            '''
            nested indexing, as I am accessing the first item of the first item in the line object which is in the lines global variable
            result of this nested indexing should access a point of  x- coordinated saved in a tuple
'           '''

            if x == line[0][0]:
                # if that begining point of the line's x coordinates equals to the preset x, then append the queue list with the name of this line
                eventQueue.append(line_name[i])
            if x == line[1][0]:  # again the nested indexing
                # removes the line from the queue if the end of the line's x coordinates equals to x variable
                eventQueue.remove(line_name[i])
            # increasing the index number at the end of the iteration loop so I can access the other items saved
            i += 1
        if stop == True:  # tells to stop if stop is clicked
            run = False  # turns off the run, if it is stop, then run must be false
            x = 50  # set x to default
            # if I don't make the stop false at the end of this clause, there would be a logic error as stop must be false after it was used otherwise, it will be true forever
            stop = False
            eventQueue = []  # empties the eventQueue
        if run == True:  # tells it to start if run is clicked
            cursor = False  # when it is running cursor can't draw any newlines
            randomLine = False  # again no new random lines too
            x += 1  # since I am scanning, the x value should scan the screen pixel after pixel, thus, adding 1 to the x value
            # this draws the scan line on the screen
            pygame.draw.line(display, hlp.red, (x, 50), (x, 450), 1)
            # iterating through points to draw the intersection circle in the run
            for point in points:
                # if the first item's x value is smaller or equal to the present x variable
                if point[0] == x:
                    firstPoint = point  # having a designated first point variable
                    run = False  # setting variables to default.
                    x = 50  # setting variables to default.
                    eventQueue = []  # setting variables to default.
                    efficiency = 0  # setting variables to default.
                    break  # break the loop
            n = len(lines)  # number of existing lines
            if n > 0:  # if the number of lines are more than 0, it means that there are existing lines
                efficiency = n * math.log10(n)  # measure the algorithm's speed

                '''
                since the display stars from 50th pixel, I substract 50 from that, and the script uses //8 as divide without remainers to convert the x values pixel to coordinates
                this is so it can be used to name the incident of intersection
                '''

            c = (x - 50) // 8
            # adding the text as well for the intersection
            hlp.AddText("(X, Y) = (" + str(c) + ", 0)", (200, 470),
                        hlp.white)  # adding the intersection
        if firstPoint != None:  # if there is a first point
            # use this pygame method of drawing a circle.
            pygame.draw.circle(display, hlp.white, firstPoint, 3)
        if cursor == True:  # arrange the mouse cursors
            pygame.mouse.set_visible(False)
            pos = pygame.mouse.get_pos()  # this is a pygame method for mouse cursor
            # the cursor with the existing pointer image, pygame method called display.blit which adds a spirit to the screen
            display.blit(pointer, pos)
            # if you clicked on the screen, this checks the number of clicks and starts drawing
            if len(clickedPos) > 0:
                pygame.draw.circle(display, hlp.white, clickedPos[0], 2)
                # if clicked then draw this
                pygame.draw.line(display, hlp.white, clickedPos[0], pos, 1)
            if len(clickedPos) >= 2:  # if the cursor is in a positon which is longer than 2 that can draw lines, if you clicked on more or equal to 2 times, which means begining and end for the lines
                # then add lines according to the points saved in the clickedPos object. [0] is the begining index and clickedPos[1] is the ending index.
                AddNewLine([clickedPos[0], clickedPos[1]])
                cursor = False  # disable the cursor after drawing
                clickedPos = []  # empty the placeholder after drawing the line
        else:  # now you are entering into the scene of mouse action
            # again pygame GUI method enabling mouse action on the screen to interact
            pygame.mouse.set_visible(True)
        if randomLine == True:  # if mouse clicked on the randomline
            GenerateRandomLine()  # then create a random line, calling the existing function
            randomLine = False  # turn it off after drawing so it would not keep drawing forever
            randomTimer = False  # and stop the timer so it won't go forever
        if run == True and x > 450:  # if run function is enabled however the x value is out of the screen
            x = 50  # put x back to the default of 50
            run = False  # and disable the run
        if clear == True:  # clear action is enabled, clear back all the placeholders to default
            lines = []  # everything is back to the default value
            colours = []  # everything is back to the default value
            points = []  # everything is back to the default value
            efficiency = 0  # everything is back to the default value
            firstPoint = None  # everything is back to the default value
            eventQueue = []  # everything is back to the default value
            intersect_name = []  # everything is back to the default value
            line_name = []  # everything is back to the default value
            x = 50  # everything is back to the default value
            run = False  # everything is back to the default value
            clear = False  # everything is back to the default value

            '''
            adding text positions and texts for the frame
            calling existing functions, giving text, position and when applicable the action
            my helper functions are button and addtext that help me in my larger script.
            '''

        # adding text positions and texts for the frame
        hlp.AddText("(0,0)", (30, 25))
        hlp.AddText("(50,0)", (430, 25))
        hlp.AddText("(0,50)", (30, 450))
        hlp.AddText("(50,50)", (430, 450))
        # drawing buttons and determining positions
        hlp.Button("Run", 80, 5, 100, 35, RunActive)
        hlp.Button("Stop", 200, 5, 100, 35, StopActive)
        hlp.Button("Clear", 320, 5, 100, 30, ClearActive)
        hlp.Button("Random Segment", 50, 500, 180, 30, RandomActive)
        hlp.Button("Insert Segment", 280, 500, 180, 35, CursorActive)
        hlp.Button("Exit", 500, 5, 100,
                   30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 900, 5, 100, 30, 1)
        if back > 0:  # if back has a value, which means it has been clicked, stop the bigger loop that we started, i.e. the game loop, and break the game loop
            break
        # calls the helper function
        nxt = hlp.ButtonWithReturn("Next", 700, 5, 100, 30, 1)
        if nxt > 0:   # so if the next button is clicked
            # calls for the description function
            hlp.Description(dsb.sh_desc)
        # pygame method to draw an object
        pygame.draw.rect(display, line_colour, [500, 50, 750, 490], 2)
        # adding caption, frame size, texts, buttons and their positions
        # adding the text on the given location
        hlp.AddText("Shamos-Hoey Algorithm", (520, 70))
        # adding the text on the given location
        hlp.AddText("Event Queue:", (520, 120))
        # creating indexing i and x, y positions to display on the GUI, this is an important way to assign values to a tuplae object
        i, o_x, o_y = 0, 540, 150

        '''
        iterating through the existing values in the eventQueue.
        because we don't want the texts to overlap on the screen
        most of the numbers below are finetuning to prevent overlapping of the texts for the order list and the eventqueue list.
        '''

        for val in eventQueue:
            # val is each text saved in the eventQueue, and these values are not to overlap on the screen
            # calling the helper function.
            hlp.AddText(val, (o_x, o_y), hlp.white)
            o_x += 30  # adding 30 to the x-axis for each item.
            i += 1  # adding one to the index to access to the next item
            if i % 23 == 0:  # 23rd item appears on the righest point on the screen so for the next one you need to go on the y axis
                o_x = 540  # text is on the edge, there no more horizontol space
                # text needs to appear on the next line, so adding 20 onto the y axis, vertical move
                o_y += 20  # go to the next line by adding 20 to the y axis
        # adding the text on the given location
        hlp.AddText("Efficiency O(nlogn):", (520, 200))
        # adding the text on the given location
        hlp.AddText(str(efficiency), (540, 230), hlp.white)
        # updates the screen every turn
        pygame.display.flip()
        # will not run more than 30 frames per second
        clock.tick(30)
    intro.Introduction2()  # calls back the introduction function


def Efficiency():
    '''
    this function compares the efficiency of the algorithms
    '''

    pygame.display.set_caption("Efficiency Comparison")
    display = pygame.display.set_mode(
        (1280, 550), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    n = 0  # number segment
    k = 0  # intersection
    posX1 = 180  # position to appear
    posX2 = 400  # position to appear
    posY = 20  # position to appear
    bPos = 450  # position to appear
    bo = 0  # bentley-ottmann placeholders
    bf = 0  # brute-force placeholders
    sh = 0  # shamos-hoey placeholders
    bog = 0  # bentley-Ottman placeholders
    bfg = 0  # brute-force placeholders
    shg = 0  # shamos-hoey placeholders
    while True:  # starting the initial loop with first game events, ie. quit and mouse button
        # starting the initial loop with first game events, ie. quit and mouse button
        display.fill((0, 0, 0))
        # display.blit(hlp.dscbg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        # again iterating as an important pygame method to set the features.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            # Here is to tell the computer to recognise if a keybord key is pressed.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.
            # starting the initial loop with first game events, i.e. quit and mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # pygame method defining the button in the GUI
                    pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # starting the initial loop with first game events, ie. quit and mouse button
                    if posX1 < pos[0] < posX1 + 130 and posY < pos[1] < posY + 60:
                        # getting the number of lines
                        lineTxt = hlp.InsertNumber("Line Number:")
                        if lineTxt != "":  # if the string is not empty
                            try:
                                # input gives string so this one turns it into an integer
                                n = int(lineTxt)
                            except:  # if that is not happening
                                n = 0  # make n equals to zero, this is a error-handling method by managing the possible error by wrong input, i.e. linetxt can't be converted to an integer
                    # same as above but for the intersect number
                    elif posX2 < pos[0] < posX2 + 170 and posY < pos[1] < posY + 60:
                        intersectTxt = hlp.InsertNumber("Intersect Number :")

                        if intersectTxt != "":
                            try:
                                k = int(intersectTxt)
                            except:
                                k = 0
                    if n > 0:
                        # using established algorithm efficiency calculation for every algorithm
                        bo = int((n + k) * math.log10(n))
                        bog = bo  # number to be used in the graph string
                        # using established algorithm efficiency calculation for every algorithm
                        bf = int(n * n)
                        bfg = bf  # number to be used in the graph string
                        # using established algorithm efficiency calculation for every algorithm
                        sh = int(n * math.log10(n))
                        shg = sh  # number to be used in the graph string
                        if bo > 350 or bf > 350 or sh > 350:  # multiply by 350 for later on to use for rectangle object below
                            m = max(bo, bf, sh)
                            bo = int((bo / m) * 350)
                            bf = int((bf / m) * 350)
                            sh = int((sh / m) * 350)
                        if bo == 0:  # handling zeros for graphs below
                            bo = 1  # handling zeros for graphs below
                        if bf == 0:  # handling zeros for graphs below
                            bf = 1  # handling zeros for graphs below
                        if sh == 0:  # handling zeros for graphs below
                            sh = 1  # handling zeros for graphs below
        # setting the texts and buttons
        hlp.Button("Insert Line", posX1, posY, 130, 30, None)
        hlp.Button("Insert Intersect", posX2, posY, 160, 30, None)
        hlp.AddText("Line: " + str(n), (600, 20), hlp.white)
        hlp.AddText("Intersect: " + str(k), (600, 50), hlp.white)
        hlp.AddText("BF", (180, 460), hlp.white)
        hlp.AddText("BO", (330, 460), hlp.white)
        hlp.AddText("SH", (480, 460), hlp.white)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (100, 100), (100, 500), 2)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (50, 450), (650, 450), 2)
        if bf > 0:  # comparing here which one is better, if bf exists
            # comparing here which one is better
            hlp.AddText(str(bfg), (165, bPos - bf - 30), hlp.white)
            pygame.draw.rect(display, hlp.button_colour, (165, bPos - bf, 50, bf)
                             )  # drawing a rectangular bar on the screen
        if bo > 0:  # comparing here which one is better, if bo exists
            # comparing here which one is better
            hlp.AddText(str(bog), (315, bPos - bo - 30), hlp.white)
            pygame.draw.rect(display, hlp.button_colour, (315, bPos - bo, 50, bo)
                             )  # drawing a rectangular bar on the screen
        if sh > 0:  # comparing here which one is better, if sh exists
            # comparing here which one is better
            hlp.AddText(str(shg), (465, bPos - sh - 30), hlp.white)
            # drawing a rectangular bar on the screen. # bPos- algorithm name determines the rectangle's dimensions
            pygame.draw.rect(display, hlp.button_colour,
                             (465, bPos - sh, 50, sh))
        # setting and drawing the next/back buttons
        hlp.Button("Exit", 350, 500, 100,
                   30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 650, 500, 100, 30, 1)
        if back > 0:
            break
        nxt = hlp.ButtonWithReturn("Next", 500, 500, 100, 30, 1)
        if nxt > 0:
            hlp.Description(dsb.effic_desc)
        pygame.display.flip()  # updates the screen every turn
        clock.tick(60)  # will not run more than 15 frames per second
    intro.Introduction2()  # calls back the introduction function


def Efficiency2():
    '''
    this function compares the efficiency of the algorithms
    '''

    pygame.display.set_caption("Efficiency Comparison")
    display = pygame.display.set_mode(
        (1280, 550), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    n = range(10, 1001)  # number segment
    bet = False
    posX1 = 180  # position to appear
    posX2 = 400  # position to appear
    posY = 20  # position to appear
    bPos = 450  # position to appear

    sheffc = [i * math.log10(i) for i in n] # it is a list comprehension method for sh algoritm efficiency.
    bfeffc = [i**2 for i in n] # it is a list comprehension method for bf algoritm efficiency.
    boeffc = [((i + (((i**2) - i) / 2)) * math.log10(i)) for i in n] # it is a list comprehension method for bo algoritm efficiency.

    topalg = sheffc + bfeffc + boeffc # here compiles all efficency into one list

    mx = max(topalg) # getting the max value from the list
    mn = min(topalg) # getting the min value from the list
    transsheffc = [TransValue(i, mx, mn) for i in sheffc] #here it starts a list comprehension to normalize the values for across three efficiencies
    transshefc2 = random.sample(transsheffc, 550) #then getting 550 values to represent equally across the pixels
    transshefc2.sort() # sorting in descending order
    shno = 0 #starting an index for iteration
    shpoints = [] #placeholder value

    for i in transshefc2[:200]:                              #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shpoints.append((100 + shno, 450 - int(i))) #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shno += 1 #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
    for i in transshefc2[200:349]: #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shpoints.append((100 + shno, 450 - (int(i + 2)))) #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shno += 1 #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
    for i in transshefc2[349:]: #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shpoints.append((100 + shno, 450 - (int(i + 4)))) #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.
        shno += 1 #here it uses indexing and iteration for creating display pixel points for sh algoritm. First one is the x value, other one is y value.

    transbfeffc = [TransValue(i, mx, mn) for i in bfeffc] # between lines 910 and 917, same as above but for bf algoritm
    transbfeffc2 = random.sample(transbfeffc, 550)
    transbfeffc2.sort()
    bfno = 0
    bfpoints = []
    for i in(transbfeffc2):
        bfpoints.append((100 + bfno, 450 - int(i)))
        bfno += 1

    transboeffc = [TransValue(i, mx, mn) for i in boeffc] # between lines 919 and 926, same as above but for bo algoritm
    transboeffc2 = random.sample(transboeffc, 550)
    transboeffc2.sort()
    bono = 0
    bopoints = []
    for i in(transboeffc2):
        bopoints.append((100 + bono, 450 - int(i)))
        bono += 1

    while True:  # starting the initial loop with first game events, ie. quit and mouse button
        # starting the initial loop with first game events, ie. quit and mouse button
        display.fill((0, 0, 0))
        # display.blit(hlp.dscbg,(0,0))
        # pygame method, iterates over the events in pygame to determine what we are doing with every event
        # again iterating as an important pygame method to set the features.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # this one quits
                pygame.quit()  # putting the quit pygame method
                exit()  # takes the user from GUI to the script for exiting
            # Here is to tell the computer to recognise if a keybord key is pressed.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:  # if that keyboard key is ESC
                    exit()  # call for the exit function.
            # starting the initial loop with first game events, i.e. quit and mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # pygame method defining the button in the GUI
                    pos = pygame.mouse.get_pos()  # displays the mouse position on the screen
                    # starting the initial loop with first game events, ie. quit and mouse button
                    if posX2 < pos[0] < posX2 + 170 and posY < pos[1] < posY + 60:
                        bet = True

        hlp.Button("Start", posX2, posY, 160, 30, None)
        hlp.AddText("Lines: 10, 100, 1000", (600, 20), hlp.white)
        hlp.AddText("10", (115, 460), hlp.white)
        hlp.AddText("100", (350, 460), hlp.white)
        hlp.AddText("1000", (650, 460), hlp.white)
        hlp.AddText("max", (50, 100), hlp.white)
        hlp.AddText("0", (50, 460), hlp.white)
        sidefont = pygame.font.Font(bitterfont, 16)
        sidetext = sidefont.render("Algorithm Efficiency", True, hlp.white)
        sidetext = pygame.transform.rotate(sidetext, 90)
        display.blit(sidetext, (70, 235))
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (100, 100), (100, 500), 2)
        # pygame method, takes display, colour, and positions of where the lines start and end
        pygame.draw.line(display, line_colour, (50, 450), (650, 450), 2)

        if bet:

            pygame.draw.lines(display, (62, 150, 81), False, bfpoints, 4)
            pygame.draw.lines(display, (255, 255, 0), False, shpoints, 4)
            pygame.draw.lines(display, (255, 0, 0), False, bopoints, 4)
            hlp.AddText("Brute Force", (750, 150), hlp.white)
            hlp.AddText("Bentley-Ottmann", (750, 250), hlp.white)
            hlp.AddText("Shamos-Hoey", (750, 350), hlp.white)
            pygame.draw.line(display, (62, 150, 81), (720, 160), (740, 160), 4)
            pygame.draw.line(display, (255, 0, 0), (720, 260), (740, 260), 4)
            pygame.draw.line(display, (255, 255, 0), (720, 360), (740, 360), 4)

            hlp.AddText("n=10;100;1000", (720, 390), hlp.white)
            hlp.AddText("Brute Force = " + str(round(bfeffc[9])) + "; " + str(
                round(bfeffc[499])) + "; " + str(round(bfeffc[989])), (720, 405), hlp.white)
            hlp.AddText("Bentley-Ottmann = " + str(round(boeffc[9])) + "; " + str(
                round(boeffc[499])) + "; " + str(round(boeffc[989])), (720, 420), hlp.white)
            hlp.AddText("Shamos-Hoey = " + str(round(sheffc[9])) + "; " + str(
                round(sheffc[499])) + "; " + str(round(sheffc[989])), (720, 435), hlp.white)

        hlp.Button("Exit", 350, 500, 100,
                   30, sys.exit)
        back = hlp.ButtonWithReturn("Back", 650, 500, 100, 30, 1)
        if back > 0:
            break
        nxt = hlp.ButtonWithReturn("Next", 500, 500, 100, 30, 1)
        if nxt > 0:
            hlp.Description(dsb.effic_desc)
        pygame.display.flip()  # updates the screen every turn
        clock.tick(60)  # will not run more than 15 frames per second
    intro.Introduction2()  # calls back the introduction function


def AddNewColour():
    '''
    this function selects random colours and appends the global colours variable
    used for adding random colour to each line
    '''

    global colours  # accessing the variable
    r = random.randrange(1, 255)  # choosing the red tone
    g = random.randrange(1, 255)  # choosing the green tone
    b = random.randrange(1, 255)  # choosing the blue tone
    randomColour = pygame.Color(r, g, b)  # appointing the colour
    colours.append(randomColour)  # appending the global variable


def AddNewLine(newLine):
    '''
    this function adds a new line to the list
    it iterates through the lines list item and checks whether they intersect
    if so, it appoints a name for the intersecting lines and appends the intersect lines list
    '''

    global lines, line_name, intersect_name
    name = str(1 + len(lines))  # appointing a name
    i = 0  # appointing default index for the coming iteration below
    for line in lines:
        # checking whether new line and existing line intersect
        status = CheckIntersect(newLine[0], newLine[1], line[0], line[1])
        if status:
            intsec_name = line_name[i] + "." + name  # appointing a name
            intersect_name.append(intsec_name)  # appending the list
        i += 1  # increasing the index by one
    l = newLine
    # indexing the newline's points and sorting from start to end in the next line
    if(newLine[0][0] > newLine[1][0]):
        l = [newLine[1], newLine[0]]
    lines.append(l)  # appending the new line
    line_name.append(name)  # appending the name of the new line.
    AddNewColour()
    ChangeColour()


def ChangeColour():
    '''
    this function changes the line colours to white for the brute force algorithm
    it iterates through the different lines and appoints a new colour for each line
    '''

    global intersect_name, colours, brutecolours
    brutecolours = colours[:]  # copies the colours variable
    for name in intersect_name:   # iterates through the items
        sp = name.split(".")  # splits the string object
        # appoints each splitted names to converted integer objects
        n1 = int(sp[0])
        n2 = int(sp[1])
        brutecolours[n1 - 1] = hlp.white  # making them white
        brutecolours[n2 - 1] = hlp.white  # making them white


def CursorActive():
    '''
    acessing and activating the cursor image to be used
    this is for when the user wishes to draw their own line segments
    '''

    global cursor
    cursor = True  # activating the cursor


def RandomActive():
    '''
    accessing the existing global variables of random timer and lines
    if random timer is on create random lines
    this activates the action for the button, i.e. it gives the action to the button
    '''

    global randomLine, randomTimer
    if randomTimer == True:  # if random timer is on
        randomLine = True  # create the random lines


def RunActive():
    '''
    empities the orderlist and runs the system with the button click
    '''

    global run, orderList
    run = True
    orderList = []  # empties the list object


def StopActive():
    '''
    stops the system when stop button is clicked
    '''

    global stop
    stop = True


def ClearActive():
    '''
    clears existing system
    '''

    global clear
    clear = True


# activate flag for introduction menu


def StartGame():
    global start  # access the global variable
    start = True  # enable it
