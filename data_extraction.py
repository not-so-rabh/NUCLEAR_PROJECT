import json
import pandas as pd
import glob

DATA_DIRECTORY = 'data'

def extract_data(json_file_address):
    """function to convert json data to dataframe excludes other details

    Args:
        json_file_address (string): address of the json file to be processed

    Returns:
        Dataframe: dataframe of json data
    """

    with open(json_file_address) as json_file:
        json_data = json.load(json_file)
    data_points = json_data['datasets'][0]['pts']
    dataframe = dictionary_to_dataframe(data_points)
    return dataframe

def dictionary_to_dataframe(dict):
    """converts dictionday to data

    Args:
        dict (dictinary): dictionary to be converted

    Returns:
        DataFrame: dataframe from dictionary
    """
    return pd.DataFrame(dict)

def get_dataframes(data_directory):
    """function to convert all json files in a directory to dataframes

    Args:
        data_directory (string): directory where all json files are stored

    Returns:
        DataFrame: dataframes of all json files
    """
    list_of_files = glob.glob(data_directory + "/*.json")
    dataframe_dict = {}
    for file in list_of_files:
        name_start = len(data_directory)+1
        name_end = len(file) - 5
        dataframe_dict[file[name_start:name_end]] = extract_data(file)
    return dataframe_dict



if __name__ == "__main__":

    dataframes = get_dataframes(DATA_DIRECTORY)
    print(dataframes['U_235']['E'].values)
