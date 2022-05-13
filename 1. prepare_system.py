
'''



'''


# import modules
import time
from os import chdir, getcwd, system, path, makedirs, remove, write, getenv
from sys import stdout, exit
from shutil import copyfile

def exists(path_):
    if path.isdir(path_):
        return True
    if path.isfile(path_):
        return True
    return False


def copy_file(filename, destination_path):
    '''
    a function to copy files
    '''
    
    if not path.isdir(path.dirname(destination_path)):
        try:
            makedirs(path.dirname(destination_path))
        except:
            pass

    copyfile(filename, destination_path)


def write_to(filename, text_to_write, v=False, mode = "overwrite"):
    '''
    a function to write to file
    modes: overwrite; append
    '''
    try:
        if not path.isdir(path.dirname(filename)):
            makedirs(path.dirname(filename))
            if v:
                print("! the directory {0} has been created".format(
                    path.dirname(filename)))
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


me = f'{path.realpath(__file__)}'

chdir(path.dirname(me))
packages_done =  exists("packages.ind")

if not packages_done:
    # install necessary modules
    system('pip install requests --user')
    system('pip install winshell --user')
    system('pip install pywin32 --user')
    system('pip install requests')
    system('pip install tqdm --user')
    system('pip install pandas --user')
    write_to("packages.ind", "Packages necessary for this script already exist")
  


# import modules
import requests
import subprocess
import winshell
import pandas
from tqdm import tqdm


# declare functions

def delete_file(file_name):
    if path.isfile(file_name):
        try:
            remove(file_name)
        except:
            print("\t! could not delete file {fn}".format(fn=file_name))
    else:
        print("\t! the file, {fn}, does not exist".format(fn=file_name))


def download_file(url, save_path, final_fn = None):

    if not final_fn is None:
        fname = final_fn
    else:
        fname = path.basename(url)

    save_dir = path.dirname(save_path)
    save_fname = "{0}/{1}".format(save_dir, fname)

    if path.isfile(save_fname):
        print("\t! the specified file already exists, skipping")
        return

    response = requests.get(url, stream=True)
    if not path.isdir(save_dir):
        makedirs(save_dir)
    with open(save_fname, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

if __name__ == '__main__':
    
    # global variables
    restart_countdown = 10
    continur_file = exists("continue.ind")
    

    if not continur_file:

        # Enable WSL and VM platform on Windows
        system("dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart")
        system("dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart")

        # need to restart
        print("\n\t your computer needs to be restarted. We will pass the command to restart after the countdown")
        write_to("continue.ind", "Set up will continue after restarting")
        batch_content = f'''%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit \nstart "python" "{me}"'''
        write_to(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\resume_setup.bat", batch_content)
        
        while restart_countdown > 0:
            stdout.write(f"\r             {restart_countdown}   "); stdout.flush()
            restart_countdown -= 1
            time.sleep(1)
        
        system("shutdown /r /t 0")
        exit() # in case the scripts starts to continue executing outside the loop

    else:
        print('\t This script was already run on this computer, go to step 2. If you run this script again, WSL & VMP will be re enabled.')
        delete_file("continue.ind")
        delete_file(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\resume_setup.bat".replace("\\\\", "/"))
        
        restart_countdown = 30
        while restart_countdown > 0:
            stdout.write(f"\r             {restart_countdown}   "); stdout.flush()
            restart_countdown -= 1
            time.sleep(1)
        