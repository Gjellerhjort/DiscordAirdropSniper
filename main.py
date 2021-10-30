#!/usr/bin/env python

import discord
import asyncio
import datetime
from time import sleep
from discord import webhook
from discord.channel import TextChannel
from discord.embeds import Embed

client = discord.Client()

filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']
Channel_ID = config['Channel_ID']

@client.event
async def on_ready():
    print("ready")
<<<<<<< HEAD
    channel = client.get_channel(int(Channel_ID))
    await channel.send('Bot Active')
    print(client.users)
    


if __name__ == '__main__':
    client.run(TOKEN_AUTH, bot=False)
    client.run(TOKEN_AUTH, bot=False)