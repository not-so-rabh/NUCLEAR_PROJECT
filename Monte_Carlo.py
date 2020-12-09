import random
import math
import matplotlib.pyplot as plt
import seaborn as sns
from nucleus_probability import get_nucleus_probability_dict


class MultiplicationFactor:

    def __init__(self,steps):
        # All input variables
        self.steps = steps

    @staticmethod
    def pdf(x):
        return 0.771*math.sqrt(x)*(math.exp(-0.776*x))

    @staticmethod
    def generate_random_with_dist(population, weights):
        # population = [0.000007 * i for i in range(1, 1000000)]
        # # print(population[0:20])
        # weights = [pdf(step) for step in population]
        # print(weights)
        return random.choices(population, weights)

    def fix_init_nuetron_energy(self):
        population_list = [(7/self.steps)*step for step in range(1,self.steps)]
        # print(population[0:20])
        weights_list = [self.pdf(step) for step in population_list]
        init_energy = self.generate_random_with_dist(population_list, weights_list)
        return init_energy


    def generate_nucleus_probability(self, energy):
        nuclei_prob_dict = get_nucleus_probability_dict(energy)
        weights = []
        population = []

        for key in nuclei_prob_dict.keys():
            weights.append(nuclei_prob_dict[key])
            population.append(key)

        return self.generate_random_with_dist(population, weights)



if __name__ == "__main__":
    Simulation_Instance = MultiplicationFactor(1000000)
    # print(Simulation_Instance.pdf(0))
    # i = 0
    # lst = []
    # population_list = [0.000007*i for i in range(1,1000000)]
    # # print(population[0:20])
    # weights_list = [Simulation_Instance.pdf(step) for step in population_list]
    # # print(weights[0:20])
    # print()

    # while i != 1000:
    #     lst.append(Simulation_Instance.generate_random_with_dist(population_list, weights_list))
    #     if i % 100 == 0:
    #         print(str(i) + "iterations done")
    #     i = i + 1


    # print(lst)
    # plt.clf()
    # sns.distplot(lst)
    # plt.xlim(0, 8)
    for i in range(100):
        print(Simulation_Instance.fix_init_nuetron_energy())
        print(Simulation_Instance.generate_nucleus_probability(3.1))
