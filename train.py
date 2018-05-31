import glob
import os
import re

import numpy as np
import torch

# There will need to be some function that calls both of these functions and uses the output from load_gamefile to train a network
# load_gamefile will return a list of lists containing [state, policy, value] as created in MCTS.
from config import Config
# from logger import Logger
from networks import Polvalnet_fc


# Set the logger
# logger = Logger('./logs')


def load_gamefile(net_number):  # I'm not married to this, I think it could be done better.
    list_of_files = glob.glob(Config.GAMEPATH)
    net_files = []
    for file_name in list_of_files:
        if 'p' + repr(net_number) in file_name:
            net_files.append(file_name)

    index = np.random.randint(0, len(net_files))
    try:
        return np.load(net_files[index])
    except IOError:
        print('Could not load gamefile!')


def train_model(model, games=None, net_number=0, min_num_games=400):
    if games is None:
        game_data = load_gamefile(net_number)
    else:
        game_data = games

    print("entered train_model\n")
    total_train_iter = 0
    if game_data is not None:
        curr_train_iter = 0
        for game in game_data:
            num_batches = int(len(game) / Config.minibatch_size + 1)
            game = np.array(game)
            for i in range(num_batches):
                lower_bound = int(i * Config.minibatch_size)
                if lower_bound > len(game):
                    break
                upper_bound = int((i + 1) * Config.minibatch_size)
                if upper_bound > len(game):
                    upper_bound = len(game)

                data = game[lower_bound:upper_bound, :]
                if data.shape[0] != 0:
                    features = np.vstack(data[:, 0])

                    policy = np.vstack(data[:, 1]).astype(float)
                    features = torch.from_numpy(features.astype(float))
                    do_backprop(features, policy, data[:, 2], model, total_train_iter, curr_train_iter)
                    total_train_iter = total_train_iter + 1
                    curr_train_iter = curr_train_iter + 1
    return model


def cross_entropy(pred, soft_targets):
    return torch.mean(torch.sum(- soft_targets.double() * pred.double(), 1))


def do_backprop(features, policy, act_val, model, total_train_iter, curr_train_iter):
    print("entered do_backprop\n")
    criterion1 = torch.nn.MSELoss(size_average=False)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    ##We can do this cuda part later!?
    # if torch.cuda_is_available():
    #    criterion.cuda()
    #    policy_network.PolicyValNetwork_Giraffe = policy_network.PolicyValNetwork.cuda()

    nn_policy_out, nn_val_out = model(features)
    act_val = torch.autograd.Variable(torch.Tensor([act_val])).view(-1, 1)
    policy = torch.autograd.Variable(torch.from_numpy(policy).long())
    loss1 = criterion1(nn_val_out, act_val)
    loss2 = cross_entropy(nn_policy_out, policy)

    l2_reg = None
    for weight in model.parameters():
        if l2_reg is None:
            l2_reg = weight.norm(2)
        else:
            l2_reg = l2_reg + weight.norm(2)
    loss3 = 0.0001 * l2_reg

    loss = loss1.float() - loss2.float() + loss3.float()

    # Logging all the loss values
    #info = {
    #    'loss1': loss1.data[0],
    #    'loss2': loss2.data[0],
    #    'loss3': loss3.data[0]
    #}

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


def load_trained(model, fname):
    pretrained_state_dict = torch.load(fname)
    model_dict = model.state_dict()
    model_dict.update(pretrained_state_dict)
    model.load_state_dict(pretrained_state_dict)
    return model


def save_trained(model, iteration):
    print("entered save_trained\n")
    torch.save(model.state_dict(), "./{}.pt".format(iteration))


def load_model(fname=None):
    model = Polvalnet_fc()
    if fname is None:
        list_of_files = glob.glob('./*.pt')
        if len(list_of_files) != 0:
            latest_file = max(list_of_files, key=os.path.getctime)
            print('Loading latest model...')
            model = load_trained(model, latest_file)
            i = re.search('./(.+?).pt', latest_file)
            if i:
                if (i.group(1)) == 'pretrained':
                    print('Loaded pretrained model')
                    i = 0
                else:
                    i = int(i.group(1))
                    print('Current model number: {}'.format(i))
            return model, i
        else:
            print('Using new model')
            save_trained(model, 0)
            return model, 0
    else:
        model = load_trained(model, fname)
        return model
