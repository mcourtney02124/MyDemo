#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
from src.Sipp import SippServer,SippClient
from src.SippUtils import NoFailedCalls
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
        try:
            outs, errs = sippServerProc.communicate(input = "q", timeout = 15)
        except TimeoutExpired:
            sippServerProc.kill()
            outs.errs = sippServerProc.communicate()
        
        self.assertTrue(NoFailedCalls(p.script,p.pid))
        
    def test_launch_server_options(self):
        """ make a non-default SippServer """
        p = SippServer(script="uas_ivr.xml",port=7070,command="-m 1")
        print("running the test for creating and launching non-default SippServer")
        self.assertTrue(p.script == "uas_ivr.xml")
        self.assertTrue(p.port == "7070")
        self.assertTrue(p.command == "-m 1")
        sippServerProc  = SippServer.Launch(p)
        time.sleep(5)
        try:
            outs, errs = sippServerProc.communicate(input = "q", timeout = 15)
        except TimeoutExpired:
            sippServerProc.kill()
            outs.errs = sippServerProc.communicate()
        
        self.assertTrue(NoFailedCalls(p.script,p.pid))
        
    def test_run_1_call(self):
        " make and launch server, make and launch client to run 1 call, both report 1 successful call"
        ps = SippServer(command="-1")
        pc = SippClient(command="-m 1")
        sippServerProc = SippServer.Launch(ps)
        time.sleep(2)
        sippClientProc = SippClient.Launch(pc)
        time.sleep(12)
        # at this point, both processes have finished and created their trace_screen files
        self.assertTrue(HowManySuccess(ps.script,ps.pid)==1)
        self.assertTrue(HowManySuccess(pc.script,pc.pid)==1)
        #make sure the processes are down, in case something went wrong
        sippServerProc.kill()
        sippClientProc.kill()
        

        
suite = unittest.TestLoader().loadTestsFromTestCase(SippTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
