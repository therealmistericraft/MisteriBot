# coding=utf-8

import discord
from discord.ext import commands
import json
from MisteriBot import setCustomPrefixes
from MisteriBot import getLang
from MisteriBot import getCustomPrefixes



class Setprefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['changeprefix', 'cp', 'prefix'])
    async def setprefix(self, ctx, pPrefix):
        with await ctx.channel.typing():
            tempCustomPrefixes = getCustomPrefixes()
            tempCustomPrefixes[str(ctx.guild.id)] = pPrefix
            setCustomPrefixes(tempCustomPrefixes)
            with open("../data/usr/prefix.json", "w") as prefixfile:
                json.dump(getCustomPrefixes(), prefixfile, indent=4)
            await ctx.send(getLang()["setprefix1"]+tempCustomPrefixes[str(ctx.guild.id)]+"`")



def setup(client):
    client.add_cog(Setprefix(client))
