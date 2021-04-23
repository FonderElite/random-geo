PIP=/usr/bin/pip
sudo apt update
if [ -f '$PIP' ]
then
echo "pip is installed."
else
sudo apt install python3-pip
sudo pip3 install requirements.txt
fi
