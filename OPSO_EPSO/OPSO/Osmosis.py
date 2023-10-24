import Data.Swarm
import Data.functions as functions
import numpy as np


class Osmosis:
    def create_osmosis(self):
        horde = [Data.Swarm.Swarm(
            self.subpopulation_size_count, self.dimension, self.range_v, self.inertia, self.cognitive_force, self.social_const, self.adaptation_func) for _ in range(self.subpopulation_count)]
        return horde

    def __init__(self, subpopulation_count, subpopulation_size_count, dimension,
                 range_v, inertia, cognitive_force, social_const,
                 iteration_limit, adaptation_func, term, acc, threshold):
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
        self.threshold = threshold
        self.horde = self.create_osmosis()
        self.best_particle_adaptation = []
        self.mean_best_adaptation = []
        self.best = np.inf

    def calculate_migration_rate(self, adaptation_state, current_swarm_adaptation, next_swarm_adaptation):
        lambda_count = adaptation_state / \
            max(current_swarm_adaptation, next_swarm_adaptation)
        return round(lambda_count, 2)

    @staticmethod
    def swapped_amount(percentage, swarm_size):
        return round(percentage * swarm_size)

    def run(self):
        for _ in range(self.iteration_limit):
            for swarm in self.horde:
                swarm.run_swarm()
            for i in range(len(self.horde)):
                current_swarm = self.horde[i]
                next_swarm = self.horde[(i + 1) % len(self.horde)]
                current_swarm_adaptation = functions.functions_array[self.adaptation_func](
                    self.horde[i].best_particle.x)
                next_swarm_adaptation = functions.functions_array[self.adaptation_func](
                    self.horde[(i + 1) % len(self.horde)].best_particle.x)
                adaptation_state = abs(
                    current_swarm_adaptation - next_swarm_adaptation)
                if adaptation_state > self.threshold:
                    lambda_rate = self.calculate_migration_rate(
                        adaptation_state, current_swarm_adaptation, next_swarm_adaptation)
                    size_to_swap = self.swapped_amount(
                        lambda_rate, self.subpopulation_size_count)

                    if current_swarm_adaptation > next_swarm_adaptation:
                        current_swarm.particles_list.sort(
                            key=lambda x: x.adaptation)
                        next_swarm.particles_list.sort(
                            key=lambda x: x.adaptation, reverse=True)
                        particle_to_swap_from_c = [
                            current_swarm.particles_list[i] for i in range(size_to_swap)]
                        particle_to_swap_from_n = [
                            next_swarm.particles_list[i] for i in range(size_to_swap)]
                        current_swarm.particles_list = particle_to_swap_from_n + \
                            current_swarm.particles_list[size_to_swap:]
                        next_swarm.particles_list = particle_to_swap_from_c + \
                            next_swarm.particles_list[size_to_swap:]
                    else:
                        current_swarm.particles_list.sort(
                            key=lambda x: x.adaptation, reverse=True)
                        next_swarm.particles_list.sort(
                            key=lambda x: x.adaptation)
                        particle_to_swap_from_c = [
                            current_swarm.particles_list[i] for i in range(size_to_swap)]
                        particle_to_swap_from_n = [
                            next_swarm.particles_list[i] for i in range(size_to_swap)]
                        current_swarm.particles_list = particle_to_swap_from_n + \
                            current_swarm.particles_list[size_to_swap:]
                        next_swarm.particles_list = particle_to_swap_from_c + \
                            next_swarm.particles_list[size_to_swap:]
                    self.horde[i] = current_swarm
                    self.horde[(i + 1) % len(self.horde)] = next_swarm
            avg = [functions.functions_array[self.adaptation_func](
            swarm.best_particle.x) for swarm in self.horde]
            self.mean_best_adaptation.append(np.mean(avg))
            # if (self.best > np.min(avg)):
            #     self.best = np.min(avg)
            for swarm in self.horde:
                if (self.best > functions.functions_array[self.adaptation_func](
                        swarm.best_particle.x)):
                    self.best = swarm.best_particle.adaptation
            self.best_particle_adaptation.append(self.best)
