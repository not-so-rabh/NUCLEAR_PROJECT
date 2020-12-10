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

def get_cross_section_dict(energy,dataframe,directory=DATA_DIRECTORY,Nuclei=Nuclei_init):
    dataframes_dict = dataframe
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

def get_nucleus_probability_dict(energy,dataframe_dict,D2O=True):
    global DATA_DIRECTORY
    global dataframes_dict
    # dataframes_dict = get_dataframes(DATA_DIRECTORY)
    dataframe_dict = dataframe_dict
    cross_section_dict = get_cross_section_dict(energy,dataframe=dataframe_dict)
    # print(cross_section_dict.keys())
    
    
    # print(cross_section_dict.keys())
    excluded = []
    probability_dict = {}
    if D2O:
        excluded = ['D_2','O_16']
        n_sig_water = (atom_count_dict['D_2']*cross_section_dict['D_2']) + (atom_count_dict['O_16']*cross_section_dict['O_16'])
        n_sig_list = [cross_section_dict[nucleus_temp]*atom_count_dict[nucleus_temp]
                    for nucleus_temp in Nuclei_init if nucleus_temp not in excluded]
        n_sig_list.append(n_sig_water)
        probability_dict['D2O'] = n_sig_water/sum(n_sig_list)
        excluded = ['D_2','O_16']
    else:
        n_sig_list = [cross_section_dict[nucleus_temp]*atom_count_dict[nucleus_temp]
                    for nucleus_temp in Nuclei_init if nucleus_temp not in excluded]
    for nucleus in Nuclei_init:
        if nucleus not in excluded:
            probability_dict[nucleus] = get_probability(n_sig_list,cross_section_dict, nucleus)
    # if not D2O:
    #     probability_dict['D_2'] = 2*probability_dict['D_2']
    # print(probability_dict)
    return probability_dict


if __name__ == "__main__":
    print(get_nucleus_probability_dict(2.2,D2O=False,dataframe_dict=get_dataframes(DATA_DIRECTORY)))


