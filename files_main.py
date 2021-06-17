# importing os module
import os
import os.path
from zipfile import ZipFile

# Directory
directory = "Charlottes_dir"

zip_path = "D:/PythonProjecten/data.zip"
cache_path = "D:\PythonProjecten\Charlotte\Charlottes_dir"

# Parent Directory path
parent_dir = "D:/PythonProjecten/Charlotte"
# Path
path = os.path.join(parent_dir, directory)

def clean_cache():
    # Kijk of the folder al bestaat
    isdir = os.path.isdir(path)
    if isdir:
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
    else:
        # maak en folder aan
        os.mkdir(path)

def cache_zip(zip_file_path, cache_dir_path):
    # Haal zip file op uit zip_file_path

    # unpack zip file en schrijf weg naar cache_dir_path
    with ZipFile(zip_file_path, 'r') as zipObj:
    # Extract all the contents of zip file in current directory
        zipObj.extractall(cache_dir_path)

def cached_files():
    # Return the paths of the files in a list
    resultlist = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        if os.path.isfile(full_path):
            resultlist.append(full_path)
    return resultlist

def find_password(list_with_filepaths, find_string):
    # loop langs alle files
    list_of_results = []
    for f in list_with_filepaths:
        f_open = open(f)
        if (find_string in f_open.read()):
            with open(f, 'r') as read_obj:
                # Read all lines in the file one by one
                line_number = 0
                for line in read_obj:
                    # For each line, check if line contains the string
                    line_number += 1
                    if find_string in line:
                        # If yes, then add the line number & line as a tuple in the list
                        list_of_results.append(line.rstrip())
    print(list_of_results)


clean_cache()
cache_zip(zip_path, cache_path)
lst = cached_files()
print(lst)
find_password(lst, 'password')