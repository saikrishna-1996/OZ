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
    elif square == 'F8':
        return 6

class oz_env:

    def __init__(self, board, turn):
        self.board = board
        self.turn = turn


