import random

import numpy as np
import Ant


class Anthill:
    def __init__(self, data, number_of_ants, evaporate_rate, alfa, beta, probability):
        self.data = data
        self.number_of_ants = number_of_ants
        self.pheromones_marks_matrix = [[1 for _ in range(len(self.data[0]))] for _ in range((len(self.data[0])))]
        self.DISTANCE_MATRIX = self.create_distance_matrix(self.data)
        self.ants_list = self.create_anthill(len(data[0]))
        self.evaporate_rate = evaporate_rate
        self.alfa = alfa
        self.beta = beta
        self.probability = probability
        self.best_ant = None
        self.best_tracks = []

    def __str__(self):
        return f"{self.data} {self.number_of_ants} {np.array(self.DISTANCE_MATRIX)} {self.pheromones_marks_matrix}"

    def get_pheromones_marks_matrix(self):
        return self.pheromones_marks_matrix

    def get_DISTANCE_MATRIX(self):
        return self.DISTANCE_MATRIX

    @staticmethod
    def calculate_distance_between_attractions(attraction_1_x, attraction_1_y, attraction_2_x, attraction_2_y):
        x_component = np.power(attraction_2_x - attraction_1_x, 2)
        y_component = np.power(attraction_2_y - attraction_1_y, 2)
        return np.sqrt(x_component + y_component)

    def create_distance_matrix(self, data):
        i, j = len(data[0]), len(data[0])
        distance_matrix = [[self.calculate_distance_between_attractions(data[1][y], data[2][y], data[1][x], data[2][x])
                            for x in range(i)] for y in range(j)]
        return distance_matrix

    def create_anthill(self, number_of_attractions):
        anthill = [Ant.Ant(number_of_attractions) for _ in range(self.number_of_ants)]
        return anthill

    def get_total_distance_for_ant(self, ant):
        total_distance = 0
        for i in range(1, len(ant.discovered_places)):
            total_distance += self.DISTANCE_MATRIX[ant.discovered_places[i - 1]][ant.discovered_places[i]]
        return total_distance

    def get_best_track(self):
        all_distances = [self.get_total_distance_for_ant(ant) for ant in self.ants_list]
        min_distance_index = all_distances.index(min(all_distances))
        self.best_ant = self.ants_list[min_distance_index]
        self.best_tracks.append(self.get_total_distance_for_ant(self.best_ant))

    def update_pheromones_marks(self, number_of_attractions):
        for i in range(number_of_attractions):
            for j in range(number_of_attractions):
                self.pheromones_marks_matrix[i][j] *= self.evaporate_rate
        for ant in self.ants_list:
            for i in range(len(ant.discovered_places) - 1):
                self.pheromones_marks_matrix[ant.discovered_places[i]][ant.discovered_places[i + 1]] \
                    += (1 / self.get_total_distance_for_ant(ant))
                self.pheromones_marks_matrix[ant.discovered_places[i + 1]][ant.discovered_places[i]] = \
                    self.pheromones_marks_matrix[ant.discovered_places[i]][ant.discovered_places[i + 1]]

    def find_path(self):
        for i in range(len(self.data[0])):
            for ant in self.ants_list:
                if i != 0:
                    if random.uniform(0, 1) < self.probability:
                        ant.visit_random_attraction()
                    else:
                        ant.visit_probabilistic_attraction(self.pheromones_marks_matrix, self.alfa, self.beta,
                                                           self.DISTANCE_MATRIX)
        # for ant in self.ants_list:
        #     ant.discovered_places.append(ant.discovered_places[0])
        self.update_pheromones_marks(len(self.data[0]))
