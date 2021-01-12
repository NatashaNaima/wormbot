import discord
import os
import random #tbd

#the bot
client = discord.Client()

#listen words
bot_prefix = ['z/','\\',',,']

#responses

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #bot does not respond to itself
        return
         
    # user messages bot checks
    msg = message.content 

    # checks every message for keywords
    if any(word in msg for word in bot_prefix): #user message to bot
        await message.delete() #bot response
    
    #direct bot commands 
    if msg.startswith('~addBot'): #add a bot prefix to list
      prefix = msg.split("~addBot ",1)[1]
      bot_prefix.append(prefix)
      await message.channel.send(bot_prefix[-1]+'? Ugh, a new bot to clean up after.')
    
    if msg.startswith('~delBot'): #removes a bot from the list
      prefix = msg.split("~delBot",1)[1]
      bot_prefix.remove(prefix)
      await message.channel.send(prefix+' is removed from the list. One less bot for me to clean up after.')

    if msg.startswith('~list'): #sends list of bot prefixes currently watching
      await message.channel.send(bot_prefix)

client.run(os.getenv('TOKEN'))