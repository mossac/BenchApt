#!/usr/bin/python3

import _thread
import time
import slave
import os
import subprocess

# Call the client, should be call to other machine in file design
def Call_Client( threadName, delay):
   subprocess.run("slave.py 1")


# Create the threads
try:
    _thread.start_new_thread( Call_Client, ("Client-1", 0, ) )
    _thread.start_new_thread( Call_Client, ("Client-2", 0, ) )
    _thread.start_new_thread( Call_Client, ("Client-3", 0, ) )
except:
   print ("Error: unable to start thread Master")

while 1:
   pass