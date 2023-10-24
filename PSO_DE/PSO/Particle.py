import numpy as np


class Particle:
    def __init__(self, dimension ,x_array, inertia, cognitive_force, social_const):
        self.dimension = dimension
        self.x = x_array
        self.inertia = np.float64(inertia)
        self.cognitive_force = np.float64(cognitive_force)
        self.social_const = np.float64(social_const)
        self.adaptation = np.inf
        self.velocity = np.random.uniform(low=-32, high=32, size=dimension)
        self.best_x = np.array([x for x in x_array])
        self.best_adaptation = np.inf

    def __str__(self):
        return f"x: {self.x}, dimension: {self.dimension}, adaptation: {self.adaptation}, best_x: {self.best_x}, " \
            f"best_adaptation: {self.best_adaptation} velocity {self.velocity}"

    def calculate_velocity(self, global_x):
        r_local_best = np.random.uniform(0, 1, size=1)
        r_global_best = np.random.uniform(0, 1, size=1)
        new_velocity = np.zeros(self.dimension)
        new_velocity = self.inertia * self.velocity + self.cognitive_force * r_local_best[0] * np.subtract(
            self.best_x, self.x) + self.social_const * r_global_best[0] * np.subtract(global_x, self.x)
        self.velocity = new_velocity

    def update_position(self):
        self.x = np.add(self.x, self.velocity)
