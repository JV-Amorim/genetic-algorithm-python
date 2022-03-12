import numpy as np
import random
from config import NATURAL_SELECTION_METHOD, POPULATION_SIZE
from enums import NaturalSelectionMethods
from individual import calculate_individual_fitness
from population import calculate_population_total_fitness, generate_empty_population


def select_individuals_to_reproduction(population):
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.ROULETTE:
    return _select_individuals_with_roulette_method(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.TOURNAMENT:
    return _select_individuals_with_tournament_method(population)
  
  if NATURAL_SELECTION_METHOD == NaturalSelectionMethods.UNIFORM:
    return _select_individuals_with_uniform_method(population)
  
  raise ValueError('No valid natural selection method have been setted.')


def _select_individuals_with_roulette_method(population):
  selected_individuals = generate_empty_population()
  roulette_slices = _calculate_a_roulette_slice_for_each_individual(population)

  for i in range(0, POPULATION_SIZE):
    selected_individuals[i] = _select_single_individual_with_roulette_method(population, roulette_slices)

  return selected_individuals

def _calculate_a_roulette_slice_for_each_individual(population):
  roulette_slices = np.empty(POPULATION_SIZE)

  population_fitness = calculate_population_total_fitness(population)
  last_roulette_slice_value = 0

  for i in range(0, POPULATION_SIZE):
    current_individual_fitness = calculate_individual_fitness(population[i])
    current_individual_probability = current_individual_fitness / population_fitness
    roulette_slices[i] = last_roulette_slice_value + current_individual_probability
    last_roulette_slice_value = roulette_slices[i]

  return roulette_slices

def _select_single_individual_with_roulette_method(population, roulette_slices):
  roulette_value = random.random()
  
  for i in range(0, POPULATION_SIZE):
    current_slice_value = roulette_slices[i]
    
    if roulette_value < current_slice_value:
      return population[i]


def _select_individuals_with_tournament_method(population):
  selected_individuals = generate_empty_population()

  for i in range(0, POPULATION_SIZE, 2):
    first_individual = _select_single_individual_with_tournament_method(population)
    second_individual = _select_single_individual_with_tournament_method(population)

    selected_individuals[i] = first_individual
    selected_individuals[i + 1] = second_individual

  return selected_individuals

def _select_single_individual_with_tournament_method(population):
  first_individual = _select_single_individual_with_uniform_method(population)
  second_individual = _select_single_individual_with_uniform_method(population)

  first_individual_fitness = calculate_individual_fitness(first_individual)
  second_individual_fitness = calculate_individual_fitness(second_individual)

  if first_individual_fitness >= second_individual_fitness:
    return first_individual
  
  return second_individual


def _select_individuals_with_uniform_method(population):
  selected_individuals = generate_empty_population()

  for i in range(0, POPULATION_SIZE):
    selected_individuals[i] = _select_single_individual_with_uniform_method(population)

  return selected_individuals

def _select_single_individual_with_uniform_method(population):
  individual_index = random.randint(0, POPULATION_SIZE - 1)
  selected_individual = population[individual_index]
  return selected_individual
