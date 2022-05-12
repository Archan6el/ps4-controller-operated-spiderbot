# Darkpaw-Spiderbot-Operated-by-PS4-Dualshock-Controller

Python code to remotely control Adeept Darkpaw Spiderbot using a bluetooth connected dualshock PS4 Controller

This code is free to be expanded and improved by anyone!

Follow Adeept's tutorial for all necessary files: https://www.adeept.com/learn/tutorial-91.html

Essentially go through the entire tutorial to where all files are on the pi, and everything is set up and ready to go.

No files were modified except the ones present in this repo. SpiderG.py I personally modified, but not much. I just changed some of the motor values. ps4.py contains the code that I developed to have the PS4 Controller operate the spider bot

All files in the "startup-files" directory are used to essentially have the spiderbot autostart and have everything run right on boot:

onBoot.sh and startup.sh are both bash scripts used to get everything running when we start up the spider bot. startup.sh runs our python file, while onBoot.sh gets blueooth up and working. rc.local is the contents of the file located in "/etc/rc.local". It contains the modifications used to have startup.sh run on boot. crontab -e contains contents of my crontab on my pi that allows onBoot.sh to run on boot


Feel free to watch my development on this project: https://www.youtube.com/watch?v=gwnKjuKFL4A&t=43s
