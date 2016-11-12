import discord
from bs4 import BeautifulSoup
from urllib import request
from time import sleep 

client = discord.Client()
token = 'xxxx'

async def wikihow(message):
    try:
        url = 'http://www.wikihow.com/Special:Random'
        soup = BeautifulSoup(request.urlopen(url), 'html.parser')
        msg = soup.title.prettify()[8:-10]
        await client.send_message(message.channel, msg)
        print(msg)
    except:
        await wikihow(message)

@client.event
async def on_message(message):
    if message.content.startswith('!wikihow'):
        await wikihow(message)

client.run(token)
