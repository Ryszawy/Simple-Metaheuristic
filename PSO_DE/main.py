import click
import matplotlib.pyplot as plt
import Data_module.Data
import PSO.Swarm
import DE.Population
import numpy as np


@click.group()
def runs():
    pass


@runs.command()
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-n", "--number_of_agents", default=20)
@click.option("-c", "--cr_parameter", default=0.8)
@click.option("-f", "--f_parameter", default=0.9)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--picked_function", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_DE_30(dimension, range_v, number_of_agents, cr_parameter, f_parameter, iteration_limit, picked_function, term, acc):
    data_list = []
    for _ in range(30):
        de = DE.Population.Population(dimension, range_v, number_of_agents,
                                      cr_parameter, f_parameter, iteration_limit, picked_function, acc)
        de.run_de(term)
        best = de.find_best_agent()
        avg_adaptation = de.find_avg_adaptation()
        std = de.find_std_deviation()
        data_list.append(Data_module.Data.Data(
            best, avg_adaptation, std, iteration_limit))

    avg = [data.avg_result for data in data_list]
    std = [data.standard_deviation for data in data_list]
    best_every = [data.best_result.adaptation for data in data_list]
    plt.title('Avg and std for 30 iterations')
    plt.plot(np.arange(len(data_list)), avg, label='Avg')
    plt.plot(np.arange(len(data_list)), std, label='Std')
    plt.legend()
    plt.show()
    plt.title('Best particle for 30 iterations')
    plt.plot(np.arange(len(data_list)), best_every, label='Best particle')
    plt.legend()
    plt.show()


@runs.command()
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-n", "--number_of_agents", default=20)
@click.option("-c", "--cr_parameter", default=0.8)
@click.option("-f", "--f_parameter", default=0.9)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--picked_function", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_DE(dimension, range_v, number_of_agents, cr_parameter, f_parameter, iteration_limit, picked_function, term, acc):
    de = DE.Population.Population(dimension, range_v, number_of_agents,
                                  cr_parameter, f_parameter, iteration_limit, picked_function, acc)
    de.run_de(term)
    plt.title('Avg adaptation for DE algorithm')
    plt.xlabel("Iteration")
    plt.ylabel("Avg value of adaptation")
    plt.plot(np.arange(len(de.avg_values)),
             de.avg_values, label='Avg adaptation')
    plt.legend()
    plt.show()
    plt.title('Avg values for DE algorithm')
    plt.xlabel("Iteration")
    plt.ylabel("Avg value of individual")
    plt.plot(np.arange(len(de.avg_values)),
             de.agents_values, label='Avg values')
    plt.legend()
    plt.show()


@runs.command()
@click.option("-n", "--number_of_particle", default=20)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.25)
@click.option("-cp", "--cognitive_force", default=0.35)
@click.option("-sp", "--social_const", default=0.45)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--picked_function", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_PSO(number_of_particle, dimension, range_v, inertia, cognitive_force, social_const, iteration_limit, picked_function, term, acc):
    swarm = PSO.Swarm.Swarm(number_of_particle, dimension, range_v,
                            inertia, cognitive_force, social_const, picked_function)
    swarm.run_PSO(iteration_limit, acc, term)
    swarm.avg_adaptation_plot()


@runs.command()
@click.option("-n", "--number_of_particle", default=20)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.25)
@click.option("-cp", "--cognitive_force", default=0.35)
@click.option("-sp", "--social_const", default=0.45)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--picked_function", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_PSO_30(number_of_particle, dimension, range_v, inertia, cognitive_force, social_const, iteration_limit, picked_function, term, acc):
    data_list = []
    for _ in range(30):
        swarm = PSO.Swarm.Swarm(number_of_particle, dimension, range_v,
                                inertia, cognitive_force, social_const, picked_function)
        swarm.run_PSO(iteration_limit, acc, term)
        best = swarm.best_particle
        avg_adaptation = swarm.find_avg_adaptation()
        std_adaptation = swarm.find_std_deviation()
        data_list.append(Data_module.Data.Data(
            best, avg_adaptation, std_adaptation, iteration_limit))

    avg = [data.avg_result for data in data_list]
    std = [data.standard_deviation for data in data_list]
    best_every = [data.best_result.adaptation for data in data_list]
    plt.title('Avg and std for 30 iterations')
    plt.plot(np.arange(len(data_list)), avg, label='Avg')
    plt.plot(np.arange(len(data_list)), std, label='Std')
    plt.legend()
    plt.show()
    plt.title('Best particle for 30 iterations')
    plt.plot(np.arange(len(data_list)), best_every, label='Best particle')
    plt.legend()
    plt.show()


@runs.command()
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-n", "--number_of_elements", default=20)
@click.option("-c", "--cr_parameter", default=0.8)
@click.option("-f", "--f_parameter", default=0.9)
@click.option("-ip", "--inertia", default=0.2)
@click.option("-cp", "--cognitive_force", default=0.35)
@click.option("-sp", "--social_const", default=0.45)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--picked_function", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def compare(number_of_elements, dimension, range_v, cr_parameter, f_parameter,inertia, cognitive_force, social_const, iteration_limit, picked_function, term, acc):
    swarm = PSO.Swarm.Swarm(number_of_elements, dimension, range_v,
                            inertia, cognitive_force, social_const, picked_function)
    de = DE.Population.Population(dimension, range_v, number_of_elements,
                                  cr_parameter, f_parameter, iteration_limit, picked_function, acc)
    de.run_de(term)
    swarm.run_PSO(iteration_limit, acc, term)
    plt.title("Compare of PSO and DE")
    plt.plot(np.arange(len(de.avg_values)), de.avg_values, label="Avg adaptation DE")
    plt.plot(np.arange(len(de.best_agent)), de.best_agent, label="Best individual DE")
    plt.plot(np.arange(len(swarm.avg_adaptation)), swarm.avg_adaptation, label="Avg adaptation PSO")
    plt.plot(np.arange(len(swarm.best_particle_values)), swarm.best_particle_values, label="Best particle PSO")
    plt.legend()
    plt.show()


runs.add_command(run_DE_30)
runs.add_command(run_DE)
runs.add_command(run_PSO)
runs.add_command(run_PSO_30)
runs.add_command(compare)


if __name__ == "__main__":
    runs()
