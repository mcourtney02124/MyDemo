#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides support for executing sipp scripts

"""

import os.path
import re
import sys
import shlex
import subprocess

failCount_re = re.compile(r"""^Failed.*(\d+)$""")

class SippUtils:
	def NoFailedCalls(self,script,pid):
		filePath = script[:-4] + "_" + str(pid) + "_screen.log"
		fh = None
		failCount = -1
		try:
			fh = open(filePath)
			for lino, line in enumerate(fh, start=1):
				line = line.strip()
				match = failCount_re.search(line)
				if match:
					failCount = int(match.group(1))
					print("value of failCount is",failCount)
			if failCount == 0:
				return True
			else:
				return False
		except ValueError as err:
				print("{0}: error {1} trying to read screen.log file".format(os.path.basename(sys.argv[0]),err))
				return False
		finally:
			if fh is not None:
				fh.close()
	

class SippServer:

	def __init__(self, script = "uas.xml", port  = 5060, command = ""):
		self.script = script
		self.port = str(port)
		self.command = command
		self.pid = 0

		
	def Launch(self):
		moreArgs = shlex.split(self.command)
		args = ['sipp', '-sf', self.script, '-p', self.port, '-trace_screen'] + moreArgs[:]
		p = subprocess.Popen(args)
		self.pid = p.pid
		return p
		
class SippClient(SippServer):

	def __init__(self, script = "uac.xml", target = "127.0.0.1", lport = 6060, rport  = 5060, command = ""):
		super().__init__(script, lport, command)
		self.target = target
		self.rport = str(rport)	
		
	def Launch(self):
		moreArgs = shlex.split(self.command)
		args = ['sipp', self.target + ":" + self.rport, '-sf', self.script, '-p', self.port, '-trace_screen'] + moreArgs[:]
		p = subprocess.Popen(args)
		self.pid = p.pid
		return p