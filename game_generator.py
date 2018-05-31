import multiprocessing as mp
import time

import numpy as np

from config import Config
from oz_env import oz_env
from networks import Polvalnet_fc
from MCTS import MCTS, Node
from self_challenge import Champion

class GameGenerator(object):
    def __init__(self, champion: Champion, pool: mp.Pool, batch_size: int, workers: int):

        self.champion = champion
        self.pool = pool
        self.workers = workers
        self.batch_size = batch_size

    def generate_game(self, model: Polvalnet_fc):
        np.random.seed()
        triplets = []
        step_game = 0
        temperature = 1
        game_over = False
        moves = 0
        env = oz_env()
        env.reset()
        root_node = Node(env, Config.EXPLORE_FACTOR)
        while not game_over:
            moves += 1
            step_game += 1
            if step_game == 50:
                temperature = 10e-6

            start = time.time()
            pi, successor, root_node = MCTS(temp=temperature, network=model, root=root_node)
            #print("Calculated next move in {}ms".format(time.time() - start))
            feature = root_node.env.board
            triplets.append([feature, pi])
            #print('')
            #print(root_node.env.board)
            #print("Running on {} ".format(mp.current_process()))
            root_node = successor
            game_over = root_node.env.is_game_over()

        z = root_node.env.who_won()
        for i in range(len(triplets) - step_game, len(triplets)):
            triplets[i].append(z)

        return triplets

    def play_game(self, _):
        return self.generate_game(self.champion.current_policy)

    def generate_games(self):
        start = time.time()
        games = self.pool.map(self.play_game, range(self.batch_size))
        #games = self.play_game
        print("Generated {} games in {}".format(len(games), time.time() - start))
        return games

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict
