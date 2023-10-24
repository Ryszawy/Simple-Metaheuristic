import matplotlib.pyplot as plt
import numpy as np
import Data.functions as functions

def avg_plot(avg_list, mean, adaptation_func, chart):
    x = [i for i in range(len(avg_list))]
    plt.title(f'Adaptation for {chart} algorithm, function {functions.functions_name[adaptation_func]}')
    plt.xlabel("Iteration")
    plt.ylabel("Adaptation")
    plt.plot(x, avg_list, label="Best adaptation")
    plt.plot(x, mean, label="Mean adaptation")
    plt.legend()
    plt.show()


def compare_plot(avg_list_o, mean_o, avg_list_e, mean_e, adaptation_func, chart):
    x = [i for i in range(len(avg_list_o))]
    plt.title(f'Adaptation for {chart} algorithm, function {functions.functions_name[adaptation_func]}')
    plt.xlabel("Iteration")
    plt.ylabel("Adaptation")
    plt.plot(x, avg_list_o, label="Best adaptation OPSO")
    plt.plot(x, mean_o, label="Mean adaptation OPSO")
    plt.plot(x, avg_list_e, label="Best adaptation EPSO")
    plt.plot(x, mean_e, label="Mean adaptation EPSO")
    plt.legend()
    plt.show()