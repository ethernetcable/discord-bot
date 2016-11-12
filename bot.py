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
        print('sent: ' + msg)
    except:
        print('wikihow fail')

async def bigben(message):
    try:
        msg = 'bong this bong that just shut your godddamn cakehole'
        await client.send_message(message.channel, msg)
        print('sent: ' + msg)
    except:
        print('bigben fail')

async def test(message):
    try:
        await client.send_message(message.channel, 'success')
        print('test success')
    except:
        print('test fail')

@client.event
async def on_message(message):
    if message.content.startswith('!wikihow'):
        await wikihow(message)
    if message.content.startswith('BONG'):
        await bigben(message)
    if message.content.startswith('test'):
        await test(message)

client.run(token)
