
import os
from genericpath import exists
from shutil import copyfile

def file_name(path_, extension=False):
    if extension:
        fn = os.path.basename(path_)
    else:
        fn = os.path.basename(path_).split(".")[0]
    return(fn)

def create_path(path_name, v = True):
    path_name = os.path.dirname(path_name)

    if not os.path.isdir(path_name):
        os.makedirs(path_name)
        if v:
            print(f"\t> created path: {path_name}")
    
    return path_name


def read_from(filename, v=False):
    '''
    a function to read ascii files
    '''
    try:
        g = open(filename, 'r')
    except:
        print(
            "\t! error reading {0}, make sure the file exists".format(filename))
        return
    file_text = g.readlines()
    if v:
        print("\t> read {0}".format(file_name(filename)))
    g.close
    return file_text



def copy_file(filename, destination_path):
    '''
    a function to copy files
    '''
    
    if not os.path.isdir(os.path.dirname(destination_path)):
        try:
            os.makedirs(os.path.dirname(destination_path))
        except:
            pass

    copyfile(filename, destination_path)


def write_to(filename, text_to_write, v=False, mode = "overwrite"):
    '''
    a function to write to file
    modes: overwrite; append
    '''
    try:
        if not os.path.isdir(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
            if v:
                print("! the directory {0} has been created".format(
                    os.path.dirname(filename)))
    except:
        pass

    if mode == "overwrite":
        g = open(filename, 'w', encoding="utf-8")
    elif mode == "append":
        g = open(filename, 'a', encoding="utf-8")
    try:
        g.write(text_to_write)
        if v:
            print('\n\t> file saved to ' + filename)
    except PermissionError:
        print("\t> error writing to {0}, make sure the file is not open in another program".format(
            filename))
        response = input("\t> continue with the error? (Y/N): ")
        if response == "N" or response == "n":
            exit()
    g.close
