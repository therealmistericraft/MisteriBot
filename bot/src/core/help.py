# coding=utf-8

import discord
from discord.ext import commands
import requests


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        page_url = 'https://raw.githubusercontent.com/wiki/therealmistericraft/MisteriBot/Commands.md'
        page = requests.get(page_url)
        page = page.text
        page = page.split('| --- | --- |')
        fields = page.split('|')
        #TODO: Bound 2 single fields to one cmd, remove withespaces
        print(page[1])



def setup(client):
    client.add_cog(Help(client))
