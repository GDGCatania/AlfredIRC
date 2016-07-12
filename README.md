# AlfredIRC
Simple IRC Bot for #GDGCatania IRC Channel

Use simple socket python libraries to work

## How to test it?

Running version is in #GDGCatania IRC Channel in [freenode IRC Network](https://webchat.freenode.net/)

### I want to run it myself 

Just clone in and run `python install.py`

It will create a configuration file and an access file.

### Example files
  
Congiuration
  Simple json file
  
  `
  {
    "real": "alfreddebug", 
    "ident": "alfredbotdebug", 
    "dbserver": "127.0.0.1", 
    "chan": "Channel", 
    "dbname": "test", 
    "server": "irc.freenode.net", 
    "nick": "Alfred_Debug", 
    "dbuser": "root", 
    "dbpass": "root", 
    "port": 6667
  }
  `
  
Access list
  Simple json file with list of users and access mode
  * 'o' channel operator
  * 'v' voice
  
  `
  [
    {"operator": "o"},
    {"uservoice": "v"}
  ]
  `
  
  
  

### What to do?

  Read issues!

