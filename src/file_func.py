"""
This module includes functions that deal with file handling
"""

import os

def ls(directory='.'):
    """ Returns the list of files in the working directory"""
    if os.path.isdir(directory):
        file_names = list(
            map(
                lambda file: file, 
                filter(
                    lambda f: os.path.isfile(os.path.join(directory, f)), 
                    os.listdir(directory)
                )
            )
        )
        return 0, file_names
    return 1, []

def fwrite(f_name,text):
    """ Writes a string to a user specified file"""
#    import os
#    if os.path.isfile(f_name):
    try:
        with open(f_name, 'w', encoding='utf-8') as file:
            try:
                file.write(text)
                return 0, ''
            except Exception as e:
                return -1, f"Error writing to file: {str(e)}"
    except Exception as e:
        return -1, f"Error opening file: {str(e)}"