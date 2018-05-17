import numpy as np

def square_to_int(square):
    if square == 'A8':
        return 0
    elif square == 'B8':
        return 1
    elif square == 'C8':
        return 2
    elif square == 'D8':
        return 3
    elif square == 'E8':
        return 4
    elif square == 'F8':
        return 5
    elif square == 'G8':
        return 6
    elif square == 'H8':
        return 7
    elif square == 'A7':
        return 8
    elif square == 'B7':
        return 9
    elif square == 'C7':
        return 10
    elif square == 'D7':
        return 11
    elif square == 'E7':
        return 12
    elif square == 'F7':
        return 13
    elif square == 'G7':
        return 14
    elif square == 'H7':
        return 15
    elif square == 'A6':
        return 16
    elif square == 'B6':
        return 17
    elif square == 'C6':
        return 18
    elif square == 'D6':
        return 19
    elif square == 'E6':
        return 20
    elif square == 'F6':
        return 21
    elif square == 'G6':
        return 22
    elif square == 'H6':
        return 23
    elif square == 'A5':
        return 24
    elif square == 'B5':
        return 25
    elif square == 'C5':
        return 26
    elif square == 'D5':
        return 27
    elif square == 'E5':
        return 28
    elif square == 'F5':
        return 29
    elif square == 'G5':
        return 30
    elif square == 'H5':
        return 31
    elif square == 'A4':
        return 32
    elif square == 'B4':
        return 33
    elif square == 'C4':
        return 34
    elif square == 'D4':
        return 35
    elif square == 'E4':
        return 36
    elif square == 'F4':
        return 37
    elif square == 'G4':
        return 38
    elif square == 'H4':
        return 39
    elif square == 'A3':
        return 40
    elif square == 'B3':
        return 41
    elif square == 'C3':
        return 42
    elif square == 'D3':
        return 43
    elif square == 'E3':
        return 44
    elif square == 'F3':
        return 45
    elif square == 'G3':
        return 46
    elif square == 'H3':
        return 47
    elif square == 'A2':
        return 48
    elif square == 'B2':
        return 49
    elif square == 'C2':
        return 50
    elif square == 'D2':
        return 51
    elif square == 'E2':
        return 52
    elif square == 'F2':
        return 53
    elif square == 'G2':
        return 54
    elif square == 'H2':
        return 55
    elif square == 'A1':
        return 56
    elif square == 'B1':
        return 57
    elif square == 'C1':
        return 58
    elif square == 'D1':
        return 59
    elif square == 'E1':
        return 60
    elif square == 'F1':
        return 61
    elif square == 'G1':
        return 62
    elif square == 'H1':
        return 63

class oz_env:

    def __init__(self, board=None):
        self.board = board
        self.winner = None
        self.result = None


	def reset(self):
    	self.board = [[0,0,0,0,0,0,0,0],
    					[0,0,0,0,0,0,0,0],
    					[0,0,0,0,0,0,0,0],
    					[0,0,0,-1,1,0,0,0],
    					[0,0,0,1,-1,0,0,0],
    					[0,0,0,0,0,0,0,0],
    					[0,0,0,0,0,0,0,0],
    					[0,0,0,0,0,0,0,0]
    					[0,0,0,0,0,0,0,0]] #turn is encoded in the last element
    	self.winner = None
    	self.resigned = False

    	return self

    @property
    def done(self):
    	return self.winner is not None

    @property
    def white_to_move(self):
    	return self.board[71] == 1

    @property

    def is_legal_E(self, board, last_move, turn):

