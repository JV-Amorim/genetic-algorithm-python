import random
import numpy as np
from config import BITS_PER_GENE, INDIVIDUAL_LENGTH, NUMBER_OF_GENES, POPULATION_SIZE


def reproduce_population_and_get_the_children(population):
  children = np.empty((POPULATION_SIZE, INDIVIDUAL_LENGTH), np.ubyte)

  for i in range(0, POPULATION_SIZE, 2):
    first_parent = population[i]
    second_parent = population[i + 1]

    two_children = _generate_two_children_using_crossover(first_parent, second_parent)

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
