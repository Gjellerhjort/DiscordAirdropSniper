#!/usr/bin/env python

import discord
import asyncio
from time import sleep

client = discord.Client()
reaction = '\N{party popper}'

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

@client.event
async def on_message(message):
    MessageFrom = str(message.author)
    if MessageFrom == "tip.cc#7731":
        print("new aidrop")
        await message.add_reaction(reaction)



if __name__ == '__main__':
    client.run(TOKEN_AUTH, bot=False)