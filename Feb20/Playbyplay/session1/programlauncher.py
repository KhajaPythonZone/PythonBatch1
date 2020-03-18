import os
import json
import argparse
import subprocess

def scan_all_directories(root_folder='C:\\Program Files'):
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

def launch_application(app, exe_map):
    """
    This function will launch application

    Parameters:
        app (str): name of the application
        exe_map (dict): executable map

    Returns:
        True if the application is found False otherwise
    """
    if app not in exe_map.keys():
        print(f"""Application {app} not found.
         If it is present and not showing, 
         please complete the scan""")
        return False
    subprocess.Popen(exe_map[app])
    return True



# This parser will help in parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '-s', '--scan', 
    help="This will scan all the directories for executables",
    action='store_true')
parser.add_argument(
    '-l', '--launch', help="This will launch an executable entered")
parser.add_argument(
    '-a', '--alias', help= "Alias for current application",
    action="store_true"
)

parser.add_argument(
    '-o', '--old', help='Existing App name'
)

parser.add_argument(
    '-n', '--new', help='New App Name' 
)

args = parser.parse_args()
exe_map = dict()
if args.scan:
    scan_and_save()
else:
    exe_map = read_and_load()
    pass

if args.launch:
    launch_application(args.launch, exe_map)

if args.alias:
    old_app = args.old
    if old_app not in exe_map.keys():
        print("Invalid old name")
        exit(1)
    else:
        exe_map[args.new] = exe_map[old_app]
        save_exe_map(exe_map)

