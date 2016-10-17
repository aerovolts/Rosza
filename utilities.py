#!/usr/bin/env python

"""Utility functions for RozsaBot."""

import config
import socket
import string

def chat_user(line):
    segment = line.split(":", 2)
    user = segment[1].split("!", 1)[0]
    return user

def chat_message(line):
    segment = line.split(":", 2)
    message = segment[-1]
    return message

def chat(sock, message):
    encoded_message = bytes("PRIVMSG #{} :{}\r\n".format(config.CHANNEL, message), 'utf-8')
    sock.send(encoded_message)
