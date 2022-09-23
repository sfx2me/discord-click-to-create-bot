from ssl import CHANNEL_BINDING_TYPES
import discord
from discord.ext import commands
from discord.ui import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_voice_state_update(member, before, after):
    s = bot.get_guild(server id here)
    try:
        if after.channel.id == channel id here:
            global channel
            channel = await s.create_voice_channel(str(member).split("#")[0])
            await member.move_to(channel)
    except:
        try: await channel.delete()
        except: pass

bot.run("token here obv")