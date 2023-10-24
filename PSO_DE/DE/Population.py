import numpy as np
from random import randrange
from tqdm import tqdm
import DE.Individual
import Data_module.functions


class Population:
    def __init__(self, dimension, range_v, number_of_agents, cr_parameter, f_parameter, iteration_limit, picked_function, acc):
        self.dimension = dimension
        self.range_v = range_v
        self.number_of_agents = number_of_agents
        self.agents = self.initialize_population()
        self.crossover_probability = cr_parameter
        self.differential_weight = f_parameter
        self.iteration_limit = iteration_limit
        self.picked_function = picked_function
        self.acc = acc
        self.avg_values = []
        self.agents_values = []
        self.best_agent = []

    def initialize_population(self):
        individuals = [DE.Individual.Individual(
            np.random.uniform(-self.range_v, self.range_v, self.dimension)) for _ in range(self.number_of_agents)]
        return individuals

    def calculate_adaptation(self):
        for agent in self.agents:
            agent.adaptation = Data_module.functions.functions_array[self.picked_function](
                agent.x)

    def find_best_agent(self):
        best_agent = None
        best_adaptation = np.inf
        for agent in self.agents:
            if (best_adaptation > agent.adaptation):
                best_agent = agent
        return best_agent

    def calculate_values(sef):
        values = []
        for agent in sef.agents:
            values.append(np.sum(agent.x))
        return values

    def find_avg_adaptation(self):
        adaptation = [agent.adaptation for agent in self.agents]
        return np.average(adaptation)

    def find_std_deviation(self):
        adaptation = [agent.adaptation for agent in self.agents]
        return np.std(adaptation)

    def update_avg_x_values(self):
        avg_x = np.array([agent.x for agent in self.agents])
        # np.append(self.agents_values, np.average(np.absolute(avg_x)))
        self.agents_values.append(np.average(np.absolute(avg_x)))

    def pick_three_random_agents(self, current_agent):
        index_array = [i for i in range(self.number_of_agents)]
        index_array.pop(current_agent)
        picked = []
        for _ in range(3):
            random_i = np.random.randint(len(index_array), size=1)[0]
            picked.append(index_array[random_i])
            index_array.pop(random_i)
        return picked

    def compute_potentially_position(self, agent, a, b, c, random_index):
        y_array = np.zeros(self.dimension)
        for i in range(len(y_array)):
            random_number = np.random.uniform(low=0, high=1, size=(1))[0]
            if (random_number < self.crossover_probability or i is random_index):
                y_array[i] = a.x[i] + \
                    self.differential_weight * (b.x[i] - c.x[i])
            else:
                y_array[i] = agent.x[i]

        result = DE.Individual.Individual(y_array)
        return result

    def run_de(self, flag):
        for i in tqdm(range(self.iteration_limit)):
            self.calculate_adaptation()
            # np.append(self.avg_values, self.find_avg_adaptation())
            self.avg_values.append(self.find_avg_adaptation())
            self.update_avg_x_values()
            # np.append(self.best_agent, self.find_best_agent().adaptation)
            self.best_agent.append(self.find_best_agent().adaptation)
            if flag and np.abs(self.find_best_agent().adaptation - self.acc) < self.acc:
                break
            current_agent = 0
            for agent in self.agents:
                picked_agents = self.pick_three_random_agents(current_agent)
                agent_a = self.agents[picked_agents[0]]
                agent_b = self.agents[picked_agents[1]]
                agent_c = self.agents[picked_agents[2]]
                random_index = randrange(self.dimension)
                new_agent = self.compute_potentially_position(
                    agent, agent_a, agent_b, agent_c, random_index)
                if (Data_module.functions.functions_array[self.picked_function](new_agent.x) <= Data_module.functions.functions_array[self.picked_function](agent.x)):
                    agent.x = new_agent.x
