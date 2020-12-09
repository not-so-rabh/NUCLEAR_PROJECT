import json
import pandas as pd
import glob

DATA_DIRECTORY = '/home/sourabh/Development/NUCLEAR_PROJECT/data'

def extract_data(json_file_address):

    with open(json_file_address) as json_file:
        json_data = json.load(json_file)
    data_points = json_data['datasets'][0]['pts']
    dataframe = dictionary_to_dataframe(data_points)
    return dataframe

def dictionary_to_dataframe(dict):
    return pd.DataFrame(dict)

def get_dataframes(data_directory):
    list_of_files = glob.glob(data_directory + "/*.json")
    dataframe_dict = {}
    for file in list_of_files:
        name_start = len(data_directory)+1
        name_end = len(file) - 5
        dataframe_dict[file[name_start:name_end]] = extract_data(file)
    return dataframe_dict



if __name__ == "__main__":
    # data_H2 = extract_data('/home/sourabh/Development/NUCLEAR_PROJECT/data/H-2.json')
    
    # print(data_H2.head(5))
    dataframes = get_dataframes(DATA_DIRECTORY)
    print(dataframes['U_235']['E'].values)
