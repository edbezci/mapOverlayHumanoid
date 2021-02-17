import src
import pytest
import random
import intro

'''
for the unit testing, the rule of thumb is to test everything that can break
with this testing, I intend to try and find any functions that are breakable
also I am adding black box testing methods where possible
black box testing means that you throw in the arguments into the functions without knowing much about them
if it breaks you find a bug, if not go on
also, we should keep in mind that variables within functions are not accessible
only class objects can have variables accessible within them
'''

# testing the enviroment


def test_AddPoints():
    '''
    this is the general method, a convention of pytest
    since we are not using oop, we are using pytest here to see
    whether all of my functions return the expected results
    '''

    if src.AddPoints((3, 4)):    # here we are feeding mock data
        # since we know that this function changes the global variable we are checking here if it really changes
        # so the number of items in the global variable should be more than 0, this function checks that
        assert len(src.points) != 0
    # here, same as above but with different mocking data since there should not be negative values
    if src.AddPoints((-4, 7)):
        # here changing if there are negative values, points variable should not be appended
        assert len(src.points) == 0


def test_acceptAddNewLine():
    # I can automate the mock values or give some manually
    if src.AddNewLine([(-5, 56), (-8, 82)]):
        # similar to the above but with more mocking data to comply with the acceptance testing
        assert len(src.lines) == 0
        assert len(src.line_name) == 0


def test_GenerateRandomlines():
    '''
    if the GenerateRandomLine function is called, check whether the lines and line_name variables lengths are not equal to zero
    if they are not zero, it means yes they are working
    if zero, it means it is not doing what it is supposed to do
    '''

    if src.GenerateRandomLine():
        # using the assert statement to see if the generating lines function actually works as it is supposed to
        assert len(src.lines) != 0
        assert len(src.line_name) != 0


def test_AddNewLine():
    if src.AddNewLine([(24, 56), (67, 82)]):  # again, putting mock data
        # checking if the related variables are working as they are supposed to
        # all the functions until check intersection check are doing this
        assert len(src.lines) != 0
        assert len(src.line_name) != 0


def test_AddNewColour():
    if src.AddNewColour:
        assert len(src.colours) != 0


def test_CursorActive():
    if src.CursorActive():
        assert src.cursor == True


def test_RandomActive():
    if src.RandomActive():
        assert src.randomTimer == True


def test_RunActive():
    if src.RunActive():
        assert src.run == True
        assert orderList == []


def test_StopActive():
    if src.StopActive():
        assert src.stop == True


def test_ClearActive():
    if src.ClearActive():
        assert src.clear == True


def test_StartGame():
    if src.StartGame():
        assert src.start == True


def test_CheckIntersect():
    '''
    this is not black box
    in this example I check inside the function, and assering values inside the function to
    see it does what it is supposed to
    '''

    p1 = random.randint(0, 400), random.randint(0, 400)
    p2 = random.randint(0, 400), random.randint(0, 400)
    q1 = random.randint(0, 400), random.randint(0, 400)
    q2 = random.randint(0, 400), random.randint(0, 400)
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]
    a2 = q2[1] - q1[1]
    b2 = q1[0] - q2[0]
    c2 = a2 * q1[0] + b2 * q1[1]
    d = (a1 * b2 - a2 * b1)
    if d == 0:
        # if determinant is zero, this should return nothing
        assert src.CheckIntersect(p1, p2, q1, q2) is None
    x = int((c1 * b2 - c2 * b1) / d)
    y = int((a1 * c2 - a2 * c1) / d)
    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
        if min(q1[0], q2[0]) <= x <= max(q1[0], q2[0]) and min(q1[1], q2[1]) <= y <= max(q1[1], q2[1]):
            # if there is an intersection, check if it is true
            assert src.CheckIntersect(p1, p2, q1, q2) == True
    # if not, it should be false
    assert src.CheckIntersect(p1, p2, q1, q2) == False


def test_BruteForceMain():
    # telling the test that ESC system exit is a desired outcome, not an error
    with pytest.raises(SystemExit):
        # if function does not work, it should have returned a message rather than "none", so I am checking for that
        assert src.BruteForceMain() is None


'''
all the test functions below are just like the one above, ensuring that no unwanted error message comes back
'''


def test_BentleyMain():
    with pytest.raises(SystemExit):
        assert src.BentleyMain() is None


def test_ShamosHoeyMain():
    with pytest.raises(SystemExit):
        assert src.ShamosHoeyMain() is None


def test_Efficiency():
    with pytest.raises(SystemExit):
        assert src.Efficiency() is None


def test_Efficiency2():
    with pytest.raises(SystemExit):
        assert src.Efficiency2() is None


def test_StartIntro2():
    if intro.StartIntro2():
        # this one checks that the global variable is acting as it is supposed to
        assert intro.intro2 == True


def test_Introduction():
    with pytest.raises(SystemExit):
        assert intro.Introduction() is None


def test_Introduction2():
    with pytest.raises(SystemExit):
        assert intro.Introduction2() is None
