import os
import json

def scan_all_directories(root_folder='C:\\'):
    """
    This function is used to scan all the directories in the root folder
    to identify executables. 

    Parameters:
      root_folder (str): root directory in which programs have to be scanned

    Returns: 
      exe_dict (dict): an executable dictionary

    """
    exe_dict = dict()
    for root, dirs, files in os.walk(root_folder):
        print(f"Scanning {root} directory")
        for name in files:
            (filename, ext) = os.path.splitext(name)
            if ext =='.exe':
                if filename not in exe_dict.keys():
                    exe_dict[filename] = os.path.join(root, name)
    return exe_dict

def save_exe_map(exe_map, file_name='exemap.json'):
    """
      This function is used to write the exe map dictionary to a file

      Parameters:
        exe_map (dict): dictionary consisting of executable to path mappings
        file_name (str): name of the file in which exe map has to be stored
        

      Returns: 
        nothing

      """
    with open(file_name, mode='w') as writer:
        json.dump(exe_map, writer, indent=4)

def scan_and_save():
    """
    This method will scan all the directories and 
    stores the exemap in exemap.json
    """
    # scan and save the dictionary to json file
    print("# Started Scanning your directories")
    exe_map = scan_all_directories()
    save_exe_map(exe_map)
    print("# Completed Scanning your directories")


def read_and_load():
    """
    This method will read the json file and build the dictionary.
    If the file is not present, then it will scan

    Returns:
       exe_map (dict): returns an executable map
    """
    if not os.path.exists('exemap.json'):
        scan_and_save()
    exe_map = dict()
    with open('exemap.json') as reader:
        exe_map =  json.load(reader)
    return exe_map

exe_map = read_and_load()
      
   


