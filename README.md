  

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


3.  #### Install KDE Desktop Environment, set up accounts and Set Up Shortcuts
    
    run script 2, '2. set-up-ubuntu-kde.py'.

    After it completes, you can add the shortcut to your start menu by searching “Ubuntu
    KDE” and clicking “Add to Start”. This shortcut will allow you to
    access the newly installed DE. You can also add “Ubuntu 22.04.4 LTS”
    to the start menu to access the terminal directly.
    
    ![](https://github.com/VUB-HYDR/Ubuntu-KDE-on-WSL2/blob/main/data/pin-shortcuts.png)
