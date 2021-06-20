# importing os module
import os
import shutil
import os.path
from zipfile import ZipFile

# Directory
directory = os.getcwd()
cache_path = directory + "/cache"
zip_path = directory + "/data.zip"

def clean_cache():
    # Kijk of folder al bestaat
    isdir = os.listdir(directory)
    # Check of cache folder in dir staat, als ja dan verwijderen
    if 'cache' in isdir:
        shutil.rmtree(cache_path)
    else:
        # Maak folder aan
        os.mkdir(cache_path)
    return

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
        full_path = os.path.abspath(path)
        if os.path.isfile(full_path):
            resultlist.append(full_path)
    return resultlist



def find_password(resultlist, find_string):
    # loop langs alle files
    for f in resultlist:
        with open(f, 'r') as read_obj:
            # Read all lines in the file one by one
            line_number = 0
            for line in read_obj:
                # For each line, check if line contains the string
                line_number += 1
                if find_string in line:
                    # If yes, then add the line number & line as a tuple in the list
                    return line[line.find(' ')+1:].rstrip()

if    __name__ == "__main__":
    clean_cache()
    cache_zip(zip_path, cache_path)
    lst = cached_files()
    print(lst)
    find_password(lst, 'password')