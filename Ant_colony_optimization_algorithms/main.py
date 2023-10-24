import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import imageio
import uuid

import Anthill
import Ant


def read_data_from_csv(data_file):
    column_names = ["NR", "X", "Y"]
    df = pd.read_csv(data_file, names=column_names)

    nr_array = np.array(df.NR.values.tolist())
    x_axis_array = np.array(df.X.values.tolist())
    y_axis_array = np.array(df.Y.values.tolist())

    return [nr_array, x_axis_array, y_axis_array]


def visualize_data_set(x_values: np.ndarray, y_values: np.ndarray, best_ant: Ant) -> None:
    plt.scatter(
        x=x_values,
        y=y_values,
        label="max",
        color="red",
        marker="o",
    )
    trail_x = [x_values[best_ant.discovered_places[i]] for i in range(len(x_values))]
    trail_y = [y_values[best_ant.discovered_places[i]] for i in range(len(y_values))]
    plt.plot(trail_x, trail_y)
    plt.show()


def make_plot(tracks):
    x = [i for i in range(len(tracks))]
    y = [tracks[i] for i in range(len(tracks))]
    plt.plot(x, y)
    plt.show()


def make_gif(x_values: np.ndarray, y_values: np.ndarray, ants):
    filenames = []
    i = 0
    for ant in ants:
        trail_x = [x_values[ant.discovered_places[i]] for i in range(len(x_values))]
        trail_y = [y_values[ant.discovered_places[i]] for i in range(len(y_values))]
        # plot the line chart
        plt.plot(trail_x, trail_y)
        plt.scatter(
            x=x_values,
            y=y_values,
            label="max",
            color="red",
            marker="o",
        )
        plt.title(f'{i}')
        i += 1
        # create file name and append it to a list
        filename = f'{str(uuid.uuid4())}.png'
        filenames.append(filename)

        # save frame
        plt.savefig(filename)
        plt.close()
    # build gif
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove files
    for filename in set(filenames):
        os.remove(filename)


def main():
    DATA = read_data_from_csv('./data/P-n16-k8.csv')
    anthill = Anthill.Anthill(DATA, 30, 0.5, 1, 1, 0.3)
    best_ants = []
    for i in range(1000):
        anthill.find_path()
        anthill.get_best_track()
        best_ants.append(anthill.best_ant)
        anthill.ants_list = anthill.create_anthill(len(DATA[0]))
    visualize_data_set(DATA[1], DATA[2], anthill.best_ant)
    make_plot(anthill.best_tracks)
    # make_gif(DATA[1], DATA[2], best_ants)


if __name__ == '__main__':
    main()
