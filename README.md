# AlfredIRC
Simple IRC Bot for #GDGCatania IRC Channel

Use simple socket python libraries to work

## How to test it?

Running version is in #GDGCatania IRC Channel in [freenode IRC Network](https://webchat.freenode.net/)

## I want to run it myself 

You need to have a mysql server and a table with this structure
```
| ID | CommandName | GroupID | SubGroupID | Output |
```


An sql script to build this structure is `command_table.sql`

Then you need to edit `alfred.conf` with your login data for mysql server and irc server

Edit `access.json` for give your irc user the permission to send command to the bot

To run del bot you can do in two way:

* Running `python alfredirc.py` will run the bot in foregroud
* Running `start_bot.sh` will run the bot in backgroud

#### Operators command

As an operator you can send private messages to the bot, avaiable commands are:

* !die - shutdown the bot
* !testdb - test if db connection works by doing a select into commands table


#### Example files
  
A configuration example file is `alfred.conf` 

An access example file is `access.json`

Avaiable mode for users in access file are:

* 'o' - User is a channel operator
* 'v' - User have voice in channel
  

## What to do?

Here are some [issues](https://github.com/GDGCatania/AlfredIRC/issues)


## License

This open-source software is published under the GNU General Public License (GNU GPL) version 3. Please refer to the "LICENSE" file of this project for the full text.


