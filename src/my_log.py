#!/usr/bin/env python3
'''
Make logs for the toy IVR
Created on Feb 23, 2018

@author: Meredith Courtney
'''
import time

class MyLog:
    '''
    Make a log file and write to it.
    '''

    def __init__(self, filepath = "data/test.log"):
        '''
        Constructor for the transaction log.
        '''
        self.filepath = filepath
        self.logfile = open(filepath, "w", encoding = "utf08")
    
    def log_line(self, keyval, data):
        """
        Make a string of keyval (timestamp), the timestamp's readable form, and data, and write it to the specified log
        """
        self.logfile.write(keyval + "," + time.ctime(keyval) + "," + data + "\n")
        