import os
from File_Handling.Dynamic_Path.Path_Cal import file_collect


csv_gold = []

def file_collect_gold_csv():
    path = file_collect() # Get dynamic path

    for file in os.listdir(path):
        if file.startswith('Gold') and file.endswith('.csv'):
            csv_gold.append(file)

    print('Gold:', csv_gold)

def path_cal():
    return os.getcwd()  # Dynamically returns the current working directory

file_collect_gold_csv()