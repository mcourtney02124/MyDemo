#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
import Sipp
import os.path
import time

class SippTestCase(unittest.TestCase):
    """Tests for `Sipp.py`."""
    
    def test_NoFailedCalls(self):
        script = "uas_ivr.xml"
        pid = 3875
        self.assertTrue(Sipp.SippUtils.NoFailedCalls(self,script,pid))

    def test_create_default_server(self):
        """create a default SippServer object, do we get the expected data in the object?"""
        p = Sipp.SippServer()
        print ("running the test for create default SippServer")
        self.assertTrue(p.script == "uas.xml")
        self.assertTrue(p.port == "5060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)
        p.Cleanup()

    def test_create_default_client(self):
        """create a default SippClient object, do we get the expected data in the object?"""
        p = Sipp.SippClient()
        print ("running the test for create default SippClient")
        self.assertTrue(p.script == "uac.xml")
        self.assertTrue(p.port == "6060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)
        self.assertTrue(p.target == "127.0.0.1")
        self.assertTrue(p.rport == "5060")
        p.Cleanup()
        
    def test_launch_default_server(self):
        """ make a default SippSserver and launch it, do we get the expected output in the stdout file"""
        p = Sipp.SippServer()
        print ("running the test for launching default SippServer")
        sippServerProc = Sipp.SippServer.Launch(p)
        time.sleep(5)
        sippServerProc.terminate()
        p.Cleanup()
        

if __name__ == '__main__':
    unittest.main()
