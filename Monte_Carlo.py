import random
import math
import matplotlib.pyplot as plt
import seaborn as sns


class MultiplicationFactor:

    INTERVAL_SIZE = 7/1000000

    def __init__():
        # All input variables
        pass

    @staticmethod
    def pdf(x):
        return 0.771*math.sqrt(x)*(math.exp(-0.776*x))

    # def generate_random_number(lower_limit, upper_limit, type='int'):
    #     if(type=='int'):
    #         return random.randint(lower_limit, upper_limit)
    #     else:
    #         return random.random(lower_limit, upper_limit)

    @staticmethod
    def generate_random_with_dist(population, weights):
        # population = [0.000007 * i for i in range(1, 1000000)]
        # # print(population[0:20])
        # weights = [pdf(step) for step in population]
        # print(weights)
        return random.choices(population, weights)


if __name__ == "__main__":
    Simulation_Instance = MultiplicationFactor()
    # print(Simulation_Instance.pdf(0))
    i = 0
    lst = []
    population_list = [0.000007*i for i in range(1,1000000)]
    # print(population[0:20])
    weights_list = [Simulation_Instance.pdf(step) for step in population_list]
    # print(weights[0:20])
    print()

    while i != 1000:
        lst.append(Simulation_Instance.generate_random_with_dist(population_list, weights_list))
        if i % 100 == 0:
            print(str(i) + "iterations done")
        i = i + 1


    # print(lst)
    plt.clf()
    sns.distplot(lst)
    plt.xlim(0, 8)
