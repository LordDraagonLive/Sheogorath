import discord
from discord.ext import commands

# print(discord.__version__) # check to make sure at least once you're on the right version!
token = open("config.ini", "r").read()  # I've opted to just save my token to a text file. 
# print(token)
client = discord.Client()  # starts the discord client.

async def replyBack(message):
    if str(message.author) == "LordDraagon#7410" and "hello" in message.content.lower():
        await message.channel.send('Greetings! Salutations! Welcome! Now go away. Leave. Run. Or die.')
    elif "see you later" == message.content:
        await message.channel.send('Wonderful! Time for a celebration... Cheese for everyone!')

async def getDetails(message,sheogorath_guild):
    # getting a member count
    if "sheogorath.member_count()" == message.content.lower():
        await message.channel.send(f"```{sheogorath_guild.member_count}```")
        # getting a community report
    elif "sheogorath.community_report()" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in sheogorath_guild.members:
            if str(m.status) == "online":
                online+=1
            if str(m.status) == "offline":
                offline+=1
            else:
                idle+=1
        await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

async def startEndBot(message):
    # End bot execution by sending a exit msg
 if "sheogorath.logout()" == message.content.lower():
    await message.channel.send('Isn\'t that a hoot? I love it, myself. Best part of being a Daedric Prince, really. Go ahead, try it again. He loves it!')
    await client.close()

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    # print(dir(message))

    # replying function
    await replyBack(message)

    # Get server ID
    sheogorath_guild = client.get_guild(408595867847622657)

    # Call get details function
    await getDetails(message,sheogorath_guild)

    # Call function to end the bot execution
    await startEndBot(message)


client.run(token)  # recall my token was saved!


