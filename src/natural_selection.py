import numpy as np
import random
from config import INDIVIDUAL_LENGTH, NATURAL_SELECTION_METHOD, POPULATION_SIZE
from natural_selection_methods import NaturalSelectionMethods
from individual import calculate_individual_fitness


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
    first_individual = _select_single_individual_with_tournament_method(population)
    second_individual = _select_single_individual_with_tournament_method(population)

    selected_individuals[i] = first_individual
    selected_individuals[i + 1] = second_individual

  return selected_individuals

def _select_single_individual_with_tournament_method(population):
  first_individual_index = random.randint(0, POPULATION_SIZE - 1)
  second_individual_index = random.randint(0, POPULATION_SIZE - 1)

  first_individual = population[first_individual_index]
  second_individual = population[second_individual_index]

  first_individual_fitness = calculate_individual_fitness(first_individual)
  second_individual_fitness = calculate_individual_fitness(second_individual)

  if first_individual_fitness >= second_individual_fitness:
    return first_individual
  
  return second_individual


def _select_individuals_with_uniform_method(population):
  raise ValueError('Implementation missing.')
