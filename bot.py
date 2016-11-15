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
              'to die of bankruptcy*']

async def wikihow(message):
    try:
        url = 'http://www.wikihow.com/Special:Random'
        soup = BeautifulSoup(request.urlopen(url), 'html.parser')
        msg = soup.title.prettify()[8:-10]
        await client.send_message(message.channel, msg)
        print('sent: ' + msg)
    except:
        print('retrying wikihow')
        sleep(0.1)
        await wikihow(message)

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

async def commands(message):
    try:
        msg = 'commands:\n`!kill`\n`!wikihow`\n`!test`\n`!wikicommands`\n`!ouch`'
        await client.send_message(message.channel, msg)
        print('sent: commands')
    except:
        print('commands fail')

async def ouch(message):
    try:
        await client.send_message(message.channel, 'ouch', tts=True)
        print('said ouch')
    except:
        print('ouch fail')

async def shout(message):
    try:
        await client.send_message(message.channel, 'shhh i\'m trying to sleep')
        print('someone is being very loud')
    except:
        print('shout fail')

@client.event
async def on_message(message):
    if message.content.startswith('!wikihow'):
        await wikihow(message)
    if message.content.startswith('test'):
        await test(message)
    if message.content.startswith('!kill'):
        await kill(message)
    if message.content.startswith('!wikicommands'):
        await commands(message)
    if message.content.startswith('!ouch'):
        await ouch(message)
    uppers = [i for i in message.content if i.isupper()]
    if len(uppers) > 4:
        await shout(message)

client.run(token)
