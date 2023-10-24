import random
import matplotlib.pyplot as plt
import numpy as np


class Genetic:
    def __init__(self, items_in_backpack, backpack_lifting_capacity, size_of_population, size_of_individual,
                 number_of_generations, percentage_of_population, odds_of_crossing, odds_of_mutation):
        self.items_in_backpack = items_in_backpack
        self.backpack_lifting_capacity = backpack_lifting_capacity
        self.size_of_population = size_of_population
        self.size_of_individual = size_of_individual
        self.number_of_generations = number_of_generations
        self.percentage_of_population = percentage_of_population
        self.odds_of_crossing = odds_of_crossing
        self.odds_of_mutation = odds_of_mutation
        self.__population = []
        self.__values_array = np.zeros(0, dtype=np.float64)
        self.__choice_probability = np.zeros(0, dtype=np.float64)
        self.__children = []
        self.__avg_value_of_population = []
        self.__best_value_of_population = []
        self.__median_value_of_population = []

    def __str__(self):
        return f"{self.__population} {self.__values_array} {self.__choice_probability}"

    def create_cycle(self):
        self.generate_initial_population()
        self.set_values_array()
        self.__avg_value_of_population.append(np.sum(self.__values_array) / self.size_of_population)
        self.set_probability_in_population()
        for i in range(0, self.number_of_generations):
            parents = self.choose_parents(self.percentage_of_population)
            while len(self.__children) < self.size_of_population:
                parent1, parent2 = self.get_couple(parents)
                if self.is_crossable:
                    # child1, child2 = self.single_point_crossover(self.__population[parent1],
                    # self.__population[parent2], 12)
                    child1, child2 = self.two_point_crossover(self.__population[parent1], self.__population[parent2],
                                                              15, 22)
                else:
                    child1, child2 = self.__population[parent1], self.__population[parent2]

                mutable1 = self.is_mutation()
                mutable2 = self.is_mutation()
                if mutable1:
                    child1 = self.individual_mutation(child1)
                elif mutable2:
                    child2 = self.individual_mutation(child2)

                self.__children.append(child1)
                self.__children.append(child2)
            self.__population = self.__children.copy()
            self.clear_properties()
            self.set_values_array()
            self.__avg_value_of_population.append(np.sum(self.__values_array) / self.size_of_population)
            self.set_probability_in_population()

    def clear_properties(self):
        self.__children.clear()
        self.__values_array = np.zeros(0, dtype=np.float64)
        self.__choice_probability = np.zeros(0, dtype=np.float64)

    def get_best_from_population(self):
        self.__best_value_of_population.append(max(self.__values_array))

    def get_median_from_population(self):
        self.__median_value_of_population.append(np.median(self.__values_array))

    def generate_initial_population(self):
        for i in range(0, self.size_of_population):
            current_individual = []
            for j in range(0, self.size_of_individual):
                gen = random.randint(0, 1)
                current_individual.append(gen)
            self.__population.append(current_individual)

    def choose_parents(self, percentage):
        parents = []
        for i in range((percentage * self.size_of_population) // 100):
            # parents.append(self.roulette_selection(self.size_of_population))
            parents.append(self.tournament_selection(100))
        return parents

    @staticmethod
    def get_couple(parents):
        pick1 = random.randint(0, len(parents) - 1)
        pick2 = random.randint(0, len(parents) - 1)
        if pick1 == pick2:
            while pick1 != pick2:
                pick2 = random.randint(0, len(parents))
        couple = [parents[pick1], parents[pick2]]
        return couple

    def is_crossable(self):
        drawing = random.uniform(0, 1)
        if self.odds_of_crossing > drawing:
            return True
        return False

    def is_mutation(self):
        drawing = random.uniform(0, 1)
        if self.odds_of_mutation > drawing:
            return True
        return False

    def calculate_adaptation_of_individual(self, individual):
        overall_weight = 0
        overall_value = 0
        for gene_index in range(len(individual)):
            current_bit = individual[gene_index]
            if current_bit == 1:
                overall_weight += self.items_in_backpack[gene_index].weight
                overall_value += self.items_in_backpack[gene_index].value

        if overall_weight > self.backpack_lifting_capacity:
            return 0
        return overall_value

    def set_values_array(self):
        for i in range(len(self.__population)):
            self.__values_array = np.append(self.__values_array,
                                            self.calculate_adaptation_of_individual(self.__population[i]))
        self.get_best_from_population()
        self.get_median_from_population()

    def set_probability_in_population(self):
        overall_population_value = sum(self.__values_array)
        if overall_population_value == 0:
            for i in range(len(self.__population)):
                self.__choice_probability = np.append(0, self.__choice_probability)
        else:
            for i in range(len(self.__population)):
                self.__choice_probability = np.append(self.__choice_probability,
                                                      self.__values_array[i] / overall_population_value)

    def roulette_selection(self, amount_of_choose):
        range_array = []
        total = 0
        for i in range(amount_of_choose):
            range_array.append([i, total, np.add(total, np.take(self.__choice_probability, i))])
            total = np.add(total, np.take(self.__choice_probability, i))
        drawing = random.uniform(0, total)
        result = []
        for i in range(amount_of_choose):
            if range_array[i][1] < drawing <= range_array[i][2]:
                result.append(range_array[i][0])
        return result[0]

    def tournament_selection(self, tournament_size):
        best = None
        for i in range(tournament_size):
            choose = random.randrange(self.size_of_population)
            if best is None or self.__choice_probability[choose] > self.__choice_probability[best]:
                best = choose
        return best

    @staticmethod
    def single_point_crossover(parent_a, parent_b, crossover_point):
        children = []
        child_1 = parent_a[:crossover_point] + parent_b[crossover_point:]
        children.append(child_1)
        child_2 = parent_b[:crossover_point] + parent_a[crossover_point:]
        children.append(child_2)
        return children

    @staticmethod
    def two_point_crossover(parent_a, parent_b, crossover_point1, crossover_point2):
        children = []
        child_1 = parent_a[:crossover_point1] + parent_b[crossover_point1:crossover_point2] + parent_a[crossover_point2:]
        children.append(child_1)
        child_2 = parent_b[:crossover_point1] + parent_a[crossover_point1:crossover_point2] + parent_b[crossover_point2:]
        children.append(child_2)
        return children

    def individual_mutation(self, individual):
        random_index = random.randint(0, self.size_of_individual - 1)
        if individual[random_index] == 0:
            individual[random_index] = 1
        elif individual[random_index] == 1:
            individual[random_index] = 0
        return individual

    def make_plot(self):
        x = np.arange(0, len(self.__avg_value_of_population), 1)

        plt.xticks(np.arange(min(x), max(x) + 1, 10.0))
        manager = plt.get_current_fig_manager()
        manager.resize(640, 480)
        plt.ticklabel_format(style='plain')
        plt.subplots_adjust(bottom=.20, left=.20)
        plt.scatter(
            x=x,
            y=self.__best_value_of_population,
            label="max",
            color="red",
            marker="x",
        )
        plt.scatter(
            x=x,
            y=self.__median_value_of_population,
            label="mediana",
            color="green",
        )
        plt.plot(x, self.__avg_value_of_population, label="srednia")
        plt.ylabel("Wartosc przedmiotow")
        plt.xlabel("Nr epoki")
        plt.legend()
        plt.show()
