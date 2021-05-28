# coding=utf-8

#0 Documentation
#0.1 Threading usage
    # Only use threading.Thread, if asyncio.sleep is in the code snippet to use less performance

#0.2 Variables
    #0.2.1 prefix
        #prefixfile: file the custom prefixes are stored in
        #custom_prefixes: dict of custom prefixes in relation to guild id
        #prefix: prefix for current message (gets updated on message)
    #0.2.2 language
        #lang: dict of messages in language for guild of current message (link to msg_ger / msg_eng)
        #!Wherever a message multi-language message is used, "lang" must be declared as global!!!
        #langfile: file the choice of language is stored in
        #langs: dict of choosen languages in relation to guild id
        #gerfile: file the messages in german language are stored in
        #engfile: file the messages in english language are stored in
        #msg_ger: dict of messages in german
        #msg_eng: dict of messages in english

#0.3 Messages
    #lang[0]:

#0.4 Cogs
    #Since I work with cogs now, this file has only 2 (main) purposes: loading/unloading/reloading single or grouped cogs and transmitting variables, which are all stored in this file as a central place.
    #Everything else is in subfolders of the src folder.



#1 imports
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from itertools import cycle
import json
import os
import logging



#2 settings
#2.1 Activate Intents from API
intents = discord.Intents.all()
#2.2 Costumize logging behavior
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d; %H:%M:%S', level=logging.INFO)



#3 instance variables
prefix = ""
lang = {}
custom_prefixes = {}
langs = {}
msg_ger = {}
msg_eng = {}



#4 initalizing
#4.1 prefix
with open("bot/data/usr/prefix.json") as prefixfile:
    custom_prefixes = json.load(prefixfile)
default_prefix = '*'

#4.2 language
with open("bot/data/usr/lang.json") as langfile:
    langs = json.load(langfile)

#4.3 multi-language messages
#4.3.1 german
with open("bot/data/lang/german.json") as gerfile:
    msg_ger = json.load(gerfile)
#4.3.2 english
with open("bot/data/lang/english.json") as engfile:
    msg_eng = json.load(engfile)



#5 get- and set-methods
#5.1 get-Methods
def getPrefix():
    return prefix
def getLang():
    return lang
def getMsg(message):
    return lang[message]
def getCustomPrefixes():
    return custom_prefixes
def getDefaultPrefix():
    return default_prefix
def getLangs():
    return langs
def getMsgGer():
    return msg_ger
def getMsgEng():
    return msg_eng
#5.2 set-Methods
def setPrefix(pPrefix):
    global prefix
    prefix = pPrefix
def setLang(pLang):
    global lang
    lang = pLang
def setCustomPrefixes(pCustomPrefixes):
    global custom_prefixes
    custom_prefixes = pCustomPrefixes
def setLangs(pLangs):
    global langs
    langs = pLangs



#6.1 create bot instance
client = commands.Bot(command_prefix = "§", intents = intents)
client.remove_command('help')
#6.2 Set custom status
status = cycle(['go.mistericraft.ga/misteribot', str(len(client.guilds))+' guilds', 'pings to get the prefix'])
#6.3 start status loop
@tasks.loop(seconds=20)
async def change_status():
    #Start custom status cyclus
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))



#7 Load specific cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    if extension+".py" in os.listdir("bot/src/events"):
        client.load_extension(f"events.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Event was loaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Event "'+extension+'" loaded')
    elif extension+".py" in os.listdir("bot/src/core"):
        client.load_extension(f"core.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Command was loaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Core command "'+extension+'" loaded')
    else:
        logging.warning('Extension "'+extension+'" not found')
        await ctx.send(content=None, embed=discord.Embed(title='Error', description='Extension `'+extension+'` not found', colour=discord.Colour.red()))



#8 unload specific cogs
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if extension+".py" in os.listdir("bot/src/events"):
        client.unload_extension(f"events.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Event was unloaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Event "'+extension+'" unloaded')
    elif extension+".py" in os.listdir("bot/src/core"):
        client.unload_extension(f"core.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Command was unloaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Core command "'+extension+'" unloaded')
    else:
        logging.warning('Extension "'+extension+'" not found')
        await ctx.send(content=None, embed=discord.Embed(title='Error', description='Extension `'+extension+'` not found', colour=discord.Colour.red()))



#9 reload specific cogs
@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    if extension+".py" in os.listdir("bot/src/events"):
        client.unload_extension(f"events.{extension}")
        client.load_extension(f"events.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Event was reloaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Event "'+extension+'" reloaded')
    elif extension+".py" in os.listdir("bot/src/core"):
        client.unload_extension(f"core.{extension}")
        client.load_extension(f"core.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Command was reloaded.", description=extension, colour=discord.Colour.orange()))
        logging.info('Core command "'+extension+'" reloaded')
    else:
        logging.warning('Extension "'+extension+'" not found')
        await ctx.send(content=None, embed=discord.Embed(title='Error', description='Extension `'+extension+'` not found', colour=discord.Colour.red()))



#10 Activating/loading all cogs on startup
for filename in os.listdir("bot/src/events"):
    if filename.endswith(".py"):
        client.load_extension(f"events.{filename[:-3]}")
        logging.info('All events loaded')
for filename in os.listdir("bot/src/core"):
    if filename.endswith(".py"):
        client.load_extension(f"core.{filename[:-3]}")
        logging.info('All core commands loaded')




#11 Token
with open("token.txt", "r") as tokenfile:
    token = tokenfile.read()
client.run(token)
