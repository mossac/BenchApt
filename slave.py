#!/usr/bin/python3
#To Do:
#Change print statements to file writes 
#
import _thread
import time
import sys 
import psutil

def first_thread( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def readout( threadName, delay):
   count = 0
   while 1:
      time.sleep(delay)
      count += 1
      print("CPU Average Load over 1,5 and 15 Seconds ", psutil.getloadavg())
      print("Memory Usage", psutil.virtual_memory())

def heartbeat( threadName, delay):
   count = 0
   while 1:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


def start():
    one = "Thread-1 "
    two = "Thread-2 "
    three = "Thread-3 "
    try:
        _thread.start_new_thread( first_thread, (one, 2, ) )
        _thread.start_new_thread( readout, (two, 4, ) )
        _thread.start_new_thread( heartbeat, (three, 6, ) )
    except:
        print ("Error: unable to start thread Slave")

    while 1:
            pass

start()