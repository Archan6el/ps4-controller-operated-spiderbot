```onBoot.sh``` and ```startup.sh``` are both bash scripts used to get everything running when we start up the spider bot. 

```onBoot.sh``` gets bluetooth up and operating and runs our ```ps4.py``` program. 

```crontab -e``` contains the contents of my crontab that runs ```onBoot.sh``` on start up.

```startup.sh``` is used to run the webserver on the spider bot. 

```rc.local``` contains the contents of the file at ```/etc/rc.local``` on your Pi that runs ```startup.sh``` on boot. 
