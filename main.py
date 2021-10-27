#!/usr/bin/env python

import discord
import asyncio
from time import sleep
from discord import webhook
from discord.channel import TextChannel
from discord.embeds import Embed

client = discord.Client()
reactions = '\N{party popper}'

filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']
Channel_ID = config['Channel_ID']

@client.event
async def on_ready():
    print("ready")
    #print("Channel_ID: " + Channel_ID)

@client.event
async def on_message(message):
    MessageFrom = str(message.author)
    if MessageFrom == "DNIIBOY#7504":
        await message.add_reaction("\N{pinching hand}")
        print(MessageFrom)

    if MessageFrom == "sjazmin#4352":
        await message.add_reaction("\N{cross mark}")
        print(MessageFrom)

    if MessageFrom == "Burker#2138":
        await message.add_reaction("\N{cross mark}")
        print(MessageFrom)



if __name__ == '__main__':
    client.run(TOKEN_AUTH, bot=False)