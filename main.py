#!/usr/bin/env python

import discord
import asyncio
import datetime

TOKEN_AUTH = "MzU4MTk3NjA0OTk3MjY3NDU4.YVyOPg.BhbQHN9uiyrLUiaycZSD8gmjWdY" # Retrieved from browser local storage

client = discord.Client()
filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']

@client.event
async def on_ready():
    print("ready")
    channel = client.get_channel(902218110113828878)
    message = await channel.fetch_message(channel.last_message_id)
    await channel.send('Bot Active')
    print(client.users)
    print(message)


client.run(TOKEN_AUTH, bot=False)
