import sys
import os
import pathlib 
from pathlib import Path

'''
Helper function that creates a new dirctory in the directory Output 
'''
def create_output_directory(format): 
    output_path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers", "Output")
    
    # Check if the directory was already made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        print('Creating new Output child Directory')
        return True
    else:
        print("Output Directory child already made")
        return False
    
'''
Helper function that creates a new directory in the parent_directory 
'''
def create_output_child_directory(parent_directory, format):
    output_path = os.path.join(pathlib.Path().absolute(), "Web_Scrapers", "Output", parent_directory)

    # Check if the directory was made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        print('Creating Child')
        return True
    else:
        print('Already Made')
        return False


'''
Helper function that creates years 1980 - 2020 directory
'''
def create_years_dir(path):

    # If this is false, creates file else just print message
    if(os.path.isdir(os.path.join(path, "1980")) == False):
        print("Creating files from 1980 to 2020")
        
        # Iterate through 1980 - 2020
        for season in range(1980, 2021):

            # Creates folder 
            os.mkdir(os.path.join(path, str(season)))
        return True

    else:
        print("Files are already created")
        return False