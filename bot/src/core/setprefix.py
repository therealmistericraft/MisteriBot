# coding=utf-8

import discord
from discord.ext import commands
import json
from MisteriBot import setCustomPrefixes
from MisteriBot import getMsg
from MisteriBot import getCustomPrefixes



class Setprefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['changeprefix', 'cp', 'prefix'])
    async def setprefix(self, ctx, pPrefix):
        async with ctx.channel.typing():
            if pPrefix != '' and len(pPrefix) < 5:
                tempCustomPrefixes = getCustomPrefixes()
                tempCustomPrefixes[str(ctx.guild.id)] = pPrefix
                setCustomPrefixes(tempCustomPrefixes)
                with open("bot/data/usr/prefix.json", "w") as prefixfile:
                    json.dump(getCustomPrefixes(), prefixfile, indent=4)
                embed = discord.Embed(title='Success', description=getMsg("setprefix1")+tempCustomPrefixes[str(ctx.guild.id)]+"`", color=discord.Color.blue())
            else:
                embed = discord.Embed(title='Error 002', description=getMsg("setprefix2"), color=discord.Color.red())
            await ctx.send(content=None, embed=embed)



def setup(client):
    client.add_cog(Setprefix(client))
