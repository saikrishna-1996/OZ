import os
import platform

def make_move_maps():
    MOVETOINDEX = {}
    INDEXTOMOVE = []
    k = 0
    for i in range(0, 64):
        for j in range(0, 64):
            move = chess.Move(i, j).uci()

            if move[3] == '8' and move[1] == '7':
                for letter in 'QRBNqrbn':
                    new_move = move + letter
                    MOVETOINDEX[new_move] = k
                    INDEXTOMOVE.append(new_move)
                    k += 1
            elif move[3] == '1' and move[1] == '2':
                for letter in 'qrbnQRBN':
                    new_move = move + letter
                    MOVETOINDEX[new_move] = k
                    INDEXTOMOVE.append(new_move)
                    k += 1
            MOVETOINDEX[move] = k
            INDEXTOMOVE.append(move)
            k += 1
    INDEXTOMOVE[0] = 'a1a1'

    return MOVETOINDEX, INDEXTOMOVE


def make_square_map():
    ALLSQUARES = {}
    files = 'abcdefgh'
    k = 0
    for j in range(1, 9):
        for i in range(8):
            square_string = str(files[i] + repr(j))
            ALLSQUARES[square_string] = k
            k += 1
    return ALLSQUARES


class Config(object):
    default_workers = 4 if platform.system() != 'Linux' else 10
    think_time = 10  # 1 seconds
    minibatch_size = 32
    PRETRAIN_EPOCHS = 1
    SQUAREMAP = {'a1': 56, 'b1': 57, 'c1': 58, 'd1': 59, 'e1': 60, 'f1': 61, 'g1': 62, 'h1': 63, 'a2': 48, 'b2': 49, 'c2': 50,
                 'd2': 51,
                 'e2': 52, 'f2': 53, 'g2': 54, 'h2': 55, 'a3': 40, 'b3': 41, 'c3': 42, 'd3': 43, 'e3': 44, 'f3': 45,
                 'g3': 46,
                 'h3': 47, 'a4': 32, 'b4': 33, 'c4': 34, 'd4': 35, 'e4': 36, 'f4': 37, 'g4': 38, 'h4': 39, 'a5': 24,
                 'b5': 25,
                 'c5': 26, 'd5': 27, 'e5': 28, 'f5': 29, 'g5': 30, 'h5': 31, 'a6': 16, 'b6': 17, 'c6': 18, 'd6': 19,
                 'e6': 20,
                 'f6': 21, 'g6': 22, 'h6': 23, 'a7': 8, 'b7': 9, 'c7': 10, 'd7': 11, 'e7': 12, 'f7': 13, 'g7': 14,
                 'h7': 15,
                 'a8': 0, 'b8': 1, 'c8': 2, 'd8': 3, 'e8': 4, 'f8': 5, 'g8': 6, 'h8': 7}

    MOVETOINDEX, INDEXTOMOVE = make_move_maps()

    NUM_SIMULATIONS = 10
    BATCH_SIZE = default_workers
    D_ALPHA = 0.4
    EPS = 0.1
    EXPLORE_FACTOR = 2

    # Game Generator
    TEMP_REDUCE_STEP = 20
    MINGAMES = 10

    # Self Challenge
    NUM_GAMES = 4

    # PATHS
    ROOTDIR = '/u/gottipav/deep_pepper_chess'  ##### DEFINE AS REQ'd
    GAMEPATH = os.path.join(ROOTDIR, 'saved_games')
    NETPATH = os.path.join(ROOTDIR, 'saved_nets')
    BESTNET_NAME = 'BestNetwork.pth.tar'  # Example seen here: https://github.com/pytorch/examples/blob/0984955bb8525452d1c0e4d14499756eae76755b/imagenet/main.py#L139-L145

    minibatch_size = 100

    # NETWORK INFO
    d_in = 72
    h1 = 512  # neurons in first hidden layer
    h2 = 256  # neurons in second hidden layer
    d_out = 64

