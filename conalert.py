#!/bin/python

#Alerts the user when network connections get too high.A large number of connections may happen due to hackers or possibly from normal use.


#This is a quick and ugly program,don't expect any professional programming practices here,it is designed to work for me not anyone else. I still hope that in some way it will be useful to others.

# Author - Peter Wolf
# dougalite@gmail.com
# Started 7-10-2024


import time
import os
from subprocess import Popen
from subprocess import PIPE



toomanyconnections=80
delay=3
print("Checking network connections.")
while 1:
	with Popen(['netstat', "-t"],stdout=PIPE) as proc:
		count=str(proc.stdout.read()).count(":")
	if count>toomanyconnections:
		alertmsg="ALERT!!!!  There are "+str(count)+" connections"
		with Popen(['zenity', "--info","--text="+alertmsg],stdout=PIPE) as proc2:
			streamdata = proc2.communicate()[0]
			while 0!=proc2.returncode:
				time.sleep(0.5)
			exit(0)
	time.sleep(delay)


