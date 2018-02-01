#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides utilities for use with execution of sipp scripts

"""

import os.path
import re
import sys

failCount_re = re.compile(r"""^Failed.*(\d+)$""")
success_re = re.compile(r"""^Successful.*(\d+)$""")

	
def ParseScreenLog(script,pid,regexper):
	filePath = script[:-4] + "_" + str(pid) + "_screen.log"
	fh = None
	retValue = None
	try:
		fh = open(filePath)
		for lino, line in enumerate(fh, start=1):
			line = line.strip()
			match = regexper.search(line)
			if match:
				retValue = int(match.group(1))
				print("value found is",retValue)
		return retValue

	except {IOError,ValueError} as err:
		print("{0}: error {1} trying to read screen.log file".format(os.path.basename(sys.argv[0]),err))

	finally:
		if fh is not None:
			fh.close()		
	
	
def NoFailedCalls(script,pid):
	if ParseScreenLog(script,pid,failCount_re) == 0:
		return True
	else:
		return False
		
def HowManySuccess(script,pid):
	return ParseScreenLog(script,pid,success_re)
