import discord
from bs4 import BeautifulSoup
from urllib import request
from time import sleep 
from random import randint
from twython import Twython, TwythonError

client = discord.Client()
token = 'xxxx'

CONSUMER_KEY = 'yyyy'
CONSUMER_SECRET = 'zzzz'
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

async def wikihow(message):
    try:
        url = 'http://www.wikihow.com/Special:Random'
        soup = BeautifulSoup(request.urlopen(url), 'html.parser')
        msg = soup.title.prettify()[8:-10].lower()
        await client.send_message(message.channel, msg)
        print('sent: ' + msg)
    except:
        sleep(0.1)
        print('retrying wikihow')
        await wikihow(message)

async def test(message):
    try:
        await client.send_message(message.channel, 'success')
        print('test success')
    except:
        print('test fail')

async def commands(message):
    try:
        msg = 'commands:\n`!kill`\n`!wikihow`\n`!test`\n`!wikicommands`\n`!ouch`\n`!trump`'
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

async def trump(message):
    try:
        trump = 'realDonaldTrump'
        tweet = twitter.get_user_timeline(screen_name=trump, count=1)[0]['text']
        msg = 'trump tweeted: ' + tweet
        await client.send_message(message.channel, msg)
        print('sent: ' + msg)
    except:
        sleep(0.1)
        print('retrying trump')
        await trump(message)
        
@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('-----')
        
@client.event
async def on_message(message):
    if message.content.startswith('!wikihow'):
        await wikihow(message)
    if message.content.startswith('!test'):
        await test(message)
    if message.content.startswith('!wikicommands'):
        await commands(message)
    if message.content.startswith('!ouch'):
        await ouch(message)
    uppers = [i for i in message.content if i.isupper()]
    if len(uppers) > 7:
        await shout(message)
    if message.content.startswith('!trump'):
        await trump(message)

client.run(token)
