import functions as f
import Item as item
import genetic_algorithm as ga

if __name__ == '__main__':
    DATA = f.readData('data.csv')
    ITEMS = [item.Item(DATA[0][i], DATA[1][i], DATA[2][i], DATA[3][i]) for i in range(0, 26)]

    test = ga.Genetic(ITEMS, 6404180, 1000, 26, 100, 5, 0.75, 0.02)
    test.create_cycle()
    test.make_plot()
