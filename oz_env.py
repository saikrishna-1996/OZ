#import numpy as np

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

class oz_env():

    def __init__(self, board=None):
        self.board = board
        self.winner = None
        self.result = None
        #self.num_pass = 0


    def reset(self):
        #self.board = [[0,0,0,0,0,0,0,0],
        #        [0,0,0,0,0,0,0,0],
        #        [0,0,0,0,0,0,0,0],
        #        [0,0,0,-1,1,0,0,0],
        #        [0,0,0,1,-1,0,0,0],
        #        [0,0,0,0,0,0,0,0],
        #        [0,0,0,0,0,0,0,0],
        #        [0,0,0,0,0,0,0,0],
        #        [0,0,0,0,0,0,0,-1]] #turn is encoded in the last element
        self.board = [0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,-1,1,0,0,0,  0,0,0,1,-1,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,-1]
        self.winner = None
        self.resigned = False
        #self.num_pass = 0

        return self

    @property
    def done(self):
        return self.winner is not None

    @property
    def white_to_move(self):
        return self.board[71] == 1

    def is_game_over(self):
        #for i in range(8):
        #    for j in range(8):
        if self.board[70] >= 2:
            return 1

        for i in range(64):
            if self.board[i] == 0:
                return 0
        return 1

    def who_won(self):
        white_count = 0
        black_count = 0
        no_count = 0
        #for i in range(8):
        #    for j in range(8):
        for i in range(64):
            if self.board[i] == 1:
                white_count = white_count + 1
            elif self.board[i] == -1:
                black_count = black_count + 1
            else:
                no_count = no_count + 1
        if white_count > black_count:
            return 1
        elif white_count == black_count:
            return 0
        else:
            return -1


    def is_legal_E(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if (move_in_int+1) % 8 == 0:
                return 0
            else:
                if self.board[move_in_int+1] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int + 1
                    while (move_in_int+1)%8 != 0:
                        move_in_int = move_in_int + 1
                        if self.board[move_in_int] == player:
                            return 1
                    return 0

    def is_legal_W(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if (move_in_int % 8) == 0:
                return 0
            else:
                if self.board[move_in_int - 1] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int - 1
                    while (move_in_int % 8) != 0:
                        move_in_int = move_in_int - 1
                        if self.board[move_in_int] == player:
                            return 1
                    return 0

    def is_legal_N(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int > 55:
                return 0
            else:
                move_in_int = move_in_int + 8
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    while move_in_int < 56:
                        move_in_int = move_in_int + 8
                        if self.board[move_in_int] == player:
                            return 1
                    return 0

    def is_legal_S(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int <= 7:
                return 0
            else:
                move_in_int = move_in_int - 8
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    while move_in_int > 7:
                        move_in_int = move_in_int - 8
                        if self.board[move_in_int] == player:
                            return 1
                    return 0

    def is_legal_NE(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int > 45:
                return 0
            else:
                move_in_int = move_in_int + 9
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int + 9
                    while move_in_int < 64:
                        if self.board[move_in_int] == player:
                            return 1
                        move_in_int = move_in_int + 9
                    return 0


    def is_legal_SW(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int < 18:
                return 0
            else:
                move_in_int = move_in_int - 9
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int - 9
                    while move_in_int > 0:
                        if self.board[move_in_int] == player:
                            return 1
                        move_in_int = move_in_int - 9
                    return 0


    def is_legal_NW(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int >= 55:
                return 0
            else:
                move_in_int = move_in_int + 7
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int + 7
                    while move_in_int < 64:
                        if self.board[move_in_int] == player:
                            return 1
                        move_in_int = move_in_int + 7
                    return 0

    def is_legal_SE(self, move):
        player = self.board[71]
        anti_player = -player
        #move_in_int = square_to_int(move)
        move_in_int = move
        if self.board[move_in_int] != 0:
            return 0
        else:
            if move_in_int < 15:
                return 0
            else:
                move_in_int = move_in_int - 7
                if self.board[move_in_int] != anti_player:
                    return 0
                else:
                    move_in_int = move_in_int - 7
                    while move_in_int >= 0:
                        if self.board[move_in_int] == player:
                            return 1
                        move_in_int = move_in_int - 7
                    return 0

    def is_legal(self, move):
        if self.is_legal_SE(move) == 1 or self.is_legal_NW(move) == 1 or self.is_legal_SW(move) == 1 or self.is_legal_NE(move) == 1 or self.is_legal_S(move) == 1 or self.is_legal_N(move) == 1 or self.is_legal_W(move) == 1 or self.is_legal_E(move) == 1:
            return 1
        else:
            return 0

    def legal_mask(self):
        the_mask = [0]*65
        #for i in range(8):
        #    for j in range(8):
        #        move = i*8 + j
        #        the_mask[i,j] = self.is_legal(move)
        count = 0
        for i in range(64):
            the_mask[i] = self.is_legal(i)
            if self.is_legal(i) == 0:
                count = count + 1
        if count == 64:
            the_mask[64] = 1
        else:
            the_mask[64] = 0
        return the_mask

    def my_legal_moves(self):
        moves_list = []
        my_mask = self.legal_mask()
        for i in range(65):
            #print("am here")
            if my_mask[i] == 1:
                moves_list.append(i)
                #print(i)
        return moves_list

    def step(self, action):

        player = self.board[71]

        if action == 64:
            self.board[70] = self.board[70] + 1

        else:
       ## invert the pieces, if applicable

            if self.is_legal_E(action) == 1:
            #move_in_int = square_to_int(action)
                move_in_int = action
                while (move_in_int+1) % 8 != 0:
                    move_in_int = move_in_int + 1
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player

            if self.is_legal_W(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                while (move_in_int % 8) != 0:
                    move_in_int = move_in_int - 1
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player

            if self.is_legal_S(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                while move_in_int > 7:
                    move_in_int = move_in_int - 8
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player

            if self.is_legal_N(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                while move_in_int < 56:
                    move_in_int = move_in_int + 8
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player

            if self.is_legal_NE(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                move_in_int = move_in_int + 9
                while move_in_int < 64:
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player
                    move_in_int = move_in_int + 9

            if self.is_legal_SW(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                move_in_int = move_in_int - 9
                while move_in_int > 0:
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player
                    move_in_int = move_in_int - 9

            if self.is_legal_NW(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                move_in_int = move_in_int + 7
                while move_in_int < 64:
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player
                    move_in_int = move_in_int + 7

            if self.is_legal_SE(action) == 1:
                #move_in_int = square_to_int(action)
                move_in_int = action
                move_in_int = move_in_int - 7
                while move_in_int >= 0:
                    if self.board[move_in_int] == player:
                        break
                    else:
                        self.board[move_in_int] = player
                    move_in_int = move_in_int - 7

        if self.board[71] == 1:
            self.board[71] = -1
            #self.board[square_to_int(action)] = 1
            self.board[action] = 1
        else:
            self.board[71] = 1
            #self.board[square_to_int(action)] = -1
            self.board[action] = -1

