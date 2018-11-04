import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from config import Config

class Polvalnet_fc(nn.Module):
	def __init__(self,
		d_in = Config.d_in,
		h1 = Config.h1,
		h2 = Config.h2,
		d_out = Config.d_out):

		super(Polvalnet_fc, self).__init__()

		self.turn_embedding = nn.Linear(2, 8)
		self.linear1 = nn.Linear(d_in, h1)
		self.linear2 = nn.Linear(h1, h2)
		self.linear3p = nn.Linear(h2, d_out)
		self.linear3v = nn.Linear(h2, 1)

	def forward(self, x, turn_to_play):

		turn_to_play = Variable(turn_to_play.float())
		turn_to_play = F.relu(self.turn_embedding(turn_to_play))

		x = Variable(x.float())

		inp = torch.cat([x, turn_to_play], dim=-1)
		h1_relu = F.relu(self.linear1(inp))
		h2_relu = F.relu(self.linear2(h1_relu))
		p_out = F.sigmoid(self.linear3p(h2_relu))
		v_out = F.tanh(self.linear3v(h2_relu))

		return p_out, v_out
