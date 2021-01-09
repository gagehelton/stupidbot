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

    #determine value type
    try: payload = json.loads(stupid_quotes(args[1]))
    except json.decoder.JSONDecodeError:
        try: payload = int(args[1])
        except ValueError:
            try: payload = float(args[1])
            except ValueError: payload = args[1]
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
    jasonisms = [
    'Sixteenth chapel',
    'Take it for granite',
    'More often than none',
    'Mind bottling',
    'Rerecurring'
    ]
    await ctx.send(random.choice(jasonisms))

client.run(os.environ['DISCORD_TOKEN'])

