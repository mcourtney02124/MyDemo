#!/usr/bin/env python3
# Copyright (c) 2018 Meredith Courtney All rights reserved.

"""
This module provides support for executing sipp scripts

"""

import shlex
import subprocess

class SippServer:

	def __init__(self, script = "uas.xml", port  = 5060, command = ""):
		self.script = script
		self.port = str(port)
		self.command = command
		self.outfile_path = script + ".out"
		self.outfile = open(self.outfile_path,"+w")
		
	def Cleanup(self):
		self.outfile.close()

		
	def Launch(self):
		moreArgs = shlex.split(self.command)
		args = ['sipp', '-sf', self.script, '-p', self.port] + moreArgs[:]
		return subprocess.Popen(args, stdout = self.outfile, stderr = self.outfile)
		
class SippClient(SippServer):

	def __init__(self, script = "uac.xml", target = "127.0.0.1", lport = 6060, rport  = 5060, command = ""):
		super().__init__(script, lport, command)
		self.target = target
		self.rport = str(rport)	
		
	def Launch(self):
		moreArgs = shlex.split(self.command)
		args = ['sipp', self.target + ":" + self.rport, '-sf', self.script, '-p', self.port] + moreArgs[:]
		return subprocess.Popen(args, stdout = self.outfile, stderr = self.outfile)