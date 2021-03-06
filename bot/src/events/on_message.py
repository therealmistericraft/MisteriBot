# coding=utf-8

import discord
from discord.ext import commands
import json
import sys
sys.path.append("../")
import MisteriBot as main



class On_message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        #check for language
        if message.guild:
            if not message.content == '*setlanguage':
                if main.langs[str(message.guild.id)]:
                    if main.langs[str(message.guild.id)] == "german":
                        main.lang = main.msg_ger
                    if main.langs[str(message.guild.id)] == "english":
                        main.lang = main.msg_eng
                elif message.content.startswith == main.prefix:
                    await message.channel.send(content=None, embed=discord.Embed(title='Error 001', description='There is no language set up for this guild/server. Please contact the owner of the server, which can set up the language with `*setlanguage`.', colour=discord.Colour.red()))
            #check for prefix
            if main.custom_prefixes[str(message.guild.id)]:
                main.prefix = main.custom_prefixes[str(message.guild.id)]
            else:
                main.prefix = main.default_prefix
        #error if DMChannel
        else:
            await message.channel.send(content=None, embed=discord.Embed(title='Error 002', description='This Bot is not available in direct chats or an unexpected error occured. Please try again on a guild/server.\nTo send my developer a message, write a DM to `MisteriCraft#5019`', colour=discord.Colour.red()))
        #set determined prefix
        main.client.command_prefix = main.prefix


        #answers
        #prefix inquiry
        if message.content == "prefix":
            embed = discord.Embed(title="The prefix of this server is ``"+prefix+"``.", colour=discord.Colour.blue())
            await message.channel.send(content=None, embed=embed)

        #hello
        if any(word in message.content.lower() for word in ["hallo", "hello", "hi", "moin", "hey", "tach", "morning"]):
            hello = ["https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627", "https://tenor.com/view/baby-yoda-baby-yoda-wave-baby-yoda-waving-hi-hello-gif-15975082", "https://tenor.com/view/inside-out-joy-hi-hey-hello-gif-4763730", "https://tenor.com/view/hello-funny-wave-chicken-gif-13330039", "https://tenor.com/view/hi-husky-hello-cute-gif-15361405"]
            id = random.randint(0, hello.length)
            await message.channel.send(hello[id])



def setup(client):
    client.add_cog(On_message(client))
