# Darkpaw-Spiderbot-Operated-by-PS4-Dualshock-Controller

Python code to remotely control an Adeept Darkpaw Spiderbot using a bluetooth connected dualshock PS4 Controller

**Clone this repo with:**
```
git clone https://github.com/Archan6el/darkpaw-spiderbot-operated-by-dualshock4-controller
```

Follow Adeept's tutorial for all necessary files: https://www.adeept.com/learn/tutorial-91.html

Essentially go through the entire tutorial to where all files are on the pi, and everything is set up and ready to go.

No files were modified except the ones present in this repo. ```SpiderG.py``` I personally modified, but not much. I just changed some of the motor values. ```ps4.py``` contains the code that I developed to have the PS4 Controller operate the spider bot

All files in the ```startup_files``` directory are used to essentially have the spiderbot autostart and have everything run right on boot. They aren't required to have the PS4 Controller operate the Spider Bot, but are useful for not having to manually run everything every time the Pi boots:

Feel free to watch my development on this project: https://www.youtube.com/watch?v=gwnKjuKFL4A
