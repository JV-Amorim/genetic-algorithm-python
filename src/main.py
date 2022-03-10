from config import NUMBER_OF_GENERATIONS
from individual import calculate_individual_fitness
from natural_selection import select_individuals_to_reproduction
from population import find_best_individual_in_current_population, generate_initial_population, get_individuals_to_the_next_generation
from reproduction import reproduce_population_and_get_the_children


def execute_genetic_algorithm_and_get_best_individual():
  current_population = generate_initial_population()

  for _ in range(NUMBER_OF_GENERATIONS):
    selected_individuals = select_individuals_to_reproduction(current_population)
    population_children = reproduce_population_and_get_the_children(selected_individuals)
    new_population = get_individuals_to_the_next_generation(current_population, population_children)
    current_population = new_population

  return find_best_individual_in_current_population(current_population)


if __name__ == '__main__':
  best_individual = execute_genetic_algorithm_and_get_best_individual()
  best_individual_fitness = calculate_individual_fitness(best_individual)
  print('Fitness of the best individual of the last generation: ' + str(best_individual_fitness))
