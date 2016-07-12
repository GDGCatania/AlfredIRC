#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json

CONF_FILE='alfred.conf'
ACCESS_FILE='access.json'

def save_configuration(configuration):
	with open(CONF_FILE,'w') as f:
		f.write(json.dumps(configuration,indent=4))
	print '[  OK  ] Configuration saved on: %s\n' % CONF_FILE

def save_access(access):
	with open(ACCESS_FILE,'w') as f:
		f.write(json.dumps(access,indent=4))
	print '[  OK  ] Access saved on: %s\n' % ACCESS_FILE



def main():
	conf={}
	access={}
	
	print '#######################'
	print '###### AlfredIRC ######'
	print '######   Setup   ######'
	print '#######################'
	
	server = raw_input('IRC Server> ')
	
	conf['server']=server
	
	port = int(raw_input('Port> '))
	
	conf['port']=port
	
	nick = raw_input('Nick> ')
	
	conf['nick']=nick

	ident = raw_input('Ident> ')
	
	conf['ident']=ident

	real = raw_input('Real name> ')
	
	conf['real']=real
	
	chan = raw_input('Channel (omitt #)> ')
	
	conf['chan']='#'+chan

	print ' DB Configuration\n'

	dbserver = raw_input('DB Server> ')
	
	conf['dbserver']=dbserver

	dbuser = raw_input('DB User> ')
	
	conf['dbuser']=dbuser

	dbpass = raw_input('DB Password> ')
	
	conf['dbpass']=dbpass

	dbname = raw_input('DB Name> ')
	
	conf['dbname']=dbname
	
	print ' Config Admin User \n'

	nick = raw_input('Nick of admin user> ')

	access[nick]='o'

	save_configuration(conf)
	
	save_access(access)

	print 'Now you can start the bot by simply type: ./start_bot.sh\n'

	
	







if __name__=='__main__':
	main()
