# coding=utf-8

import discord
from discord.ext import commands
import json
from MisteriBot import langs



class Setlanguage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['lang', 'setlang','language', 'sprache'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def setlanguage(self, ctx, pLanguage):
        async with ctx.channel.typing():
            if pLanguage == "german" or pLanguage == "english":
                langs[str(ctx.guild.id)] = pLanguage
                with open("../data/usr/lang.json", "w") as langfile:
                    json.dump(langs, langfile, indent=4)
                await ctx.send("Language has been set up successfully! Your language: `"+pLanguage+"`")
            else:
                await ctx.send("Your language is not available. Available languages are: `german`, `english`")



def setup(client):
    client.add_cog(Setlanguage(client))
