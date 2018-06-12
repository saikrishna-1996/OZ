# Goal is to check if our current policy is any better than random policy
import argparse
#import glob
#import os
import time

import numpy as np
import torch
#print("lol")
from config import Config
from oz_env import oz_env, deepcopy
#import oz_env
#print("loool")
from networks import Polvalnet_fc
#print("wtf-1")
from MCTS import Node, MCTS
#print("wtf-2")
from train import load_model
#print("l0l-2")
parser = argparse.ArgumentParser(description='Launcher for policy tester')
parser.add_argument('--newnetwork', type=str, default=None, help='Path to the most recently trained model')
#print("lol-3")
parser.add_argument('--oldnetwork', type=str, default=None, help='Path to an older trained model')
parser.add_argument('--numgames', type=int, default=1, help='how many games should they play against eachother?')
parser.add_argument('--no-cuda', action='store_true', default=True, help='disables GPU use')

#print("check-1")
args = parser.parse_args()
args.cuda = True if not args.no_cuda and torch.cuda.is_available() else False


def main():
    #print("check-2")
    network = load_model(args.newnetwork)
    #print("am here")
    score_net = 0
    score_random = 0

    for game in range(args.numgames):
        moves = 0
        temperature = 10e-6
        white = 1
        black = None

        env = oz_env()
        env.reset()
        root_node = Node(env, Config.EXPLORE_FACTOR)
        game_over = False

        while not game_over:
            if root_node.env.board[71] == 1:
                player = white
            else:
                player = black
            #print(root_node.env.board)
            start = time.time()
            if player == white:
                #print(root_node.env.board)
                print("am here-1\n")
                pi, successor, root_node = MCTS(temp=temperature, network= network, root=root_node)
                #print(root_node.env.board)
                print("MCTS completed move {} in: {}".format(moves, time.time() - start))
                root_node = successor
            else:
                print("am here-2\n")
                if (root_node.children == None):
                    root_node.children = [None]*len(root_node.legal_moves)

                move = np.random.randint(0,(len(root_node.legal_moves)))
                if (root_node.children[move] is None):
                    #next_env = root_node.env.deepcopy()
                    next_env = deepcopy(root_node.env)
                    #next_env = root_node.env
                    next_env.step(root_node.legal_moves[move])

                    root_node.children[move] = Node(next_env,temperature,parent=root_node,child_id=move)
                root_node = root_node.children[move]
            print(root_node.env.board)
            moves = moves + 1

            game_over = root_node.env.is_game_over()
            z = root_node.env.who_won()

        # from white perspective

        #if white == player:
        if z >= 1:
            score_net += 1
        else:
            score_random += 1
        #else:
        #    if z <= -1:
        #        score_net += 1
        #    else:
        #        score_random += 1

        print("Game {} complete. Net: {} Random: {}".format(game, score_net, score_random))

    print("New network score total wins: {} Average Score: {}".format(score_net, score_net / args.numgames))
    print("Random play score total wins: {} Average Score: {}".format(score_random, score_random / args.numgames))


if __name__ == '__main__':
    main()

