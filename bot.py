import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def jasonism(ctx):
    jasonisms = ['Sixteenth chapel',
    'Take it for granite',
    'More often than none',
    'Mind bottling',
    'Rerecurring']
    await ctx.send(random.choice(jasonisms))

client.run(os.environ['DISCORD_TOKEN'])
