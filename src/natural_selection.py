import numpy as np
import random
from config import INDIVIDUAL_LENGTH, NATURAL_SELECTION_METHOD, POPULATION_SIZE
from natural_selection_methods import NaturalSelectionMethods


def select_individuals_from_population(population):
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.ROULETTE:
    return _select_individuals_with_roulette_method(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.TOURNAMENT:
    return _select_individuals_with_tournament_method(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.UNIFORM:
    return _select_individuals_with_uniform_method(population)
  
  raise ValueError('No valid natural selection method have been setted.')


def _select_individuals_with_roulette_method(population):
  raise ValueError('Implementation missing.')


def _select_individuals_with_tournament_method(population):
  selected_individuals = np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH))

  for i in range(0, POPULATION_SIZE, 2):
    first_individual_index = random.randint(0, POPULATION_SIZE - 1)
    second_individual_index = random.randint(0, POPULATION_SIZE - 1)

    selected_individuals[i] = population[first_individual_index]
    selected_individuals[i + 1] = population[second_individual_index]

  return selected_individuals


def _select_individuals_with_uniform_method(population):
  raise ValueError('Implementation missing.')
