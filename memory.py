#!/usr/bin/python
# -*- coding:utf-8 -*-

# I.R.I.S.
# br4in

########## Imports #########
from rivescript import RiveScript
import json
import re  # Learn more
re_comment = re.compile('\s//')

# Env variables
bot_name = 'I.R.I.S.'

# Load RiveScript 
#rs = RiveScript()
#rs.load_directory("./brain")
#rs.sort_replies()


def read(filename):
    """Read a JSON config file from disk.

    @param filename: The file to read."""

    fh    = open(filename, 'r')
    lines = fh.readlines()
    data  = []

    # Allow comments in the JSON data.
    for line in lines:
        if re.match(re_comment, line):
            continue
        data.append(line)

    return json.loads("".join(data))


def write(filename, data):
    """Write JSON configuration back to disk.

    @param filename: The file to be written to.
    @param data: Python data structure to be converted."""

    fh = open(filename, 'w')
    fh.write(json.dumps(data))

# The meat of the logic is in here.This function gets a reply from the bot
# and persists user data to disk as a local file named "./$USERNAME.json"
def get_reply(bot, username, message):

    log_file = '{}.json'.format(username)
    # See if the bot knows this user yet (in its current memory).
    user_data = bot.get_uservars(username)

    if not user_data:


    # See if a local file exists for stored user variables.
        try:
    # Get content from file
                user_data = read(log_file)
    # For key, value in database, set variables in memory
                for key, value in user_data.items():
                    bot.set_uservar(username, key, value)
                    #print('User var set: {} - {}'.format(value, key))
                #print 'User vars set!'

    # On error
        except IOError as e:
            print "Unable to open file!" # doesn't exists or no perms

    # Get a reply
    reply = bot.reply(username, message)

    # Export user variables to disk
    user_data = bot.get_uservars(username)

    try:
        data = write(log_file, user_data)
    except:
        print 'Unable to write file'

    return reply

