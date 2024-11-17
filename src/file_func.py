"""
This module includes functions that deal with file handling
"""

def ls(directory='.'):
    """ Returns the list of files in the working directory"""
    import os
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
        file = open(f_name, 'w')
        try:
            file.write(text)
            return 0, ''
        except:
            return -1, 'Error writing to file'
    except:
        return -1, 'Error opening file'
    finally:
        file.close()
