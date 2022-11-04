'''
This scripts installs Ubuntu KDE on WSL2

You need to make sure that the latest kernel for WSL 2 is installed
and that WSL is already 

'''
from pySmartDL import SmartDL
from data.cjfxlite import create_path, os, write_to, copy_file, read_from
from genericpath import exists
from data.rdp_file import rdp_fc

dest = create_path("/wsl/ubuntu-22.04/image/")
create_path("/wsl/ubuntu-22.04/instance/")

url = 'http://hydr.vub.be/assets/downloads/jammy-server-cloudimg-amd64-wsl.rootfs.tar.gz'

obj = SmartDL(url, dest)
obj.start()
path = obj.get_dest()


# wsl --import <distroname> <location of instance> <location of download>
os.system(f"wsl --import ubuntu-22.04 /wsl/ubuntu-22.04/instance {path}")

# checking if successful
os.system("wsl --list --all -v")

# set it as default distro
os.system('wsl --setdefault ubuntu-22.04')

# launch it
os.system('wsl -d ubuntu-22.04')

# set up ubuntu
os.system('bash -e ./data/set_up_ubutu.sh')

me = f'{os.path.realpath(__file__)}'

os.chdir(os.path.dirname(me))
packages_done =  exists("./data/packages.ind")

if not packages_done:
    # install necessary modules
    os.system('pip install requests --user')
    os.system('pip install winshell --user')
    os.system('pip install pywin32 --user')
    os.system('pip install pandas --user')
    write_to("./data/packages.ind", "Packages necessary for this script already exist")

# import modules
import winshell

username = read_from("./data/username.txt")[0].strip()
# username = read_from("./data/username.txt")[0]

print("Setting up shortcuts")
write_to(f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.rdp", rdp_fc.format(user_name = username))
write_to(f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.bat", '"' + f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.rdp" + '"')
# create shortcut
copy_file("data/Plasma_coloured_logo.ico", f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\UbuntuKDE.ico")
with winshell.shortcut(f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.lnk") as link:
    link.path = f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\Ubuntu KDE.bat"
    link.description = "Start WSL Ubuntu KDE Session"
    link.arguments = ""
    link.icon_location = (f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Ubuntu KDE\\UbuntuKDE.ico", 0)
    link.working_directory = "C:/"



