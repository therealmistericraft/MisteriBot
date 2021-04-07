# coding=utf-8

import discord
from discord.ext import commands
from MisteriBot import change_status
import logging



class On_ready(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        logging.info('Ready')
        change_status.start()
        logging.info('Status loop started')



def setup(client):
    client.add_cog(On_ready(client))
