#!/bin/sh
sleep 2
sudo systemctl restart bluetooth
sleep 5
sudo systemctl restart bluetooth
sleep 3
sudo python3 adeept_darkpaw/server/ps4.py
