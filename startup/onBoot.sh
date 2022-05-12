#!/bin/sh
sleep 2
sudo systemctl restart bluetooth
sleep 5
sudo systemctl restart bluetooth
sleep 3
sudo python3 adeept_darkpaw/server/ps4.py
#bluetooth is restarted multiple times on boot because connecting to the bluetooth PS4 controller is very finnicky. A restart will usually do the trick but not always
#A double restart is used just in case
