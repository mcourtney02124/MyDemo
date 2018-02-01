#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
from src.Sipp import SippServer,SippClient
from src.SippUtils import NoFaileCalls
import time

class SippTestCase(unittest.TestCase):
    """Tests for `Sipp.py`, assumed to be executed from top level directory"""

    def test_create_default_server(self):
        """create a default SippServer object, do we get the expected data in the object?"""
        p = SippServer()
        print ("running the test for create default SippServer")
        self.assertTrue(p.script == "uas.xml")
        self.assertTrue(p.port == "5060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)

    def test_create_default_client(self):
        """create a default SippClient object, do we get the expected data in the object?"""
        p = SippClient()
        print ("running the test for create default SippClient")
        self.assertTrue(p.script == "uac.xml")
        self.assertTrue(p.port == "6060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)
        self.assertTrue(p.target == "127.0.0.1")
        self.assertTrue(p.rport == "5060")
        
    def test_launch_default_server(self):
        """ make a default SippServer and launch it, do we get the expected output"""
        p = SippServer()
        print ("running the test for launching default SippServer")
        sippServerProc = SippServer.Launch(p)
        time.sleep(5)
        sippServerProc.terminate()
        self.assertTrue(NoFailedCalls(p.script,p.pid))

        
suite = unittest.TestLoader().loadTestsFromTestCase(SippTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
