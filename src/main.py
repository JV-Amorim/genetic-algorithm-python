import numpy as np
from config import NUMBER_OF_GENERATIONS
from natural_selection import select_individuals_from_population
from population import generate_initial_population, generate_new_population_from_current
from reproduction import generate_children_between_individuals


if __name__ == '__main__':
  current_population = generate_initial_population()

  for population_index in range(NUMBER_OF_GENERATIONS):
    selected_individuals = select_individuals_from_population(current_population)
    individuals_children = generate_children_between_individuals(selected_individuals)
    current_population = np.concatenate(current_population, individuals_children)
    new_population = generate_new_population_from_current(current_population)
    current_population = new_population
