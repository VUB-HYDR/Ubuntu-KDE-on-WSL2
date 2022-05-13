'''



'''
from distutils.command.config import config
import winshell
from os import chdir, getcwd, getenv, makedirs, path, remove, system, write
from shutil import copyfile


def copy_file(filename: str, destination_path: str) -> None:
    '''
    Function to copy a file. The function will create a path if it does not exist.

    filename: the file path to the file being copied
    destination_path: path to the new file destination
    '''
    
    if not path.isdir(path.dirname(destination_path)):
        try:
            makedirs(path.dirname(destination_path))
        except: pass

    copyfile(filename, destination_path)


def read_from(filename: str) -> list:
    '''
    Function to read ascii files

    filename: the path to the ascii file that needs to be read
    '''
    try:
        g = open(filename, 'r')
    except:
        print("\t! error reading {0}, make sure the file exists".format(filename))
        quit()
    file_text = g.readlines()
    g.close

    return file_text


def write_to(filename: str, text_to_write: str, mode: str = "overwrite") -> None:
    '''
    Function to write to file. All strings are writen with utf-8 encoding. The function will create a path if it does not exist.

    filename: the path to the file that is being writen
    text_to_write: the string that should be writen to file
    mode: mode of writing to 'filename'
          overwite --> replaces contents of any existing file with
          append   --> adds the new contents at the end of any existing file.
    '''
    try:
        if not path.isdir(path.dirname(filename)):
            makedirs(path.dirname(filename))
    except: pass

    if mode == "overwrite":
        g = open(filename, 'w', encoding="utf-8")
    elif mode == "append":
        g = open(filename, 'a', encoding="utf-8")
    
    try:
        g.write(text_to_write)
    except PermissionError:
        print(f"\t> error writing to {filename}, make sure the file is not open in another program")
        response = input("\t> continue even with this error? (Y/N): ")
        if response == "N" or response == "n":
            exit()
    g.close



# set WSL2 as default
print('\nsetting WSL2 as default')
system("wsl --set-default-version 2")

config = {}

config["username"] = read_from("data/login.txt")[0].strip()
config["desktop_width"] = 1920
config["desktop_height"] = 1080

rdp_fc_list, rdp_fc = read_from("data/rdp_template.txt"), ""

for line in rdp_fc_list:
    rdp_fc += line

print('\nsetting {username} default user'.format(**config))
system("ubuntu2004 config --default-user {username}".format(**config))

print("Setting up shortcuts")
write_to(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.rdp", rdp_fc.format(**config))
write_to(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\start_xrdp.bat", "ubuntu2004 config --default-user root\nbash -c 'sudo service xrdp restart'\nubuntu2004 config --default-user {username}".format(**config))
write_to(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.bat", '"' + f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.rdp" + '"')

# create shortcut
copy_file("data/Plasma_coloured_logo.ico", f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\UbuntuKDE.ico")

with winshell.shortcut(f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.lnk") as link:
    link.path = f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.bat"
    link.description = "Start WSL Ubuntu KDE Session"
    link.arguments = ""
    link.icon_location = (f"{getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\UbuntuKDE.ico", 0)
    link.working_directory = "C:/"