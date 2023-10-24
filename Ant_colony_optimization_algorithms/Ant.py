import math
import random


class Ant:
    def __init__(self, number_of_attractions):
        self.number_of_attractions = number_of_attractions
        self.discovered_places = [random.randint(0, number_of_attractions - 1)]
        self.available_attractions = [i for i in range(self.number_of_attractions) if i not in self.discovered_places]

    def __str__(self):
        return f'{self.number_of_attractions} {self.discovered_places}, {self.available_attractions}'

    def visit_random_attraction(self):
        r = random.randint(0, len(self.available_attractions) - 1)
        self.discovered_places.append(self.available_attractions[r])
        self.available_attractions.remove(self.available_attractions[r])

    def visit_probabilistic_attraction(self, pheromones_marks, alfa, beta, distance_matrix):
        actual_attraction = self.discovered_places[-1]
        used_indexes = []
        used_probability = []
        sum_of_probability = 0
        for attraction in self.available_attractions:
            used_indexes.append(attraction)
            pheromones_on_path = math.pow(pheromones_marks[actual_attraction][attraction], alfa)
            heuristic_for_path = math.pow(1 / distance_matrix[actual_attraction][attraction], beta)
            probability = pheromones_on_path * heuristic_for_path
            used_probability.append(probability)
            sum_of_probability += probability
        for i in range(len(used_probability)):
            used_probability[i] = used_probability[i] / sum_of_probability
        self.roulette_selection(used_indexes, used_probability)

    def roulette_selection(self, used_indexes, used_probability):
        interval = []
        total = 0
        for i in range(len(self.available_attractions)):
            interval.append([used_indexes[i], total, total + used_probability[i]])
            total = total + used_probability[i]
        draw = random.uniform(0, 1)
        result = None
        for i in range(len(self.available_attractions)):        #self.available_attractions
            if interval[i][1] < draw <= interval[i][2]:
                result = interval[i][0]
        self.discovered_places.append(result)
        self.available_attractions.remove(result)
