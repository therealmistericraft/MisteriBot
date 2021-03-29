# coding=utf-8

import discord
from discord.ext import commands
import json
from MisteriBot import lang
from MisteriBot import custom_prefixes



class Setprefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['changeprefix', 'cp', 'prefix'])
    async def setprefix(self, ctx, pPrefix):
        custom_prefixes[str(ctx.guild.id)] = pPrefix
        with open("../data/usr/prefix.json", "w") as prefixfile:
            json.dump(custom_prefixes, prefixfile, indent=4)
        await ctx.send(lang["setprefix1"]+custom_prefixes[str(ctx.guild.id)]+"`")



def setup(client):
    client.add_cog(Setprefix(client))
