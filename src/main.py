import matplotlib.pyplot as plt
from config import BEST_POSSIBLE_FITNESS, NUMBER_OF_EXECUTIONS_PER_RUN, NUMBER_OF_GENERATIONS
from individual import calculate_individual_fitness
from natural_selection import select_individuals_to_reproduction
from population import \
  find_best_individual_in_current_population, \
  generate_initial_population, \
  get_individuals_to_the_next_generation
from reproduction import reproduce_population_and_get_the_children


def execute_genetic_algorithm_n_times_and_display_the_results():
  best_fitnesses = []
  best_possible_fitness_count = 0

  for _ in range(NUMBER_OF_EXECUTIONS_PER_RUN):
    best_individual = execute_genetic_algorithm_and_get_best_individual()
    best_individual_fitness = calculate_individual_fitness(best_individual)
    best_fitnesses.append(best_individual_fitness)

    if (best_individual_fitness == BEST_POSSIBLE_FITNESS):
      best_possible_fitness_count += 1
  
  display_boxplot_with_the_results(best_fitnesses, best_possible_fitness_count)


def execute_genetic_algorithm_and_get_best_individual():
  current_population = generate_initial_population()

  for _ in range(NUMBER_OF_GENERATIONS):
    selected_individuals = select_individuals_to_reproduction(current_population)
    population_children = reproduce_population_and_get_the_children(selected_individuals)
    new_population = get_individuals_to_the_next_generation(current_population, population_children)
    current_population = new_population

  return find_best_individual_in_current_population(current_population)


def display_boxplot_with_the_results(best_fitnesses, best_possible_fitness_count):
  figure = plt.figure()
  figure.suptitle(f'Genetic Algorithm Result', fontsize=14, fontweight='bold')

  plot = figure.add_subplot(111)
  plot.boxplot(best_fitnesses)
  plot.set_title(f'The best possible fitness have been reached {best_possible_fitness_count} time(s).')
  plot.set_xlabel(f'Boxplot of the best fitnesses in {NUMBER_OF_EXECUTIONS_PER_RUN} execution(s).')
  plot.set_ylabel('Fitness')

  plt.show()


if __name__ == '__main__':
  execute_genetic_algorithm_n_times_and_display_the_results()
