import numpy as np
import random
from config import INDIVIDUAL_LENGTH


def generate_random_individual():
  individual = np.empty(INDIVIDUAL_LENGTH)

  for i in range(0, INDIVIDUAL_LENGTH):
    individual[i] = random.randint(0, 1)

  return individual


def calculate_individual_fitness(i):
  return \
    9 \
    + i[ 0] * i[ 4] - i[22] * i[13] + i[23] * i[ 3] - i[20] * i[ 9] \
    + i[35] * i[14] - i[10] * i[25] + i[15] * i[16] + i[ 2] * i[32] \
    + i[27] * i[18] + i[11] * i[33] - i[30] * i[31] - i[21] * i[24] \
    + i[34] * i[26] - i[28] * i[ 6] + i[ 7] * i[12] - i[ 5] * i[ 8] \
    + i[17] * i[19] - i[ 0] * i[29] + i[22] * i[ 3] + i[20] * i[14] \
    + i[25] * i[15] + i[30] * i[11] + i[24] * i[18] + i[ 6] * i[ 7] \
    + i[ 8] * i[17] + i[ 0] * i[32]
