# Darkpaw-Spiderbot-Operated-by-PS4-Dualshock-Controller

Python code to remotely control Adeept Darkpaw Spiderbot using a bluetooth connected dualshock PS4 Controller

This code is free to be expanded and improved by anyone!

Follow Adeept's tutorial for all necessary files: https://www.adeept.com/learn/tutorial-91.html

Essentially go through the entire tutorial to where all files are on the pi, and everything is set up and ready to go.

No files were modified except the ones present in this repo. SpiderG.py I personally modified, but not much. I just changed some of the motor values. ps4.py contains the code that I developed to have the PS4 Controller operate the spider bot

All files in the "startup-files" directory are used to essentially have the spiderbot autostart and have everything run right on boot. They aren't required to have the PS4 Controller operate the Spider Bot, but are useful for not having to manually run everything every time the Pi boots:

onBoot.sh and startup.sh are both bash scripts used to get everything running when we start up the spider bot. onBoot.sh gets bluetooth up and operating and runs our ps4.py program. "crontab -e" contains the contents of my crontab that runs onBoot.sh on start up. startup.sh is used to run the webserver on the spider bot. "rc.local" contains the contents of the file at "/etc/rc.local" that runs startup.sh on boot. 


Feel free to watch my development on this project: https://www.youtube.com/watch?v=gwnKjuKFL4A
