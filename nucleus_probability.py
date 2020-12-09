import numpy as np
from numpy.core.numeric import cross
from data_extraction import get_dataframes
from utility import atom_count_dict

DATA_DIRECTORY = '/home/sourabh/Development/NUCLEAR_PROJECT/data'
Nuclei_init = ['D_2','O_16','U_235','U_238','Zr']

"Module to generate the probabilities based on cross-sections"


def nucleus_probs():
    pass

def cross_section(energy,element,dataframes_dict):
    "Gives cross section for the given element for the given data"
    # print(dataframes_dict.keys())
    dataframe = dataframes_dict[element]
    # y - Cross_section
    # x - Energy
    cross_section_data = dataframe['Sig'].values
    energy_data = dataframe['E'].values

    cross_section = np.interp(energy, energy_data, cross_section_data)

    return cross_section

def get_cross_section_dict(energy,directory=DATA_DIRECTORY,Nuclei=Nuclei_init):
    dataframes_dict = get_dataframes(directory)
    # print(dataframes_dict.keys())
    cross_section_dict = {}
    for nucleus in Nuclei:
        cross_section_dict[nucleus] = cross_section(energy, nucleus, dataframes_dict)
    return cross_section_dict

def get_probability(n_sig_list, cross_section_dict, nucleus):
    #n*sigma
    # print(cross_section_dict.keys())
    nucleus_probability = cross_section_dict[nucleus]*atom_count_dict[nucleus]/sum(n_sig_list)
    return nucleus_probability

def get_nucleus_probability_dict(energy):
    global DATA_DIRECTORY
    global dataframes_dict
    dataframes_dict = get_dataframes(DATA_DIRECTORY)
    cross_section_dict = get_cross_section_dict(energy)
    # print(cross_section_dict.keys())
    n_sig_water = (atom_count_dict['D_2']*cross_section_dict['D_2']) + (atom_count_dict['O_16']*cross_section_dict['O_16'])
    n_sig_list = [cross_section_dict[nucleus_temp]*atom_count_dict[nucleus_temp]
                    for nucleus_temp in Nuclei_init if nucleus_temp not in ['D_2','O_16']]
    n_sig_list.append(n_sig_water)
    # print(cross_section_dict.keys())
    
    probability_dict = {}
    probability_dict['D2O'] = n_sig_water/sum(n_sig_list)
    for nucleus in Nuclei_init:
        if nucleus not in ['D_2','O_16']:
            probability_dict[nucleus] = get_probability(n_sig_list,cross_section_dict, nucleus)
    
    return probability_dict


if __name__ == "__main__":
    print(get_nucleus_probability_dict(2.2))


