  

## Installation of Ubuntu with KDE-Plasma on WSL2 for Windows 10 and Windows 11

-----

  

This repository hosts files necessary to install ubuntu with KDE desktop
on WSL2.

![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/icon.bmp)

### Before you install

Installing a setup like the one described in this guide aims at having
the benefits of using Windows and Linux, without the inconvenience of
dual booting and without the performance hit suffered by virtualized
software.

  

### Why this set up?

Linux on WSL has many distributions available. While it may take effort
to set up a GUI for some of them, having the options even if it is just
access to the terminal, is awesome.

Access to the terminal means you do not need to load an entire desktop
environment (DE) just to run a simple command. The ability to launch the
terminal in ‘current window’ from file explorer also makes it easy to
use the terminal from specified locations. This also means access to
windows files from the Linux side: a shared files system allows you to
get the best of both sides in your workflow.

With a full-blown DE, you can open and use both Windows and Linux where
you can minimize the Linux DE or have each on a separate screen if you
have two screens. This is a dream set-up for some.

There is also a shared internet. Thus, if you set up your internet
connection for Windows (especially in institutional departments that
give assigned IP addresses), your Linux installation uses the same
connection.

  

### What are the drawbacks?

The installation needs administrator privileges which may not be
available for the user in some institutions.

Another annoyance is that there is no hardware accelerated graphics in
the Linux DE. This means the graphics are not as smooth but general
performance is not affected.

### Installation

The installation has been subdivided into several steps.

Initial guide was just one script that downloaded and installed
everything. However due to a few changes in ubuntu updates, this script
will need to be updated.

1.  #### Preparations
    
    To prepare for installation, you need to run a python script in
    PowerShell as an administrator. To do this, search for PowerShell.
    Right-click and select run as administrator.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/opening_powershell.png)
    
    Change directory to the scripts directory and run script 1
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/run-script-1.png)
    
    Your computer will restart after the script finishes executing.

2.  #### Download and install Ubuntu 20.04
    
    Before you install ubuntu you will need to upgrade your Linux kernel
    and set WSL to version 2 as default WSL. Download and install WL
    update from here:
    
    [https://wslstorestorage.blob.core.windows.net/wslblob/wsl\_update\_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi%20)
    
    Download Ubuntu 20.04 from this URL:
    <http://li1512-89.members.linode.com/assets/downloads/Ubuntu20.04.AppxBundle>
    (which will later be changed to
    <https://hydr.vub.be/assets/downloads/Ubuntu20.04.AppxBundle> )
    
    Double click the downloaded file and click install to install Ubuntu
    20.04.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/install-ubuntu.png)
    
    Once the install is complete, click launch and Ubuntu will install
    and prompt you to enter username. Do NOT enter anything. Please
    close the window at this point.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/open-bash-first-time.png)

3.  #### Install KDE Desktop Environment and set up accounts
    
    Open the scripts directory and right click in the directory while
    holding the shift button. Select the option
    <span style="color: orange;">‘Open Linux shell’</span> here.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/run-script-2.png)
    
    Now you can run script number 2 in bash to install KDE DE and set up
    accounts by running the command <span style="color: orange;">‘bash
    2.\\ set\_up\_kde.sh’</span>.
    
    This script will take a few minutes to run. Select OK if you see a
    prompt. On the prompt for display manager, select
    <span style="color: orange;">‘lightdm’</span>.
    
    You will be asked to enter a username (Recommended: use your VUB
    netid) and password for your user account and more details for your
    account. Please fill as appropriate.

4.  #### Set Up Shortcuts
    
    The third script will set shortcuts for logging into your Ubuntu DE.
    Make sure you are in the
    <span style="color: orange;">‘scripts’</span> directory within
    PowerShell. Run the script <span style="color: orange;">‘3.
    Set\_shortcuts.py’</span> <span style="color: orange;">“python ‘3.\\
    set\_shortcuts.py’”</span>
    
    You can now add the shortcut to your start menu by searching “Ubuntu
    KDE” and clicking “Add to Start”. This shortcut will allow you to
    access the newly installed DE. You can also add “Ubuntu 20.04.4 LTS”
    to the start menu to access the terminal directly.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/pin-shortcuts.png)
