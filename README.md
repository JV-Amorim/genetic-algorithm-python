# Genetic Algorithm

- Run `python src/main.py` or `py src/main.py` to execute the algorithm. The result plot will be save in `output/last-plot.png`.

- Read the following document for the problem description: 
[Computação Natural - Primeiro Trabalho Prático - Descrição do Problema](./docs/descricao-do-problema.pdf).

- Read the following document for the results report: 
[Computação Natural - Primeiro Trabalho Prático - Relatório de Resultados](./docs/relatorio-de-resultados.pdf).

- Set the `config.py` file with the following values to have the best possible results. With the number of executions equal to 1000, the program will be a little slow (about 1 minute per run), so please wait.

```python

NUMBER_OF_EXECUTIONS_PER_RUN = 1000

# ...

NATURAL_SELECTION_METHOD = NaturalSelectionMethods.TOURNAMENT
MUTATION_RATE = 0.4

```

> TODO: Improvements in this README.
