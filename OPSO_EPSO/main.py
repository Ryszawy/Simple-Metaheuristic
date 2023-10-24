import click
import numpy as np
import EPSO.EliteHorde
import OPSO.Osmosis
import Data.Plots


@click.group()
def runs():
    pass


@runs.command()
@click.option("-sc", "--subpopulation_count", default=2)
@click.option("-ssc", "--subpopulation_size_count", default=2)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.9)
@click.option("-cp", "--cognitive_force", default=0.8)
@click.option("-sp", "--social_const", default=0.4)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--adaptation_func", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_EPSO(subpopulation_count, subpopulation_size_count, dimension,
             range_v, inertia, cognitive_force, social_const,
             iteration_limit, adaptation_func, term, acc):
    horde = EPSO.EliteHorde.EliteHorde(
        subpopulation_count, subpopulation_size_count, dimension,
        range_v, inertia, cognitive_force, social_const,
        iteration_limit, adaptation_func, term, acc)
    horde.run()
    Data.Plots.avg_plot(horde.best_particle_adaptation, horde.mean_best_adaptation, adaptation_func, chart="EPSO")

@runs.command()
@click.option("-sc", "--subpopulation_count", default=2)
@click.option("-ssc", "--subpopulation_size_count", default=2)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.9)
@click.option("-cp", "--cognitive_force", default=0.8)
@click.option("-sp", "--social_const", default=0.4)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--adaptation_func", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
def run_EPSO_30(subpopulation_count, subpopulation_size_count, dimension,
             range_v, inertia, cognitive_force, social_const,
             iteration_limit, adaptation_func, term, acc):
    data_list = []
    mean_list = []
    for _ in range(30):
        horde = EPSO.EliteHorde.EliteHorde(
            subpopulation_count, subpopulation_size_count, dimension,
            range_v, inertia, cognitive_force, social_const,
            iteration_limit, adaptation_func, term, acc)
        horde.run()
        data_list.append(np.mean(horde.best_particle_adaptation))
        mean_list.append(np.min(horde.mean_best_adaptation))
    Data.Plots.avg_plot(data_list, mean_list, adaptation_func, chart="EPSO-30")
    print(min(data_list))
    print(min(mean_list))


@runs.command()
@click.option("-sc", "--subpopulation_count", default=2)
@click.option("-ssc", "--subpopulation_size_count", default=2)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.45)
@click.option("-cp", "--cognitive_force", default=0.55)
@click.option("-sp", "--social_const", default=0.65)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--adaptation_func", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
@click.option("-th", "--treshold", default=50)
def run_OPSO(subpopulation_count, subpopulation_size_count, dimension,
             range_v, inertia, cognitive_force, social_const,
             iteration_limit, adaptation_func, term, acc, treshold):
    osmosis = OPSO.Osmosis.Osmosis(
        subpopulation_count, subpopulation_size_count, dimension,
        range_v, inertia, cognitive_force, social_const,
        iteration_limit, adaptation_func, term, acc, treshold)
    osmosis.run()
    Data.Plots.avg_plot(osmosis.best_particle_adaptation, osmosis.mean_best_adaptation, adaptation_func, chart="OPSO")


@runs.command()
@click.option("-sc", "--subpopulation_count", default=2)
@click.option("-ssc", "--subpopulation_size_count", default=2)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.45)
@click.option("-cp", "--cognitive_force", default=0.55)
@click.option("-sp", "--social_const", default=0.65)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--adaptation_func", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
@click.option("-th", "--treshold", default=50)
def run_OPSO_30(subpopulation_count, subpopulation_size_count, dimension,
             range_v, inertia, cognitive_force, social_const,
             iteration_limit, adaptation_func, term, acc, treshold):
    data_list = []
    mean_list = []
    for _ in range(30):
        osmosis = OPSO.Osmosis.Osmosis(
            subpopulation_count, subpopulation_size_count, dimension,
            range_v, inertia, cognitive_force, social_const,
            iteration_limit, adaptation_func, term, acc, treshold)
        osmosis.run()
        data_list.append(np.min(osmosis.best_particle_adaptation))
        mean_list.append(np.min(osmosis.mean_best_adaptation))
    Data.Plots.avg_plot(data_list, mean_list, adaptation_func, chart="OPSO-30")
    print(np.min(data_list))
    print(np.min(mean_list))


@runs.command()
@click.option("-sc", "--subpopulation_count", default=2)
@click.option("-ssc", "--subpopulation_size_count", default=2)
@click.option("-d", "--dimension", default=2)
@click.option("-r", "--range_v", default=32)
@click.option("-ip", "--inertia", default=0.45)
@click.option("-cp", "--cognitive_force", default=0.55)
@click.option("-sp", "--social_const", default=0.65)
@click.option("-i", "--iteration_limit", default=100)
@click.option("-a", "--adaptation_func", default=0)
@click.option("-t", "--term", default=0)
@click.option("-acc", "--acc", default=0.00001)
@click.option("-th", "--treshold", default=50)
def compare(subpopulation_count, subpopulation_size_count, dimension,
             range_v, inertia, cognitive_force, social_const,
             iteration_limit, adaptation_func, term, acc, treshold):
    osmosis = OPSO.Osmosis.Osmosis(
        subpopulation_count, subpopulation_size_count, dimension,
        range_v, inertia, cognitive_force, social_const,
        iteration_limit, adaptation_func, term, acc, treshold)
    osmosis.run()
    horde = EPSO.EliteHorde.EliteHorde(
        subpopulation_count, subpopulation_size_count, dimension,
        range_v, inertia, cognitive_force, social_const,
        iteration_limit, adaptation_func, term, acc)
    horde.run()
    Data.Plots.compare_plot(osmosis.best_particle_adaptation, osmosis.mean_best_adaptation, horde.best_particle_adaptation,  horde.mean_best_adaptation, adaptation_func, chart="OPSO vs EPSO")


runs.add_command(run_EPSO)
runs.add_command(run_EPSO_30)
runs.add_command(run_OPSO)
runs.add_command(run_OPSO_30)
runs.add_command(compare)

if __name__ == "__main__":
    runs()
