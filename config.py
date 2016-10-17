"""
Configuration information for RoszaBot. Connects via the Twitch IRC interface.

HOST and PORT are set by the Twitch API and should not be changed
NICKNAME is the bot account's username in lowercase
PASSWORD is a Twitch OAuth token that can be gotten from http://twitchapps.com/tmi/
CHANNEL is the Twitch channel chat to connect to

Command options can be found below that customize the commands.
"""

# Twitch IRC API settings
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICKNAME = "NICKNAME"
PASSWORD = "PASSWORD"
CHANNEL = "CHANNEL"

# Command specific settings
TWITTER_COM = "DISABLE" #ENABLE or DISABLE
TWITTER_HANDLE = "TWITTER_HANDLE"
