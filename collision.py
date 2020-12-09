import math
from nucleus_probability import get_cross_section_dict

ATOMIC_NUMBER = {
    'D2O': 20,
    'U_235': 235,
    'U_238' : 238,
    'Zr' : 91
}
ELASTIC_ENERGY_LOSS_COEFF = {
    'D2O': 0.491,
    'U_238':0.992
}
D2O_data_directory = '/home/sourabh/Development/NUCLEAR_PROJECT/data/D2O_collision'
U_238_directory = '/home/sourabh/Development/NUCLEAR_PROJECT/data/U_238_collision'
D2O_nuclei_type = ['D_inelastic', 'O_elastic', 'D_elastic', 'O_inelastic']
U_238_nuclei_type = ['U_238_inelastic','U_238_elastic', 'U_238_capture']

def elastic_collision_energy(init_energy, nucleus):
    multiplier = ELASTIC_ENERGY_LOSS_COEFF[nucleus]
    # print(init_energy)
    # print(atomic_number)
    final_energy = multiplier*init_energy
    return final_energy

def inelastic_collision_energy(init_energy):
    return 0.4*init_energy

def get_D2O_cross_section(energy,dataframe):
    cross_section_dict = get_cross_section_dict(energy, directory=D2O_data_directory, Nuclei=D2O_nuclei_type,dataframe=dataframe)
    D2O_cross_section_dict = {}
    D2O_cross_section_dict['elastic'] = 2*cross_section_dict['D_elastic'] + cross_section_dict['O_elastic']
    D2O_cross_section_dict['inelastic'] = 2*cross_section_dict['D_inelastic'] + cross_section_dict['O_inelastic']
    return D2O_cross_section_dict

def get_U_238_cross_section(energy):
    cross_section_dict = get_cross_section_dict(energy, directory=U_238_directory,Nuclei=U_238_nuclei_type)
    U_238_cross_section_dict = {}
    U_238_cross_section_dict['elastic'] = cross_section_dict['U_238_elastic']
    U_238_cross_section_dict['inelastic'] = cross_section_dict['U_238_inelastic']
    U_238_cross_section_dict['capture'] = cross_section_dict['U_238_capture']
    return U_238_cross_section_dict

def get_collision_prob_dict(energy,dataframe,nucleus='D2O'):
    probab_dict = {}
    if nucleus=='D2O':
        cross_section_dict = get_D2O_cross_section(energy,dataframe)
    else:
        cross_section_dict = get_U_238_cross_section(energy)

    collision_type = cross_section_dict.keys()
    cross_section_list = [cross_section_dict[key] for key in cross_section_dict.keys()]
    total_cross_section = sum(cross_section_list)
    for collision in collision_type:
        probab_dict[collision] = cross_section_dict[collision]/total_cross_section
    return probab_dict


if __name__ == "__main__":

    print(get_collision_prob_dict(2.1))


