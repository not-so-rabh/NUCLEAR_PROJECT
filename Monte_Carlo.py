import random
import math
import matplotlib.pyplot as plt
import seaborn as sns
from nucleus_probability import get_nucleus_probability_dict, nucleus_probs
from collision import get_collision_prob_dict,elastic_collision_energy,inelastic_collision_energy


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
        return init_energy[0]


    def generate_choices_probability(self, energy, nuclei_prob_dict=None):
        if not nuclei_prob_dict:
            nuclei_prob_dict = get_nucleus_probability_dict(energy)
        weights = []
        population = []

        for key in nuclei_prob_dict.keys():
            weights.append(nuclei_prob_dict[key])
            population.append(key)

        return self.generate_random_with_dist(population, weights)

    def generate_collision_type(self,init_energy,nuclei):
        if nuclei=='D2O':
            col_prob_dict = get_collision_prob_dict(init_energy)
            return self.generate_choices_probability(init_energy,nuclei_prob_dict=col_prob_dict)[0]
        if nuclei=='U_238':
            print('U_238_milaa re baba')
            col_prob_dict = get_collision_prob_dict(init_energy, nucleus='U_238')
            return self.generate_choices_probability(init_energy,nuclei_prob_dict=col_prob_dict)[0]
        return 'in_progress'

    @staticmethod
    def energy_post_collision(init_energy, collision_type, nucleus):
        if(collision_type=='elastic'):
            return elastic_collision_energy(init_energy,nucleus)
        if(collision_type=='inelastic'):
            return inelastic_collision_energy(init_energy,nucleus)


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
        nuetron_energy = Simulation_Instance.fix_init_nuetron_energy()
        nucleus_prob = Simulation_Instance.generate_choices_probability(nuetron_energy)[0]
        # nucleus_prob = 'U_238'
        collision_type = Simulation_Instance.generate_collision_type(nuetron_energy,nucleus_prob)
        print(nuetron_energy)
        print(collision_type)
        print(Simulation_Instance.energy_post_collision(nuetron_energy,collision_type,nucleus_prob))
