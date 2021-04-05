# coding=utf-8

import discord
from discord.ext import commands
from itertools import cycle



class On_ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Set custom status
    #status = cycle(['go.mistericraft.ga/misteribot', str(len(self.client.guilds))+' guilds'])
    #Add "ping me to get the prefix"
    #Start custom status cyclus
    #@tasks.loop(seconds=10)
    #async def change_status():
    #    await self.client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready')
        #change_status.start()



def setup(client):
    client.add_cog(On_ready(client))
