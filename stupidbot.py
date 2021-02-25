#!/root/stupidbot_env/bin/python3
import discord
from discord.ext import commands
from common import stupid_quotes
import random
import os
import logg3r
from modules import cnvrt,inspirobot,avcalc

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('stupidbot is feeling stupid')

#@client.command()
#async def help(ctx):
#    await ctx.send("https://github.com/gagehelton/stupidbot")

@client.command()
async def test(ctx):
    await ctx.send(embed=discord.Embed(title="Hello",description="Use `!help` test!"))

@client.command(aliases=['468'])
async def fourSixEight(ctx,*args):
    fmt = '''
**Display Sizes for Furthest Viewer @ {feet}'**
1/4 = {four[0]} - {four[1]}
1/6 = {six[0]} - {six[1]}
1/8 = {eight[0]} - {eight[1]}
'''.format(**avcalc.fourSixEight.get_display_size(int(args[0])))

    await ctx.send(fmt)

@client.command(aliases=['mm'])
async def mm2in(ctx,*args):
    a = "".join([str(i) for i in args])
    result = avcalc.mm2in(a)
    if(result):
        fmt = '''
**Millimeters to Inches**
{_MM}
{_IN}
'''.format(**result)
    else:
        fmt = '''FAIL'''

    await ctx.send(fmt)    

@client.command()
async def wisdom(ctx):
    f = inspirobot.generate()
    await ctx.send(file=discord.File(f))
    os.remove(f)
 
@client.command()
async def jimmy(ctx):
    path = '/root/stupidbot_dropbox/jimmy/'
    j = random.choice(os.listdir(path))
    await ctx.send(file=discord.File(path+'/'+j))

@client.command()
async def jasonism(ctx):
    await ctx.send(random.choice(open("/root/stupidbot/assets/jasonisms","r").readlines()))

@client.command()
async def convert(ctx,*args):
    try:
        if('help' in args[0].lower()):
            await ctx.send(open('./help/convert.md','r').read())
            return

        payload = str(args[1]).strip()

        if(isinstance(payload,str)):
            if(args[0] == 'binary'):
                await ctx.send(cnvrt.str2binary(payload))
                return
            elif('hex' in args[0]):
                await ctx.send(cnvrt.str2hex(payload))
                return

        await ctx.send('failed to recognize command')
    except Exception as e:
         print(type(e).__name__,e.args) #LOG!
         
client.run(os.environ['DISCORD_TOKEN'])

