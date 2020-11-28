import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "_")

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_member_update(before, after):
    if after.id == 707242307610476595:
        if str(after.status) == "offline":
            channel=client.get_channel(738855769730187304)
            embed=discord.Embed(title=":red_circle: Outage detected", description="Outage automatically detected. Please wait for <@303166734557380608> for further information.", colour=discord.Colour.red())
            await channel.send(content=None, embed=embed)
            dmchannel=client.get_user(707242307610476595)
            await dmchannel.send("<@303166734557380608> MisteriBot offline.")
    if after.id == 708584393555312690:
        if str(after.status)=="offline":
            dmchannel=client.get_user(707242307610476595)
            await dmchannel.send("<@303166734557380608> MisteriBot W.I.P. offline.")

client.run("")
