"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this judge allows you to focus on choosing the best position to play
tic-tac-toe game Just by write your code in BotNumOne or BotNumTwo
------------------------------------------------------------
this dummy bot chooses positions randomly
you can edit it and check the game board assigned in "GameBoard",
and your char will be X|O assigned randomly in "Char"
the free spaces in GameBoard are initialized as List of Nones
your code must contain "play" function that return position
that's the position you want to make your move in
NOTE: Empty = None
"""
import random
from Helper import *

class BotNumTwo:
    def __init__(self):
        self.GameBoard = Empty
        self.Char = Empty
        self.Opponent = Empty

    def play(self, GameBoard, Char):
        # reinitialize the current turn properties
        self.GameBoard = GameBoard
        self.Char = Char
        self.Opponent = GetOpponent(Char)
        AvailableMoves = GetAvailableMoves(GameBoard)

        return random.randint(0, 8)
