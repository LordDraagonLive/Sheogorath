import discord
from discord.ext import commands

# print(discord.__version__) # check to make sure at least once you're on the right version!
token = open("config.ini", "r").read()  # I've opted to just save my token to a text file. 
# print(token)
client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message. 

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    # print(dir(message))
    if str(message.author) == "LordDraagon#7410" and "hello" in message.content.lower():
        await message.channel.send('Hi!') 

client.run(token)  # recall my token was saved!


