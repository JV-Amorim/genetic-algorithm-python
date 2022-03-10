import numpy as np
from config import NUMBER_OF_GENERATIONS
from natural_selection import select_individuals_to_reproduction
from population import generate_initial_population, get_individuals_to_the_next_generation
from reproduction import reproduce_population_and_get_the_children


if __name__ == '__main__':
  current_population = generate_initial_population()

  for population_index in range(NUMBER_OF_GENERATIONS):
    selected_individuals = select_individuals_to_reproduction(current_population)
    population_children = reproduce_population_and_get_the_children(selected_individuals)
    new_population = get_individuals_to_the_next_generation(current_population, population_children)
    current_population = new_population
