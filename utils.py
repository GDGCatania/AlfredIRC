#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import json


def load_access_file(filename):
	with open(filename) as data_file:
		data = json.load(data_file)

	return data

def load_configuration(filename):
	conf={}
	config = ConfigParser.ConfigParser()
	config.read(filename)
	
	sections = config.sections()		
	
	for section in sections:
		options = config.options(section)
		for option in options:
			try:
				conf[option]=config.get(section,option)
			except:
				print("exception on %s!" % option)
				conf[option]=None
	return conf
				
	
