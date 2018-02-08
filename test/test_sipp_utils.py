#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for executing sipp scripts (Sipp module)

"""

import unittest
from src.SippUtils import NoFailedCalls,HowManySuccess

class SippUtilsTestCase(unittest.TestCase):
    """Tests for `SippUtils.py`, assumed to be executed from top level directory"""
    
    def test_NoFailedCalls(self):
        script = "test_data.xml"
        pid = 3875
        self.assertTrue(NoFailedCalls(script,pid))
        
    def test_HowManySuccess(self):
        script = "test_data.xml"
        pid = 3876
        self.assertTrue(HowManySuccess(script,pid) == 10)


suite = unittest.TestLoader().loadTestsFromTestCase(SippUtilsTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
