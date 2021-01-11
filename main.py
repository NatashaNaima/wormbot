import discord
import os
import random #tbd

#the bot
client = discord.Client()

#listen words
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
bot_prefix = []

#responses
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

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
    if any(word in msg for word in sad_words): #user message to bot
        await message.channel.send(random.choice(starter_encouragements)) #bot response
    
    #direct bot commands 
    if msg.startswith('~add'):
      prefix = msg.split("~add ",1)[1]
      bot_prefix.append(prefix)
      await message.channel.send(bot_prefix[-1]+'? Ugh, a new bot to clean up after?')


client.run(os.getenv('TOKEN'))