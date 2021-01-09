#!/usr/bin/env python3
import discord
from discord.ext import commands
from common import stupid_quotes
import random
import os
import json
from modules import cnvrt

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('stupidbot is feeling stupid')

@client.command()
async def convert(ctx,*args):
    if('help' in args[0].lower()):
        await ctx.send(open('./help/convert.md','r').read())
        return
    print(args[1])

    #determine value type
    try: payload = json.loads(stupid_quotes(args[1]))
    except json.decoder.JSONDecodeError:
        payload = str(args[1]).strip()
        #try: payload = int(args[1])
        #except ValueError:
            #try: payload = float(args[1])
            #except ValueError: payload = args[1]
    except Exception as e: print(type(e).__name__,e.args)

    if(isinstance(payload,str)):
        if(args[0] == 'binary'):
            await ctx.send(cnvrt.str2binary(payload))
            return
        elif('hex' in args[0]):
            await ctx.send(cnvrt.str2hex(payload))
            return

    await ctx.send('failed to recognize command')
 
@client.command()
async def jasonism(ctx):
    await ctx.send(random.choice(open("./assets/jasonisms","r").readlines()))

client.run(os.environ['DISCORD_TOKEN'])

