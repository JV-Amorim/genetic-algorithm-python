import random
import numpy as np
from enum import Enum


class NaturalSelectionMethods(Enum):
  ROULETTE = 1,
  TOURNAMENT = 2,
  UNIFORM = 3


POPULATION_SIZE = 30
NUMBER_OF_GENERATIONS = 40
NUMBER_OF_GENES = 9
BITS_PER_GENE = 4
INDIVIDUAL_LENGTH = NUMBER_OF_GENES * BITS_PER_GENE
NATURAL_SELECTION_METHOD = NaturalSelectionMethods.TOURNAMENT


def generate_initial_population():
  population = np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH))

  for i in range(0, POPULATION_SIZE):
    population[i] = generate_random_individual()

  return population

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


def select_individuals_with_roulette(population):
  raise ValueError('Implementation missing.')

def select_individuals_with_tournament(population):
  selected_individuals = np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH))

  for i in range(0, POPULATION_SIZE, 2):
    first_individual_index = random.randint(0, POPULATION_SIZE - 1)
    second_individual_index = random.randint(0, POPULATION_SIZE - 1)

    selected_individuals[i] = population[first_individual_index]
    selected_individuals[i + 1] = population[second_individual_index]

  return selected_individuals

def select_individuals_with_uniform(population):
  raise ValueError('Implementation missing.')

def select_individuals_from_population(population):
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.ROULETTE:
    return select_individuals_with_roulette(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.TOURNAMENT:
    return select_individuals_with_tournament(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.UNIFORM:
    return select_individuals_with_uniform(population)
  
  raise ValueError('No valid natural selection method have been setted.')


def generate_children_between_individuals(individuals):
  raise ValueError('Implementation missing.')


def generate_new_population_from_current(population):
  raise ValueError('Implementation missing.')


if __name__ == '__main__':
  current_population = generate_initial_population()

  for population_index in range(NUMBER_OF_GENERATIONS):
    selected_individuals = select_individuals_from_population(current_population)
    individuals_children = generate_children_between_individuals(selected_individuals)
    current_population = np.concatenate(current_population, individuals_children)
    new_population = generate_new_population_from_current(current_population)
    current_population = new_population
