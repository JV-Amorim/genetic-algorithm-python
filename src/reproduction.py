import random
import numpy as np
from config import BITS_PER_GENE, MUTATION_ENABLED, NUMBER_OF_GENES, POPULATION_SIZE
from mutation import try_to_mutate_an_individual_child
from population import generate_empty_population


def reproduce_population_and_get_the_children(population):
  children = generate_empty_population()

  for i in range(0, POPULATION_SIZE, 2):
    first_parent = population[i]
    second_parent = population[i + 1]

    two_children = _generate_two_children_using_crossover(first_parent, second_parent)

    if MUTATION_ENABLED:
      children[i] = try_to_mutate_an_individual_child(two_children[0])
      children[i + 1] = try_to_mutate_an_individual_child(two_children[1])
    else:
      children[i] = two_children[0]
      children[i + 1] = two_children[1]

  return children

def _generate_two_children_using_crossover(first_parent, second_parent):
  crossover_cut_point = random.randint(1, NUMBER_OF_GENES - 1)
  crossover_cut_index = crossover_cut_point * BITS_PER_GENE

  first_child = np.concatenate((
    first_parent[:crossover_cut_index],
    second_parent[crossover_cut_index:]
  ))
  second_child = np.concatenate((
    second_parent[:crossover_cut_index],
    first_parent[crossover_cut_index:]
  ))

  return [first_child, second_child]
