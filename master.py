#!/usr/bin/python3

import _thread
import time
import slave
import os
import subprocess

# Define a function for the thread
def Call_Client( threadName, delay):
   subprocess.run("slave.py 1")


# Create two threads as follows
try:
    _thread.start_new_thread( Call_Client, ("Client-1", 0, ) )
    _thread.start_new_thread( Call_Client, ("Client-2", 0, ) )
    _thread.start_new_thread( Call_Client, ("Client-3", 0, ) )
except:
   print ("Error: unable to start thread Master")

while 1:
   pass