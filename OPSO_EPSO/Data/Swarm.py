import Data.Particle as Particle
import Data.functions as functions
import numpy as np


class Swarm:
    def generate_swarm(self):
        particles = [Particle.Particle(self.dimension, np.random.uniform(-self.range_v, self.range_v, self.dimension),
                                       self.inertia, self.cognitive_force, self.social_const) for _ in range(self.number_of_particle)]
        return particles

    def __init__(self, number_of_particle, dimension, range_v, inertia, cognitive_force, social_const, adaptation_func):
        self.number_of_particle = number_of_particle
        self.dimension = dimension
        self.range_v = range_v
        self.inertia = inertia
        self.cognitive_force = cognitive_force
        self.social_const = social_const
        self.adaptation_func = adaptation_func
        self.particles_list = self.generate_swarm()
        self.best_particle = None

    def calculate_adaptation(self, particle):
        particle.adaptation = functions.functions_array[self.adaptation_func](
        particle.x)
        if particle.adaptation < particle.best_adaptation:
            particle.best_adaptation = particle.adaptation
            particle.best_x = particle.x

    def set_best_particle(self):
        best_adaptation = np.inf
        best_particle = None
        for particle in self.particles_list:
            self.calculate_adaptation(particle)
            if particle.adaptation < best_adaptation:
                best_adaptation = particle.adaptation
                best_particle = particle
        self.best_particle = best_particle

    def run_swarm(self):
        self.set_best_particle()
        for particle in self.particles_list:
            if particle is not self.best_particle:
                particle.calculate_velocity(self.best_particle.x)
                particle.update_position()  
                                            