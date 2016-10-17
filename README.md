# Rosza

[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://raw.githubusercontent.com/aerovolts/rosza/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@aerovolts-55acee.svg?style=flat-square)](https://twitter.com/aerovolts)

A simple chat bot for Twitch written in Python 3. She doesn't do much, but it's something.

## Setup

To run this bot on your [twitch.tv](https://twitch.tv) channel simply download download or `git clone` the repository.

Open `config.py` and replace the `NICKNAME`, `PASSWORD`, AND `CHANNEL` fields with the relevant information listed in the docstring at the top.

The OAuth Token can be found at [twitchapps.com/tmi/](http://twitchapps.com/tmi/). Make sure you get the token from the account that will be running the bot, so presumably not your primary broadcasting account.

Run `python rosza.py` in a terminal window and Rosza will initiate connection to Twitch and let you know in your channel chat that she is ready!

## Todo

- [ ] Add moderator checks to some commands like `!kill`
- [ ] Add automatic timeout/ban on broadcaster defined phrases or words
- [ ] Dynamically generate command list for all enabled commands
