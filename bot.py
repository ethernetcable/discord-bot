import discord
from bs4 import BeautifulSoup
from urllib import request
from time import sleep 
from random import randint

client = discord.Client()
token = 'xxxx'

shank_bank = ['\*shanks %s*',
              '\*shivs %s*',
              '\*rips out %s\'s heart and feeds it to him*',
              '\*stabs %s*',
              '\*pushes %s off a bridge*',
              '\*feeds on %s\'s brain*',
              '\*kills %s to death*',
              '\*%s does a backflip off trump tower*',
              '\*%s reads a wikihow article on how to die*',
              '\*%s dies of old age*',
              '\*%s falls over and dies*',
              '\*%s hooks up with a nigerian prince, proceeds '
              'to die of bankruptcy']

ong_words = ['strong',
             'pong',
             'glong',
             'fong',
             'kong',
             'long',
             'trong',
             'frong',
             'tong',
             'extremely long',
             'donald trong',
             'michael gong',
             'kit smong',
             'jomes phillong',
             'aaron hong']

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
        num = randint(0, len(ong_words) - 1)
        msg = ong_words[num]
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

async def kill(message):
    try:
        user = message.content.split()[1]
        num = randint(0, len(shank_bank) - 1)
        msg = shank_bank[num]
        await client.send_message(message.channel, msg % user)
        print('killed someone')
    except:
        print('kill failed')

@client.event
async def on_message(message):
    if message.content.startswith('!wikihow'):
        await wikihow(message)
    if 'BONG' in message.content:
        await bigben(message)
    if message.content.startswith('test'):
        await test(message)
    if message.content.startswith('!kill'):
        await kill(message)

client.run(token)
