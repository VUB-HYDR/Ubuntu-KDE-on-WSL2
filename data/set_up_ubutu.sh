# !/bin/bash

# update packages
sudo apt-get update && sudo apt-get upgrade -y

# install kubuntu desktop
sudo apt-get install neofetch -y && neofetch
sudo apt-get install kubuntu-desktop -y

sudo apt-get install -y lightdm


echo 'Installing and configuring xrdp'
sudo apt-get install xrdp -y
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini
sudo adduser xrdp ssl-cert

echo 'enabling dbus'
# sudo systemctl enable dbus
sudo /etc/init.d/dbus start
sudo /etc/init.d/xrdp start

# make sure session uses KDE Plasma
sudo cp ./data/startwm.sh /etc/xrdp/startwm.sh

sudo service xrdp restart
# sudo /etc/init.d/xrdp status

sudo ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target


# get user details from user
read -p "enter username: " u_name

# save login credentials to file for shortcuts and rdp file
echo $u_name > data/username.txt

echo "Creating an account using the username '$u_name'"

# add user and add the user to sudoers
adduser $u_name
read -p "enter account password again (will be needed for GUI): " u_pass
echo $u_pass > data/passcode.txt

usermod -aG sudo $u_name

exit
