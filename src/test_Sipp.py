#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
import Sipp
import os.path

class SippTestCase(unittest.TestCase):
    """Tests for `Sipp.py`."""

    def test_create_default_server(self):
        """create a default SippServer object, do we get the expected data in the object?"""
        p = Sipp.SippServer()
        print ("running the test for create default SippServer")
        self.assertTrue(p.script == "uas.xml")
        self.assertTrue(p.port == "5060")
        self.assertTrue(p.command == "")
        self.assertTrue(os.path.isfile(p.outfile_path))

    def test_create_default_client(self):
        """create a default SippClient object, do we get the expected data in the object?"""
        p = Sipp.SippClient()
        print ("running the test for create default SippClient")
        self.assertTrue(p.script == "uac.xml")
        self.assertTrue(p.port == "6060")
        self.assertTrue(p.command == "")
        self.assertTrue(os.path.isfile(p.outfile_path))
        self.assertTrue(p.target == "127.0.0.1")
        self.assertTrue(p.rport == "5060")

if __name__ == '__main__':
    unittest.main()
