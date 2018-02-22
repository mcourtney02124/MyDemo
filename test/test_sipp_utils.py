#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides unit tests for utility functions used with sipp execution (the sipp_procs module).

"""

import os.path
import shutil
import unittest

from src.sipp_utils import no_failed_calls, how_many_success, cleanup_screen_log, empty_screen_log


class SippUtilsTestCase(unittest.TestCase):
    """Tests for `sipp_utils.py`, these are assumed to be executed from top level directory."""
    
    def test_no_failed_calls(self):
        """no_failed_calls: check a saved sipp screen log for a run that had 0 failed calls."""
        script = "test_data.xml"
        pid = 3875
        self.assertTrue(no_failed_calls(script,pid))
        
    def test_how_many_success(self):
        """how_many_success: check a saved sipp screen log for a run that had 10 successful calls."""
        script = "test_data.xml"
        pid = 3876
        self.assertTrue(how_many_success(script,pid) == 10)

    def test_cleanup_screen_log(self):
        """cleanup:screen_log: delete sipp screen log from the data directory, identified by script name and process id."""
        file_path = "data/test_data_3877_screen.log"
        try:
            shutil.copy("data/test_data_3876_screen.log", file_path)
        except IOError:
            self.fail(msg="could not make test file to be deleted")
            return
            
        script = "test_data.xml"
        pid = 3877
        cleanup_screen_log(script, pid)
        self.assertFalse(os.path.isfile(file_path))
        
    def test_empty_screen_log(self):
        """ File must exist and have size 0. """
        script = "test_data.xml"
        pid = 3876
        self.assertFalse(empty_screen_log(script,pid))
        pid = 0
        self.assertFalse(empty_screen_log(script,pid))
        pid = 3878
        self.assertTrue(empty_screen_log(script,pid))
