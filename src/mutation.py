import random
from config import INDIVIDUAL_LENGTH, MUTATION_RATE


def try_to_mutate_an_individual_child(child):
  child_mutation_value = random.random()  
  if (child_mutation_value <= MUTATION_RATE):
    child = _mutate_a_random_bit_in_individual_child(child)  
  return child

def _mutate_a_random_bit_in_individual_child(child):
  bit_index = random.randint(0, INDIVIDUAL_LENGTH - 1)
  child[bit_index] = 1 if child[bit_index] == 0 else 0
  return child
