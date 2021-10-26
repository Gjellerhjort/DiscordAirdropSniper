#!/usr/bin/env python

import discord
import asyncio
import datetime

#TOKEN_AUTH = "MzU4MTk3NjA0OTk3MjY3NDU4.YVyOPg.BhbQHN9uiyrLUiaycZSD8gmjWdY" # Retrieved from browser local storage
client = discord.Client()

filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']
Channel_ID = config['Channel_ID']

@client.event
async def on_ready():
    print("ready")
    channel = client.get_channel(int(Channel_ID))
    await channel.send('Bot Active')
    print(client.users)

if __name__ == '__main__':
    client.run(TOKEN_AUTH, bot=False)
