#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
import time

from src.sipp_procs import SippServer, SippClient
from src.sipp_utils import no_failed_calls, how_many_success, cleanup_screen_log


class SippTestCase(unittest.TestCase):
    """Tests for `Sipp.py`, assumed to be executed from top level directory"""

    def test_create_default_server(self):
        """Create a default SippServer object, do we get the expected data in the object?"""
        
        p = SippServer()
        self.assertTrue(p.script == "uas.xml")
        self.assertTrue(p.port == "5060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)

    def test_create_default_client(self):
        """Create a default SippClient object, do we get the expected data in the object?"""
        
        p = SippClient()
        self.assertTrue(p.script == "uac.xml")
        self.assertTrue(p.port == "6060")
        self.assertTrue(p.command == "")
        self.assertTrue(p.pid == 0)
        self.assertTrue(p.target == "127.0.0.1")
        self.assertTrue(p.rport == "5060")
        
    def test_launch_default_server(self):
        """Make a default SippServer and launch it, do we get the expected output."""
        
        p = SippServer()
        sipp_server_proc = SippServer.launch(p)
        time.sleep(5)
        try:
            outs, errs = sipp_server_proc.communicate(input = "q", timeout = 15)
        except TimeoutExpired:
            sipp_server_proc.kill()
            outs.errs = sipp_server_proc.communicate()
        
        # The script ran, took no calls, and there was a clean manual shutdown.
        self.assertTrue(no_failed_calls(p.script, p.pid))
        cleanup_screen_log(p.script,p.pid)
        
    def test_launch_server_options(self):
        """Make and launch a non-default SippServer ."""
        p = SippServer(script="uas_ivr.xml",port=7070,command="-m 1")
        self.assertTrue(p.script == "uas_ivr.xml")
        self.assertTrue(p.port == "7070")
        self.assertTrue(p.command == "-m 1")
        sipp_server_proc  = SippServer.launch(p)
        time.sleep(5)
        try:
            outs, errs = sipp_server_proc.communicate(input = "q", timeout = 15)
        except TimeoutExpired:
            sipp_server_proc.kill()
            outs.errs = sipp_server_proc.communicate()
        
        self.assertTrue(no_failed_calls(p.script, p.pid))
        cleanup_screen_log(p.script, p.pid)
        
    def test_run_1_call(self):
        """Make and launch server, make and launch client to run 1 call, both report 1 successful call."""
        ps = SippServer(command="-m 1")
        pc = SippClient(command="-m 1")
        sipp_server_proc = SippServer.launch(ps)
        time.sleep(2)
        sipp_client_proc = SippClient.launch(pc)
        time.sleep(12)
        # at this point, both processes have finished and created their trace_screen files, but make sure they are down
        try:
            outs, errs = sipp_client_proc.communicate(input = "q", timeout = 10)
        except TimeoutExpired:
            sipp_client_proc.kill()
            outs.errs = sipp_client_proc.communicate()
            
        try:
            outs, errs = sipp_server_proc.communicate(input = "q", timeout = 10)
        except TimeoutExpired:
            sipp_server_proc.kill()
            outs.errs = sipp_server_proc.communicate()
                       
        self.assertTrue(how_many_success(ps.script, ps.pid) == 1)
        self.assertTrue(how_many_success(pc.script, pc.pid) == 1)
        cleanup_screen_log(ps.script, ps.pid)
        cleanup_screen_log(pc.script, pc.pid)


