import Data.Swarm
import Data.functions as functions
import numpy as np


class EliteHorde:
    def create_horde(self):
        horde = [Data.Swarm.Swarm(
            self.subpopulation_size_count, self.dimension, self.range_v, self.inertia, self.cognitive_force, self.social_const, self.adaptation_func) for _ in range(self.subpopulation_count)]
        return horde

    def __init__(self, subpopulation_count, subpopulation_size_count, dimension,
                 range_v, inertia, cognitive_force, social_const,
                 iteration_limit, adaptation_func, term, acc):
        self.subpopulation_count = subpopulation_count
        self.subpopulation_size_count = subpopulation_size_count
        self.dimension = dimension
        self.range_v = range_v
        self.inertia = inertia
        self.cognitive_force = cognitive_force
        self.social_const = social_const
        self.iteration_limit = iteration_limit
        self.adaptation_func = adaptation_func
        self.term = term
        self.acc = acc
        self.horde = self.create_horde()
        self.best_particle_adaptation = []
        self.mean_best_adaptation = []
        self.best = np.inf

    @staticmethod
    def learn_from_the_best(elite_particles, best_from_swarm):
        filtered_elite_particles = []
        for particle in elite_particles:
            if particle is not best_from_swarm:
                filtered_elite_particles.append(particle)
        all_x_values = []
        for particle in filtered_elite_particles:
            all_x_values.append(particle.x)

        columns_value = np.sum(all_x_values, axis=0)
        mu, sigma = 0, 1  # mean and standard deviation
        mean_values = [columns_value[i] /
                       len(all_x_values) for i in range(len(columns_value))]
        n_component = np.random.default_rng().normal(mu, sigma) + 1
        return [mean_values[i] * n_component for i in range(len(mean_values))]

    def run(self):
        for _ in range(self.iteration_limit):
            for swarm in self.horde:
                swarm.run_swarm()
            elite_particles = [swarm.best_particle for swarm in self.horde]
            for swarm in self.horde:
                swarm.best_particle.x = self.learn_from_the_best(
                    elite_particles, swarm.best_particle)
                # print(swarm.best_particle.adaptation)
            avg = [functions.functions_array[self.adaptation_func](
                swarm.best_particle.x) for swarm in self.horde]
            self.mean_best_adaptation.append(np.mean(avg))
            for swarm in self.horde:
                if (self.best > functions.functions_array[self.adaptation_func](
                        swarm.best_particle.x)):
                    self.best = swarm.best_particle.adaptation
            # if (self.best > np.min(avg)):
            #     self.best = np.min(avg)
            self.best_particle_adaptation.append(self.best)
