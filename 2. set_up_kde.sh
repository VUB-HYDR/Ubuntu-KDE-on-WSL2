# 
# 
# 
# 
# 

echo "Updating repositories and upgrading packages"
sudo apt update && sudo apt -y upgrade

echo "Installing KDE desktop to WSL"
sudo apt-get install -y kubuntu-desktop
sudo apt-get install -y lightdm

echo 'Installing and configuring xrdp'
sudo apt-get install xrdp -y
sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini
sudo sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini

echo 'enabling dbus'
sudo systemctl enable dbus
sudo /etc/init.d/dbus start
sudo /etc/init.d/xrdp start

echo 'check xrdp status'
sudo /etc/init.d/xrdp status

# get user details from user
read -p "enter username: " u_name

# save login credentials to file for shortcuts and rdp file
echo $u_name > data/login.txt

echo, "Creating an account using the username '$u_name'"

# add user and add the user to sudoers
adduser $u_name
usermod -aG sudo $u_name
