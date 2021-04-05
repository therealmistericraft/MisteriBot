# coding=utf-8

import discord
from discord.ext import commands
import json
import random
from MisteriBot import getLang
from MisteriBot import getLangs
from MisteriBot import getMsgGer
from MisteriBot import getMsgEng
from MisteriBot import getPrefix
from MisteriBot import getCustomPrefixes
from MisteriBot import getDefaultPrefix
from MisteriBot import setLang
from MisteriBot import setLangs
from MisteriBot import setPrefix
from MisteriBot import setCustomPrefixes



class On_message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        #ignore messages by bots
        if message.author.bot == False:
            #check for language
            if message.guild:
                #check for prefix
                if str(message.guild.id) in getCustomPrefixes():
                    setPrefix(getCustomPrefixes()[str(message.guild.id)])
                else:
                    setPrefix(getDefaultPrefix())
                if message.content != '*setlanguage':
                    if str(message.guild.id) in getLangs():
                        if getLangs()[str(message.guild.id)] == 'german':
                            setLang(getMsgGer())
                        elif getLangs()[str(message.guild.id)] == 'english':
                            setLang(getMsgEng())
                        else:
                            message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='That is my fault - I forgot which language you speak! Please contact the owner of the server, which can set up the language again with `'+prefix+'setlanguage`.', colour=discord.Colour.red()))
                    elif message.content.startswith(getPrefix()):
                        await message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='There is no language set up for this guild/server. Please contact the owner of the server, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
            #error if DMChannel
            else:
                await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='This Bot is not available in direct chats or an unexpected error occured. Please try again on a guild/server.\nTo send my developer a message, write a DM to `MisteriCraft#5019`', colour=discord.Colour.red()))
            #set determined prefix
            self.client.command_prefix = getPrefix()


            #answers
            #prefix inquiry
            if message.content == "prefix":
                embed = discord.Embed(title="The prefix of this server is ``"+prefix+"``.", colour=discord.Colour.blue())
                await message.channel.send(content=None, embed=embed)

            #hello
            if any(word in message.content.lower() for word in ["hallo", "hello", "hi", "moin", "hey", "tach", "morning", "servus"]):
                hello = ["https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627", "https://tenor.com/view/baby-yoda-baby-yoda-wave-baby-yoda-waving-hi-hello-gif-15975082", "https://tenor.com/view/inside-out-joy-hi-hey-hello-gif-4763730", "https://tenor.com/view/hello-funny-wave-chicken-gif-13330039", "https://tenor.com/view/hi-husky-hello-cute-gif-15361405"]
                id = random.randint(0, len(hello)-1)
                await message.channel.send(hello[id])



def setup(client):
    client.add_cog(On_message(client))
