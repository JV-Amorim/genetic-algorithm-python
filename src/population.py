import numpy as np
from config import INDIVIDUAL_LENGTH, POPULATION_SIZE
from individual import calculate_individual_fitness, generate_random_individual


def generate_initial_population():
  population = generate_empty_population()

  for i in range(0, POPULATION_SIZE):
    population[i] = generate_random_individual()

  return population

def generate_empty_population():
  return np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH), np.ubyte)


# The following function uses the elitism method.
def get_individuals_to_the_next_generation(current_population, population_children):
  best_individual = find_best_individual_in_current_population(current_population) 
  worst_child_index = _find_index_of_worst_child_in_current_children(population_children)

  population_children[worst_child_index] = best_individual

  return population_children

def find_best_individual_in_current_population(current_population):
  best_individual = current_population[0]
  best_individual_fitness = calculate_individual_fitness(best_individual)

  for current_individual in current_population:
    current_individual_fitness = calculate_individual_fitness(current_individual)

    if current_individual_fitness > best_individual_fitness:      
      current_individual = best_individual
      best_individual_fitness = current_individual_fitness

  return best_individual

def _find_index_of_worst_child_in_current_children(population_children):
  index_of_worst_child = 0
  worst_child_fitness = calculate_individual_fitness(population_children[0])

  for current_index in range(0, POPULATION_SIZE):
    current_child_fitness = calculate_individual_fitness(population_children[current_index])

    if current_child_fitness < worst_child_fitness:
      index_of_worst_child = current_index
      worst_child_fitness = current_child_fitness

  return index_of_worst_child
