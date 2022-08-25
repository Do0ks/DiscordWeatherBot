#When the guild pictures change, they print out the image name. So, if you have a cloudy weather image, name your gif "weather has turned cloudy.gif". 
#When line 30 is called it will post the gif name to the chat.

from discord.ext import commands
import asyncio
import random
import os


Bot_Prefix = "~" #change prefix to your liking.
bot = commands.Bot(command_prefix=Bot_Prefix, case_insensitive=True, self_bot=False)

@bot.event
async def on_connect(): 
    print("Connecting...")

@bot.event
async def on_ready():
    print("WeatherBot is online.")

async def weather(ctx):
    while True:
        rand = random.choice(os.listdir("Directory to pictures or gifs")) #server must hold 2 server boosts to use gifs
        with open("Directory to pictures or gifs" + rand, 'rb') as f: #Same directory as above.
            icon = f.read()
        await ctx.guild.edit(icon=icon)
        size = len(rand)
        nrand = rand[:size -4] #Change this only if you're uploading something different other than a gif. Number corresponds with the file extension including the . so when it prints out to the chat it won't include .gif (4). If the extension is something like .jpeg it would be 5.
        channel = bot.get_channel(Channel_ID) #Channel to post weather changes to
        await channel.send("Weather forcast: " + nrand, delete_after=7100) #Check note at the top, also deletes last message before new one is posted to keep chat clean.
        await asyncio.sleep(7200) #Sleeps 2 hours.

#Starts a 2 hour loop.
@bot.command()
async def weather(ctx): 
    bot.loop.create_task(weather(ctx))
    print("started") 


bot.run("Discord_Bot_Token", bot=True, reconnect=True)
