# Goal is to check if our current policy is any better than random policy
import argparse
import time

import numpy as np
import torch
from config import Config
from oz_env import oz_env, deepcopy
from networks import Polvalnet_fc
from MCTS import Node, MCTS
from train import load_model
parser = argparse.ArgumentParser(description='Launcher for policy tester')
parser.add_argument('--newnetwork', type=str, default=None, help='Path to the most recently trained model')
parser.add_argument('--numgames', type=int, default=1, help='how many games should they play against eachother?')
parser.add_argument('--no-cuda', action='store_true', default=True, help='disables GPU use')

args = parser.parse_args()
args.cuda = True if not args.no_cuda and torch.cuda.is_available() else False


def main():
    network = load_model(args.newnetwork)
    score_net = 0
    score_random = 0

    for game in range(args.numgames):
        moves = 0
        temperature = 10e-6
        env = oz_env()
        env.reset()
        root_node = Node(env, Config.EXPLORE_FACTOR)
        game_over = False
     #   print(root_node.env.board[71])
        while not game_over:
            start = time.time()
            if root_node.env.board[71] == -1:
                #print("am here")
                pi, successor, root_node = MCTS(temp=temperature, network= network, root=root_node)
                root_node = successor
            else:
                if (root_node.children == None):
                    root_node.children = [None]*len(root_node.legal_moves)

                move = np.random.randint(0,(len(root_node.legal_moves)))
                if (root_node.children[move] is None):
                    next_env = deepcopy(root_node.env)
                    next_env.step(root_node.legal_moves[move])

                    root_node.children[move] = Node(next_env,temperature,parent=root_node,child_id=move)
                root_node = root_node.children[move]
            moves = moves + 1

            game_over = root_node.env.is_game_over()
            z = root_node.env.who_won()

        if z <= -1:
            score_net += 1
        else:
            score_random += 1

        print("Game {} complete. Net: {} Random: {}".format(game, score_net, score_random))

    print("New network score total wins: {} Average Score: {}".format(score_net, score_net / args.numgames))
    print("Random play score total wins: {} Average Score: {}".format(score_random, score_random / args.numgames))


if __name__ == '__main__':
    main()

