import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']



intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

webserver.keep_alive()
bot.run(DISCORD_TOKEN)
