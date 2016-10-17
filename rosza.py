#!/usr/bin/env python

"""The main code behind the Twitch chat bot RozsaBot."""

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "1.0"

import re
import socket
import string
import sys
import time
import config
import utilities

def main():
    # Twitch IRC Connection/Networking - Change values in config.py
    irc = socket.socket()
    try:
        irc.connect((config.HOST, config.PORT))
    except:
        print("Error: Failed to connect to the specified host: " + config.host)
        sys.exit("\n" + "Please check your host configuration and try again")
    irc.send("PASS {p}\r\n".format(p=config.PASSWORD).encode("utf-8"))
    irc.send("NICK {n}\r\n".format(n=config.NICKNAME).encode("utf-8"))
    irc.send("JOIN #{c}\r\n".format(c=config.CHANNEL).encode("utf-8"))

    # Successful bot connection message to the Twitch channel.
    utilities.chat(irc, "Hello @" + config.CHANNEL + ", I am ready to go!")

    while True:
        irc_response = ""

        irc_response = irc_response + irc.recv(1024).decode()

        log = str.split(irc_response, "\r")
        irc_response = log.pop()

        for line in log:
            print (line)
            if "PING" in line:
                irc.send("PONG".encode())
                break
            user = utilities.chat_user(line)
            message = utilities.chat_message(line)

            # Chat Command List
            command_list = ["!time", "!twitter", "!help"]

            if "!time" in message:
                utilities.chat(irc, "It is currently " + time.strftime("%I:%M %p %Z on %A, %B %d, %Y."))
            if "!twitter" in message:
                if "ENABLE" in config.TWITTER_COM:
                    utilities.chat(irc, "Check me out on Twitter: https://twitter.com/" + config.TWITTER_HANDLE + " !")
                else:
                    if "DISABLE" in config.TWITTER_COM:
                        utilities.chat(irc, "This command is not enabled, sorry!")
            if "!help" in message:
                utilities.chat(irc, "Command List: " + ", ".join(command_list))
            if "!kill" in message:
                utilities.chat(irc, "Shutting Down...")
                utilities.chat(irc, "Bye o/")
                return False
                break

if __name__ == "__main__":
    main()
