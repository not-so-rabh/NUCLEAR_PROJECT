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
    """gives cross section data for a given nuetron energy and nucleus from a data

    Args:
        energy (int): the nuetron energy
        element (string): element whose cross section is needed
        dataframes_dict (dict): dictionary of dataframes of different element

    Returns:
        int: cross section data
    """

    # print(dataframes_dict.keys())
    dataframe = dataframes_dict[element]
    # y - Cross_section
    # x - Energy
    cross_section_data = dataframe['Sig'].values
    energy_data = dataframe['E'].values

    cross_section = np.interp(energy, energy_data, cross_section_data)

    return cross_section

def get_cross_section_dict(energy,dataframe,directory=DATA_DIRECTORY,Nuclei=Nuclei_init):
    """generate cross section dict for a given nuetron energy and dataframe

    Args:
        energy (int): energy at which the data is needed
        dataframe ([dict]): dictionary of various required dataframes
        directory (['string], optional): address where the required data is stored. Defaults to DATA_DIRECTORY.
        Nuclei (list, optional): types of nuclei in the given dataframes. Defaults to Nuclei_init.

    Returns:
        [dictionary]: different cross section data
    """
    dataframes_dict = dataframe
    # print(dataframes_dict.keys())
    cross_section_dict = {}
    for nucleus in Nuclei:
        cross_section_dict[nucleus] = cross_section(energy, nucleus, dataframes_dict)
    return cross_section_dict

def get_probability(n_sig_list, cross_section_dict, nucleus):
    """converts cross section of an element to it's probability

    Args:
        n_sig_list (list): list of cross sections
        cross_section_dict (dict): dictionary with all the cross sections
        nucleus (int): nucleus which is to be converted to probability

    Returns:
        int: probability of hitting the given cross sections
    """
    #n*sigma
    # print(cross_section_dict.keys())
    nucleus_probability = cross_section_dict[nucleus]*atom_count_dict[nucleus]/sum(n_sig_list)
    return nucleus_probability

def get_nucleus_probability_dict(energy,dataframe_dict,D2O=True):
    """generates probabilities for a particular collision event to happen

    Args:
        energy (int): nuetron energy
        dataframe_dict (dictionary): dictionary of required dataframes
        D2O (bool, optional): whether the probability needed is combined or separated atoms of D2O. Defaults to True.

    Returns:
        [type]: [description]
    """
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


