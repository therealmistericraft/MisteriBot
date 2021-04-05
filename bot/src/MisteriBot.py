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
import json
import os



#2 settings
#2.1 Activate Intents from API
intents = discord.Intents.all()



#3 instance variables
prefix = ""
lang = {}
custom_prefixes = {}
langs = {}
msg_ger = {}
msg_eng = {}



#4 initalizing
#4.1 prefix
with open("../data/usr/prefix.json") as prefixfile:
    custom_prefixes = json.load(prefixfile)
default_prefix = '*'

#4.2 language
with open("../data/usr/lang.json") as langfile:
    langs = json.load(langfile)

#4.3 multi-language messages
#4.3.1 german
with open("../data/lang/german.json") as gerfile:
    msg_ger = json.load(gerfile)
#4.3.2 english
with open("../data/lang/english.json") as engfile:
    msg_eng = json.load(engfile)



#5 get- and set-methods
#5.1 get-Methods
def getPrefix():
    return prefix
def getLang():
    return lang
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



#7 Load specific cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    if extension+".py" in os.listdir("./events"):
        client.load_extension(f"events.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Event was loaded.", description=None, colour=discord.Colour.orange()))
    if extension+".py" in os.listdir("./core"):
        client.load_extension(f"core.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Command was loaded.", description=None, colour=discord.Colour.orange()))



#8 unload specific cogs
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if extension+".py" in os.listdir("./events"):
        client.unload_extension(f"events.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Event was unloaded.", description=None, colour=discord.Colour.orange()))
    if extension+".py" in os.listdir("./core"):
        client.unload_extension(f"core.{extension}")
        await ctx.send(content=None, embed=discord.Embed(title="Command was unloaded.", description=None, colour=discord.Colour.orange()))



#9 reload specific cogs
@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    if extension+".py" in os.listdir("./events"):
        await ctx.send(content=None, embed=discord.Embed(title="Event was reloaded.", description=None, colour=discord.Colour.orange()))
        client.unload_extension(f"events.{extension}")
        client.load_extension(f"events.{extension}")
    if extension+".py" in os.listdir("./core"):
        await ctx.send(content=None, embed=discord.Embed(title="Command was reloaded.", description=None, colour=discord.Colour.orange()))
        client.unload_extension(f"core.{extension}")
        client.load_extension(f"core.{extension}")



#10 Activating/loading all cogs on startup
for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        client.load_extension(f"events.{filename[:-3]}")
for filename in os.listdir("./core"):
    if filename.endswith(".py"):
        client.load_extension(f"core.{filename[:-3]}")




#11 Token
with open("token.txt", "r") as tokenfile:
    token = tokenfile.read()
client.run(token)
