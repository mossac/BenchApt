#!/usr/bin/python3

import _thread
import time
import sys 

def first_thread( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def second_thread( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def third_thread( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


def start():
    one = "Thread-1 "
    two = "Thread-2 "
    three = "Thread-3 "
    try:
        _thread.start_new_thread( first_thread, (one, 2, ) )
        _thread.start_new_thread( second_thread, (two, 4, ) )
        _thread.start_new_thread( third_thread, (three, 6, ) )
    except:
        print ("Error: unable to start thread Slave")

    while 1:
            pass

start()