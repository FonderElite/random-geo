PIP=/usr/bin/pip
DEP=/home/kali/requirements.txt
sudo apt update
modules=(geopy geocoder colorama requests)
if [ -f '$PIP' ]
then
echo "pip is installed."
else
sudo apt install python3-pip
for i in ${modules[@]}
do
sudo pip3 install $i
done
fi
