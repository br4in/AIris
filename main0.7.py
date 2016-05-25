#!/usr/bin/python
# -*- coding:utf-8 -*-

# I.R.I.S.
# br4in

########## Imports #########
from rivescript import RiveScript
import time
from os import system
from speech_rec import get_command
from memory import read, write, get_reply

# Env variables
bot_name = 'AIris'

# Load RiveScript 
rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()

def say(reply):

    output = system('say "{}" &'.format(reply))
 

def login():
    log_name = raw_input('Username: ')
    return log_name

def cli_mode(log_name, bot_name):
    while True:
        msg = raw_input('{}_>'.format(log_name))
        if msg == 'quit':
        	quit()
        reply = get_reply(rs, log_name, msg)
	say(reply)
	print('{}_>{}'.format(bot_name, reply))
        

def speech_mode(log_name, bot_name):
    while True:
        msg = get_command()
        if msg == 'quit':
        	quit()
        print('{}_>{}'.format(log_name, msg))
        reply = get_reply(rs, log_name, msg)
        print('{}_>{}'.format(bot_name, reply))

# Intro -- this goes before the loop --
system('clear') 
print('Starting {}'.format(bot_name))
time.sleep(1)
print('System Started')
time.sleep(0.5)
system('clear')

# Login 
log_name = login()

# Choose betweeen cli or speech mode
items = ['Command line mode', 'Speech mode']
line = 1
# Print menu
for item in items:
    print('[{}] {}'.format(line, item))
    line += 1
# Get choice
choice = raw_input('Enter line number: ')
if choice == '1':
    cli_mode(log_name, bot_name)
elif choice == '2':
    speech_mode(log_name, bot_name)


