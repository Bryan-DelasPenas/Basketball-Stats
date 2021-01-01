import sys
import os
import pathlib 
from pathlib import Path

'''
Helper function that creates a new dirctory in the directory Output 
'''
def create_output_directory(format): 
    output_path = os.path.join(pathlib.Path().absolute(), "Output")
    
    # Check if the directory was already made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        return True
    else:
        return False
    
'''
Helper function that creates a new directory in the parent_directory 
'''
def create_output_child_directory(parent_directory, format):
    output_path = os.path.join(pathlib.Path().absolute(), "Output", parent_directory)

    # Check if the directory was made
    if(os.path.isdir(os.path.join(output_path, format)) == False):
        os.mkdir(os.path.join(output_path,format))
        return True
    else:
        return False
