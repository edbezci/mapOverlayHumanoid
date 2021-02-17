import hlp
import src
import pytest
import pygame
import sys
import random


def test_Button():
    pos = pygame.mouse.get_pos()  # checking if pygame is working
    click = pygame.mouse.get_pressed()

    if hlp.Button("mock", 345, 531, 112, 45, src.ClearActive):
        # asserting whether the function is working and the button is working as required
        assert src.ClearActive()


def test_ButtonWithReturn():
    assert hlp.ButtonWithReturn("mock", 352, 214, 51, 10) == 0


def test_Description():
    with pytest.raises(SystemExit):
        # using list comprehension to create the mock data
        mock = [i for i in "mockingstringcreation"]
        for i in range(len(mock)):  # testing for each mock data
            # assuring that the output is correct
            assert hlp.Description(mock[i]) is None


def test_AddDesc():
    # using list comprehension to create the mock data
    mock = [i * 2 for i in "mockingstringcreation1232.,565"]
    x, y = random.randint(0, 789), random.randint(325, 861)
    for i in range(len(mock)):
        assert hlp.AddDesc(mock, (x, y)) is None


def test_AddText():
    # using list comprehension to create the mock data
    mock = [i * 2 for i in "mockingstringcreation1232.,565"]
    x, y = random.randint(0, 789), random.randint(325, 861)
    for i in range(len(mock)):
        assert hlp.AddText(mock[i], (x, y)) is None


def test_InsertNumber():
    with pytest.raises(SystemExit):  # assuring that the ESC key is normal not an error
        mock = str(random.randint(0, 950))
        assert hlp.InsertNumber(mock) == mock
