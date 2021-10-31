import requests
import json

filename = "config"
contents = open(filename).read()
config = eval(contents)
TOKEN_AUTH = config['Token_AUTH']
Channel_ID = config['Channel_ID']

def retrieve_messages(channelid):
    headers = {
        'authorization' : TOKEN_AUTH
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value['content'], '\n')

retrieve_messages("902218110113828878")
