from File_Handling.Dynamic_Path.Path_Cal import file_collect
import os

csv_copper = []

def file_collect_copper_csv():
    path = file_collect()

    for file in os.listdir(path):
        if file.startswith('Copper') and file.endswith('.csv'):

            csv_copper.append(file)
        else:
            pass

    print('Copper:',csv_copper)


file_collect_copper_csv()