import matplotlib.pyplot as plt
import pandas as pd
import pandas
import numpy as np
from tqdm import tqdm
from pandas.plotting import parallel_coordinates
import PSO.Particle
import Data_module.functions


class Swarm:
    def __init__(self, number_of_particle, dimension, range_v, inertia, cognitive_force, social_const, picked_function):
        self.number_of_particle = number_of_particle
        self.dimension = dimension
        self.range_v = range_v
        self.inertia = inertia
        self.cognitive_force = cognitive_force
        self.social_const = social_const
        self.picked_function = picked_function
        self.particles_list = self.generate_swarm()
        self.best_particle = None
        self.avg_adaptation = []
        self.avg_x_values = []
        self.avg_iteration = []
        self.best_particle_values = []

    def generate_swarm(self):
        particles = [PSO.Particle.Particle(self.dimension, np.random.uniform(
            -self.range_v, self.range_v, self.dimension), self.inertia, self.cognitive_force, self.social_const) for _ in range(self.number_of_particle)]
        return particles

    # zparametryzować użycie funkcji function1 itp
    def calculate_adaptation(self, particle):
        particle.adaptation = Data_module.functions.functions_array[self.picked_function](
            particle.x)
        if particle.adaptation < particle.best_adaptation:
            particle.best_adaptation = particle.adaptation
            particle.best_x = particle.x

    def update_avg_adaptation(self):
        adaptation = np.array(
            [particle.adaptation for particle in self.particles_list])
        self.avg_adaptation.append(np.average(adaptation))

    def update_avg_x_values(self):
        avg_x = np.array([particle.x for particle in self.particles_list])
        self.avg_x_values.append(np.average(np.absolute(avg_x)))

    def find_avg_adaptation(self):
        adaptation = [particle.adaptation for particle in self.particles_list]
        return np.average(adaptation)

    def find_std_deviation(self):
        adaptation = [particle.adaptation for particle in self.particles_list]
        return np.std(adaptation)

    def set_best_particle(self):
        best_adaptation = np.inf
        best_particle = None
        for particle in self.particles_list:
            self.calculate_adaptation(particle)
            if particle.adaptation < best_adaptation:
                best_adaptation = particle.adaptation
                best_particle = particle
        self.best_particle = best_particle

    def run_PSO(self, epoch_number, acc, flag):
        self.set_best_particle()
        for i in tqdm(range(epoch_number)):
            if flag and np.abs(self.best_particle.adaptation - acc) < acc:
                break
            self.update_avg_adaptation()
            self.update_avg_x_values()
            self.best_particle_values.append(self.best_particle.adaptation)
            for particle in self.particles_list:
                particle.calculate_velocity(self.best_particle.x)
                particle.update_position()
                self.calculate_adaptation(particle)
                self.set_best_particle()

    def avg_adaptation_plot(self):
        x = [i for i in range(len(self.avg_adaptation))]
        plt.title('Avg adaptation for PSO algorithm')
        plt.xlabel("Iteration")
        plt.ylabel("Avg value of adaptation")
        plt.plot(x, self.avg_adaptation, label="Avg adaptation")
        plt.legend()
        plt.show()
        plt.title('Avg values for PSO algorithm')
        plt.xlabel("Iteration")
        plt.ylabel("Avg value of particles")
        plt.plot(x, self.avg_x_values, label="Avg values")
        plt.legend()
        plt.show()
