#!/usr/bin/env python

import discord
import asyncio
import os
from time import sleep
from discord import message
from discord.message import Message
import requests
import json



client = discord.Client()
reaction = '\N{party popper}'
AirdropsJoined = 0
airdropStatus = "false"
filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']
Channel_ID = config['Channel_ID']

def retrieve_messages(channelid, messageid):
    bannedchannels = [846864477642031174, 889908778395385936, 846854228386250795, 884115738741325905, 900880235086626846, 847894288322265110, 903483119489933373]
    messageDetailsDict = {}
    headers = {
        'authorization' : TOKEN_AUTH
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        if value['id'] == messageid and int(channelid) not in bannedchannels:
            messageDetails = value['embeds']
            if len(messageDetails) != 0:
                messageDetailsDict = dict(messageDetails[-1])
                try:
                    if 'An airdrop appears' in messageDetailsDict['title']:
                        if 'React with 🎉' in messageDetailsDict['description']:
                            airdropStatus = True
                            return airdropStatus
                except:
                    continue

@client.event
async def on_ready():
    print("ready")
    channel = client.get_channel(int(Channel_ID))
    await channel.send('Bot Active')

@client.event
async def on_message(message):
    MessageFrom = str(message.author)
    if MessageFrom == "tip.cc#7731":
        Messageid = str(message.id)
        MessageChannelId = str(message.channel.id)
        airdropStatus = retrieve_messages(MessageChannelId, Messageid)
        if airdropStatus == True:
            sleep(2)
            print("joined new airdrop in " + message.channel.name)
            await message.add_reaction(reaction)
            airdropStatus = False



if __name__ == '__main__':
    client.run(TOKEN_AUTH, bot=False)