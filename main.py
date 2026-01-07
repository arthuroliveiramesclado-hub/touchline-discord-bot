import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot online!")

@bot.command()
async def build(ctx):
    await ctx.send("Build atacante: Drible 4.5⭐ | Passe 3⭐ | Chute 2.5⭐")

bot.run(os.getenv("TOKEN"))
