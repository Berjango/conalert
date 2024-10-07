#!/bin/python

#Alerts the user when network connections get too high.A large number of connections may happen due to hackers or possibly from normal use.


#This is a quick and ugly program,don't expect any professional programming practices here,it is designed to work for me not anyone else. I still hope that in some way it will be useful to others.

# Author - Peter Wolf
# dougalite@gmail.com
# Started 7-10-2024

#Requirements - espeak, to install type "sudo apt install espeak -y" in a terminal prior to running the program

import time
import os
from subprocess import Popen
from subprocess import PIPE


toomanyconnections=80
delay=30
print("Checking network connections.")
shownmessage=False
loop=1
while 1:
	with Popen(['netstat', "-t"],stdout=PIPE) as proc:
		count=str(proc.stdout.read()).count("ESTAB")
	alertmsg="ALERT!!!!  There are "+str(count)+" connections"
	print(alertmsg)
	print("Loop= ",str(loop))
	loop+=1
	if count>toomanyconnections:
		Popen(['espeak', alertmsg])
		if not shownmessage:
			shownmessage=True
			with Popen(['zenity', "--info","--text="+alertmsg],stdout=PIPE) as proc2:
#				streamdata = proc2.communicate()[0]
#				while 0!=proc2.returncode:
#					pass
				time.sleep(0.5)
			
	time.sleep(delay)


