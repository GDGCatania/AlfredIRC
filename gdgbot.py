########################## GDG IRC BOT #######################
# 
#  Ci sono ancora un bel pò di cose da sistemare 
#	* caricare le configurazioni da file
#	* dovrebbe essere multithread
#
##############################################################



import sys
import socket
import string
import os
import MySQLdb


## SI DEVONO CARICARE DA FILE
DBHOST="192.168.56.102"
DBUSER="root"
DBPASS="root"
DBNAME="test"



## DB STUFF

def connect():
	return MySQLdb.connect(host=DBHOST,
								user=DBUSER,
								passwd=DBPASS,
								db=DBNAME)
def execute_query(db,query):
	cur = db.cursor()
	cur.execute(query)
	return cur.fetchall()


def close_db(db):
	db.close






###





### FUNCTIONS ###

def send_pong(msg):
    s.send(bytes('PONG %s\r\n' % msg))


def send_message(chan, msg):
    s.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg)))

def send_nick(nick):
    s.send(bytes('NICK %s\r\n' % nick))

def send_pass(password):
    s.send(bytes('PASS %s\r\n' % password))


def join_channel(chan):
    s.send(bytes('JOIN %s\r\n' % chan))


def part_channel(chan):
    s.send(bytes('PART %s\r\n' % chan))


def quit():
    s.send(bytes('QUIT %s\r\n'))


####


### HELPING 
def get_sender(msg):
    result = ""
    for char in msg:
        if char == "!":
            break
        if char != ":":
            result += char
    return result


def get_message(msg):
    result = ""
    i = 3
    length = len(msg)
    while i < length:
        result += msg[i] + " "
        i += 1
    result = result.lstrip(':')
    return result


def is_private(msg):
	return not msg[2].startswith('#')

def is_command(msg):
    return msg.startswith('!')

def execute_command(cmd,avaiable_commands):
    if cmd in avaiable_commands:
    	#send_message(CHAN,"eseguo !%s" % cmd)
    	c=avaiable_commands[cmd]
    	print 'output %s' % c[2]
    	print 'subgroupid %s' % c[1]
    	if c[2] is not None:
    		send_message(CHAN,'%s' % c[2])
    	for co in avaiable_commands:
    		if avaiable_commands[co][0]==c[1]:
    			print "command groupid %s\n" % avaiable_commands[co][0]
    			send_message(CHAN,'!%s' %co)
    	
    		






def parse_private_message(msg,user):
	if len(msg) >= 1:
		print ('Sender %s'  % user)
		authorized=('Gabrik','Fabyolo')
		if user in authorized:
			msg = msg.split(' ')
			options = {'!die' : command_die,
                        '!testdb':command_db
                        }                 
			if msg[0] in options:
				send_message(user,options[msg[0]]())
		else:
			send_message(user,'Not autorized!')




###### 





### COMMANDS ######


def command_die():
    send_message(CHAN, 'Bye folks')
    part_channel(CHAN)
    quit()
    sys.exit(0)


def command_db():
    db=connect()
    res=execute_query(db,'SELECT * FROM GDGIRCBot')
    close_db(db)
    #print res
    return res




#####

##### SI DEVONO CARICARE DA FILE
HOST="irc.freenode.net"
PORT=6667
NICK="GDG_Bot"
IDENT="gdgbot"
REALNAME="gdgbot"
CHAN='#GDGCatania'
readbuffer=""


print('Load commands from db....')

commands=command_db()
commands_map={}
for c in commands:
	print c[0]
	commands_map[c[0]]=(c[1],c[2],c[3])




s=socket.socket( )
s.connect((HOST, PORT))
send_nick(NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
join_channel(CHAN)



while 1:
    readbuffer=readbuffer+s.recv(1024).decode('UTF-8')
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop()
    #print readbuffer

    for line in temp:
    	print line
        single_line=string.rstrip(line)
       	single_line=string.split(single_line)
        
 	#print single_line
	if len(single_line)>=1:

		if single_line[0]=="PING" :
       	    		send_pong(single_line[1])
       	    		print('PONG!\n')

        
		if single_line[1] == 'PRIVMSG':
			sender=get_sender(single_line[0])
			message = get_message(single_line)

			if is_private(single_line):
				print('Private')
				parse_private_message(message,sender)
			else:
				print('Message in a chan\n')
				if is_command(message):
					print('Command received\n')
					cmd = message[1:].strip()
					print cmd
					execute_command(cmd,commands_map)

			
			print(sender + ": " + message)

