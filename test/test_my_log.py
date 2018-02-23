##!/usr/bin/env python3

# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for writing log files for the toy ivr application

"""
import unittest

import os.path
import time
from src.my_log import log_line

class MyLogTestCase(unittest.TestCase):
    """Tests for `my_log.py`, these are assumed to be executed from top level directory."""
    
    def test_log_line(self):
        """log_line: make a file named test_log and write to it."""
        logfile = MyLog()
        ts = time.time()
        logfile.log_line(ts,"this is a test line")
        logfile.logfile.close()
        
        self.assertTrue(os.path.isfile(logfile.filepath) and os.path.getsize(logfile.filepath) > 0)
