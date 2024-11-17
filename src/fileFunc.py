def ls(directory='.'):
    import os
    if os.path.isdir(directory):
        file_names = list(map(lambda file: file, filter(lambda f: os.path.isfile(os.path.join(directory, f)), os.listdir(directory))))
        return 0, file_names
    return 1, []

def fwrite(fName,text):
#    import os
#    if os.path.isfile(fName):
    try:
        file = open(fName, 'w')
        try:
            file.write(text)
            return 0, ''
        except:
            return -1, 'Error writing to file'
    except:
        return -1, 'Error opening file'
    finally:
        file.close()
