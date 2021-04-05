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
        page = page.json()
        print(page)
        #page = page.split('| --- | --- |')
        #print(page[1])



def setup(client):
    client.add_cog(Help(client))
